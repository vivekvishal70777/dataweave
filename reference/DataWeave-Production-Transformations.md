# DataWeave production transformations

Hard **DataWeave 2.0** mappings you see on real Mule 4 projects: canonical APIs, partial failure, money, joins, overlays, CDC, and batching. Each lab is self-contained (`payload` only — no hidden `vars`) so it runs in the Playground.

Levels: **Production (55–82)** — **28 programs**. Do these after Labs 37–54.

Try the problem before the solution. In interviews, say the **rules** first (precedence, rounding, what happens on bad rows), then write the script.

---

## Production (55–82)

### 55. Canonical order API with line errors

**Problem:** Map a commerce order to a canonical JSON API. Compute `lineTotal`, `subtotal`, `tax`, `grandTotal`. If a line has a non-numeric `qty` or `price`, omit it from `lines` and append `{ sku, reason }` to `errors`. Missing `customerId` becomes `null` (do not fail the whole document).

**Production rules:** Round money to 2 decimal places via `as String {format: "0.00"} as Number`. Tax applies only to the successful subtotal. Keep `correlationId` from the source.

**Input:**

```json
{
  "correlationId": "corr-9",
  "customerId": null,
  "taxRate": 0.18,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50 },
    { "sku": "B", "qty": "bad", "price": 100 },
    { "sku": "C", "qty": 1, "price": 100 }
  ]
}
```

**Expected:**

```json
{
  "correlationId": "corr-9",
  "customerId": null,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50, "lineTotal": 100 },
    { "sku": "C", "qty": 1, "price": 100, "lineTotal": 100 }
  ],
  "subtotal": 200,
  "tax": 36,
  "grandTotal": 236,
  "errors": [
    { "sku": "B", "reason": "qty or price is not numeric" }
  ]
}
```

**Interview talking point:** Partial success is normal in B2B: ship the good lines, park bad lines in `errors[]` (or a DLQ field). Do not hide HTTP/DB calls inside the `map`.

**Solution:**

```dataweave
%dw 2.0
import try from dw::Runtime
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
fun lineOk(l) =
  try(() -> (l.qty as Number) >= 0 and (l.price as Number) >= 0).success default false
var parsed = payload.lines map (l) -> {
  sku: l.sku,
  ok: lineOk(l),
  qty: try(() -> l.qty as Number).result,
  price: try(() -> l.price as Number).result
}
var good = parsed filter $.ok map (l) -> {
  sku: l.sku,
  qty: l.qty,
  price: l.price,
  lineTotal: money(l.qty * l.price)
}
var subtotal = money(sum(good.lineTotal default []))
var tax = money(subtotal * payload.taxRate)
---
{
  correlationId: payload.correlationId,
  customerId: payload.customerId default null,
  lines: good,
  subtotal: subtotal,
  tax: tax,
  grandTotal: money(subtotal + tax),
  errors: parsed filter !$.ok map {
    sku: $.sku,
    reason: "qty or price is not numeric"
  }
}
```

---

### 56. Customer 360 merge with field precedence

**Problem:** Merge `erp`, `crm`, and `mdm` profiles for one customer. Scalar field precedence: **MDM > CRM > ERP**. `emails` is a union of unique lowercase addresses. `addresses` merge by `type` (same precedence for overlapping fields).

**Production rules:** Do not let a `null` in a higher source wipe a lower source’s value. Right-hand `++` would wipe; use `default` per field.

**Input:**

```json
{
  "erp": {
    "id": "E-1",
    "name": "Acme ERP",
    "phone": "111",
    "emails": ["ERP@X.com"],
    "addresses": [{ "type": "BILL", "city": "Pune", "line": "Old" }]
  },
  "crm": {
    "id": "C-1",
    "name": "Acme CRM",
    "phone": null,
    "emails": ["crm@x.com"],
    "addresses": [{ "type": "SHIP", "city": "Mumbai" }]
  },
  "mdm": {
    "id": "M-1",
    "name": null,
    "phone": "999",
    "emails": ["mdm@x.com"],
    "addresses": [{ "type": "BILL", "city": "Pune", "line": "HQ" }]
  }
}
```

**Expected:**

```json
{
  "id": "M-1",
  "name": "Acme CRM",
  "phone": "999",
  "emails": ["crm@x.com", "erp@x.com", "mdm@x.com"],
  "addresses": [
    { "type": "BILL", "city": "Pune", "line": "HQ" },
    { "type": "SHIP", "city": "Mumbai", "line": null }
  ]
}
```

**Interview talking point:** Golden-record merges need **explicit precedence**, unique keys for collections, and null-safe coalesce — not a blind `++`.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun pick(mdm, crm, erp) = mdm default (crm default erp)
fun addrKey(a) = a.type
fun mergeAddr() = do {
  var tagged =
    (payload.erp.addresses default [] map $ ++ { _src: 0 })
      ++ (payload.crm.addresses default [] map $ ++ { _src: 1 })
      ++ (payload.mdm.addresses default [] map $ ++ { _src: 2 })
  var byType = tagged groupBy addrKey
  ---
  namesOf(byType) map (t) -> do {
    var rows = byType[t]
    var erp = (rows filter ((r) -> r._src == 0))[0]
    var crm = (rows filter ((r) -> r._src == 1))[0]
    var mdm = (rows filter ((r) -> r._src == 2))[0]
    ---
    {
      type: t as String,
      city: pick(mdm.city, crm.city, erp.city),
      line: pick(mdm.line, crm.line, erp.line)
    }
  }
}
var stacked = [payload.erp, payload.crm, payload.mdm]
---
{
  id: pick(payload.mdm.id, payload.crm.id, payload.erp.id),
  name: pick(payload.mdm.name, payload.crm.name, payload.erp.name),
  phone: pick(payload.mdm.phone, payload.crm.phone, payload.erp.phone),
  emails: (stacked.emails flatten map lower($)) distinctBy $ orderBy $,
  addresses: mergeAddr()
}
```

---

### 57. CDC envelope to domain events

**Problem:** Each change-data-capture row has `op` (`c` create, `u` update, `d` delete), `before`, `after`, and `ts`. Emit domain events. Deletes use `before` as `record`. Unknown `op` → skip (do not fail the batch).

**Input:**

```json
{
  "changes": [
    { "op": "c", "before": null, "after": { "id": "1", "name": "Asha" }, "ts": "2026-08-20T10:00:00Z" },
    { "op": "u", "before": { "id": "1", "name": "Asha" }, "after": { "id": "1", "name": "Asha R" }, "ts": "2026-08-20T11:00:00Z" },
    { "op": "d", "before": { "id": "2" }, "after": null, "ts": "2026-08-20T12:00:00Z" },
    { "op": "x", "before": null, "after": { "id": "9" }, "ts": "2026-08-20T13:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "type": "created", "id": "1", "record": { "id": "1", "name": "Asha" }, "ts": "2026-08-20T10:00:00Z" },
  { "type": "updated", "id": "1", "record": { "id": "1", "name": "Asha R" }, "ts": "2026-08-20T11:00:00Z" },
  { "type": "deleted", "id": "2", "record": { "id": "2" }, "ts": "2026-08-20T12:00:00Z" }
]
```

**Interview talking point:** CDC mappings must be **idempotent** downstream (same event twice = same business result). Tombstones (`op=d`) still need a stable `id`.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun event(c) =
  c.op match {
    case "c" -> { type: "created", id: c.after.id, record: c.after, ts: c.ts }
    case "u" -> { type: "updated", id: c.after.id, record: c.after, ts: c.ts }
    case "d" -> { type: "deleted", id: c.before.id, record: c.before, ts: c.ts }
    else -> null
  }
---
payload.changes map event($) filter $ != null
```

---

### 58. Multi-currency invoice with FX table

**Problem:** Convert each line to USD using `rates` (units of USD per 1 unit of `currency`). If a rate is missing, the line is an error and excluded from `totalUsd`.

**Input:**

```json
{
  "rates": { "USD": 1, "EUR": 1.1 },
  "lines": [
    { "sku": "A", "amount": 100, "currency": "EUR" },
    { "sku": "B", "amount": 50, "currency": "USD" },
    { "sku": "C", "amount": 20, "currency": "GBP" }
  ]
}
```

**Expected:**

```json
{
  "lines": [
    { "sku": "A", "amount": 100, "currency": "EUR", "amountUsd": 110 },
    { "sku": "B", "amount": 50, "currency": "USD", "amountUsd": 50 }
  ],
  "totalUsd": 160,
  "errors": [
    { "sku": "C", "reason": "missing FX rate for GBP" }
  ]
}
```

**Interview talking point:** FX belongs in a **table** (Object keyed by currency), not an HTTP `lookup` per line. Pin the rate timestamp in production (not shown here).

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var rated = payload.lines map (l) -> do {
  var rate = payload.rates[l.currency]
  ---
  l ++ {
    amountUsd: if (rate != null) money((l.amount as Number) * rate) else null,
    fxError: rate == null
  }
}
var good = rated filter !$.fxError
---
{
  lines: good map {
    sku: $.sku,
    amount: $.amount,
    currency: $.currency,
    amountUsd: $.amountUsd
  },
  totalUsd: money(sum(good.amountUsd)),
  errors: rated filter $.fxError map {
    sku: $.sku,
    reason: "missing FX rate for " ++ $.currency
  }
}
```

---

### 59. Bill of materials: explode one level

**Problem:** Each product has `components` (sku list). Replace each component sku with `{ sku, name, unitCost }` from `catalog`. Unknown sku → `{ sku, name: null, unitCost: null, missing: true }`. Output the parent with `exploded` and `bomCost` (sum of known costs only).

**Input:**

```json
{
  "catalog": [
    { "sku": "P", "name": "Pump", "unitCost": 10, "components": ["G", "S"] },
    { "sku": "G", "name": "Gasket", "unitCost": 2, "components": [] },
    { "sku": "S", "name": "Screw", "unitCost": 1, "components": [] }
  ],
  "parentSku": "P"
}
```

**Expected:**

```json
{
  "sku": "P",
  "name": "Pump",
  "exploded": [
    { "sku": "G", "name": "Gasket", "unitCost": 2, "missing": false },
    { "sku": "S", "name": "Screw", "unitCost": 1, "missing": false }
  ],
  "bomCost": 3
}
```

**Interview talking point:** One-level explode is a **groupBy catalog** lookup. Multi-level explode is recursion plus a cycle guard (visited set) — mention it; do not infinite-loop in production.

**Solution:**

```dataweave
%dw 2.0
output application/json
var bySku = payload.catalog groupBy ((c) -> c.sku)
var parent = bySku[payload.parentSku][0]
fun part(sku) = do {
  var c = (bySku[sku] default [])[0]
  ---
  {
    sku: sku,
    name: c.name default null,
    unitCost: c.unitCost default null,
    missing: c == null
  }
}
var exploded = (parent.components default []) map part($)
---
{
  sku: parent.sku,
  name: parent.name,
  exploded: exploded,
  bomCost: sum((exploded filter !$.missing).unitCost)
}
```

---

### 60. Bank statement rows plus trailer checksum

**Problem:** `rows` are transactions; the last object with `type == "TRAILER"` holds `total`. Sum `amount` of non-trailer rows. Return `{ total, expected, balanced, items }`.

**Input:**

```json
{
  "rows": [
    { "type": "TXN", "id": "1", "amount": 10.5 },
    { "type": "TXN", "id": "2", "amount": 4.5 },
    { "type": "TRAILER", "total": 15 }
  ]
}
```

**Expected:**

```json
{
  "items": [
    { "id": "1", "amount": 10.5 },
    { "id": "2", "amount": 4.5 }
  ],
  "total": 15,
  "expected": 15,
  "balanced": true
}
```

**Interview talking point:** File-based banking/EDI often has **control totals**. Fail the flow (or route to ops) when `balanced` is false; do not post partial ledgers.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var items = payload.rows filter ((r) -> r.type != "TRAILER") map {
  id: $.id,
  amount: $.amount as Number
}
var trailer = payload.rows filter ((r) -> r.type == "TRAILER")[-1]
var total = money(sum(items.amount))
var expected = money(trailer.total as Number)
---
{
  items: items,
  total: total,
  expected: expected,
  balanced: total == expected
}
```

---

### 61. Pagination envelope for a list API

**Problem:** Page `page` (1-based) of `size` over `items`. Return the window plus `total`, `hasMore`, and `nextPage` (`null` if none).

**Input:**

```json
{
  "page": 2,
  "size": 2,
  "items": [1, 2, 3, 4, 5]
}
```

**Expected:**

```json
{
  "items": [3, 4],
  "page": 2,
  "size": 2,
  "total": 5,
  "hasMore": true,
  "nextPage": 3
}
```

**Interview talking point:** `drop`/`take` **materialize** the array. For huge files, paginate at the **connector** (DB `LIMIT`, S3 list), not in DataWeave.

**Solution:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
var page = payload.page as Number
var size = payload.size as Number
var total = sizeOf(payload.items)
var window = payload.items drop ((page - 1) * size) take size
var hasMore = (page * size) < total
---
{
  items: window,
  page: page,
  size: size,
  total: total,
  hasMore: hasMore,
  nextPage: if (hasMore) page + 1 else null
}
```

---

### 62. Idempotency key from a natural key

**Problem:** Build `idempotencyKey` = `customerId` + `|` + `externalOrderId` + `|` + sorted unique line `sku`s joined by `,`. Production APIs send this as `Idempotency-Key` or store it for upserts.

**Input:**

```json
{
  "customerId": "C1",
  "externalOrderId": "EXT-9",
  "lines": [
    { "sku": "B" },
    { "sku": "A" },
    { "sku": "B" }
  ]
}
```

**Expected:** `"C1|EXT-9|A,B"`

**Interview talking point:** Keys must be **stable** if the client retries with the same business document (sort, distinct). Do not include `now()` or random UUIDs in the key.

**Solution:**

```dataweave
%dw 2.0
output application/json
var skus = (payload.lines.sku distinctBy $ orderBy $) joinBy ","
---
payload.customerId ++ "|" ++ payload.externalOrderId ++ "|" ++ skus
```

---

### 63. FIFO stock allocation across warehouses

**Problem:** Allocate `need` units from warehouses ordered by `priority` ascending. Each allocation `{ warehouseId, qty }`. `shortfall` is leftover demand.

**Input:**

```json
{
  "need": 7,
  "warehouses": [
    { "id": "W2", "qty": 10, "priority": 2 },
    { "id": "W1", "qty": 4, "priority": 1 }
  ]
}
```

**Expected:**

```json
{
  "allocations": [
    { "warehouseId": "W1", "qty": 4 },
    { "warehouseId": "W2", "qty": 3 }
  ],
  "shortfall": 0
}
```

**Interview talking point:** This is a **running remainder** (`reduce`). Inventory writes still happen in the backend; DataWeave only shapes the allocation plan.

**Solution:**

```dataweave
%dw 2.0
output application/json
var ordered = payload.warehouses orderBy ((w) -> w.priority)
var plan = ordered reduce ((w, acc = { left: payload.need as Number, rows: [] }) -> do {
  var take = if (acc.left < w.qty) acc.left else w.qty
  var row = if (take > 0) [{ warehouseId: w.id, qty: take }] else []
  ---
  { left: acc.left - take, rows: acc.rows ++ row }
})
---
{
  allocations: plan.rows,
  shortfall: plan.left
}
```

---

### 64. Nested GraphQL-style order to line rows

**Problem:** Flatten `order.lines` into reporting rows: `orderId`, `customer`, `sku`, `qty`. Drop lines with `qty <= 0`.

**Input:**

```json
{
  "order": {
    "id": "O-1",
    "customer": "Asha",
    "lines": [
      { "sku": "A", "qty": 2 },
      { "sku": "B", "qty": 0 },
      { "sku": "C", "qty": 5 }
    ]
  }
}
```

**Expected:**

```json
[
  { "orderId": "O-1", "customer": "Asha", "sku": "A", "qty": 2 },
  { "orderId": "O-1", "customer": "Asha", "sku": "C", "qty": 5 }
]
```

**Interview talking point:** Same pattern as exploding SOAP/XML line items: **`flatMap` / `map` + filter**. Analytics feeds want a **grain** (one row = one line), not nested documents.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.order.lines
  filter ((l) -> (l.qty as Number) > 0)
  map (l) -> {
    orderId: payload.order.id,
    customer: payload.order.customer,
    sku: l.sku,
    qty: l.qty as Number
  }
```

---

### 65. Wrap a domain payload as CloudEvents 1.0

**Problem:** Produce a CloudEvents-like envelope. Use `payload.now` (injected; never `now()` in tests). `id` = `eventId`. `data` is the domain object without envelope fields.

**Input:**

```json
{
  "eventId": "e-100",
  "now": "2026-08-20T08:00:00Z",
  "source": "urn:mule:orders",
  "type": "com.acme.order.created",
  "orderId": "O-1",
  "amount": 99
}
```

**Expected:**

```json
{
  "specversion": "1.0",
  "id": "e-100",
  "source": "urn:mule:orders",
  "type": "com.acme.order.created",
  "time": "2026-08-20T08:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "orderId": "O-1",
    "amount": 99
  }
}
```

**Interview talking point:** Inject clocks and UUIDs as **parameters** so modules stay testable. Kafka/Anypoint MQ headers often duplicate `id` / `type`.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  specversion: "1.0",
  id: payload.eventId,
  source: payload.source,
  type: payload.type,
  time: payload.now,
  datacontenttype: "application/json",
  data: payload - "eventId" - "now" - "source" - "type"
}
```

---

### 66. Tenant config overlay (defaults < tenant < request)

**Problem:** Deep-merge objects with precedence **request > tenant > defaults**. For `featureFlags` (array of strings), **replace** the whole array from the highest source that provided it (do not concatenate). Scalars: first non-null from request, then tenant, then defaults.

**Input:**

```json
{
  "defaults": {
    "timeoutMs": 3000,
    "region": "us",
    "featureFlags": ["a"],
    "retry": { "max": 2, "backoffMs": 100 }
  },
  "tenant": {
    "region": "in",
    "featureFlags": ["b", "c"],
    "retry": { "max": 4 }
  },
  "request": {
    "timeoutMs": 9000,
    "retry": { "backoffMs": 250 }
  }
}
```

**Expected:**

```json
{
  "timeoutMs": 9000,
  "region": "in",
  "featureFlags": ["b", "c"],
  "retry": { "max": 4, "backoffMs": 250 }
}
```

**Interview talking point:** Config overlays need a **documented merge algebra**. Blind `++` is shallow; array concat silently duplicates flags.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun overlay(a, b) =
  (a match {
    case ao is Object if b is Object ->
      ((namesOf(ao) ++ namesOf(b)) distinctBy $)
        reduce ((k, acc = {}) -> acc ++ { (k): overlay(ao[k], b[k]) })
    else -> b default a
  })
var mid = overlay(payload.defaults, payload.tenant)
var merged = overlay(mid, payload.request)
---
merged update {
  case .featureFlags -> (
    payload.request.featureFlags default
      (payload.tenant.featureFlags default payload.defaults.featureFlags)
  )
}
```

---

### 67. Windowed totals by account and business date

**Problem:** Group payments by `accountId` and calendar date of `ts` (`yyyy-MM-dd` prefix). Sum `amount`. Sort output by account then date.

**Input:**

```json
{
  "payments": [
    { "accountId": "A1", "ts": "2026-08-20T10:00:00Z", "amount": 10 },
    { "accountId": "A1", "ts": "2026-08-20T18:00:00Z", "amount": 5 },
    { "accountId": "A2", "ts": "2026-08-21T01:00:00Z", "amount": 7 },
    { "accountId": "A1", "ts": "2026-08-21T00:00:00Z", "amount": 1 }
  ]
}
```

**Expected:**

```json
[
  { "accountId": "A1", "date": "2026-08-20", "total": 15 },
  { "accountId": "A1", "date": "2026-08-21", "total": 1 },
  { "accountId": "A2", "date": "2026-08-21", "total": 7 }
]
```

**Interview talking point:** “Business date” is a **timezone policy**, not `now()`. Here we take the UTC date prefix; production often converts to a store timezone first (see Lab 72).

**Solution:**

```dataweave
%dw 2.0
output application/json
fun day(ts) = (ts as String)[0 to 9]
---
payload.payments
  groupBy ((p) -> p.accountId ++ "|" ++ day(p.ts))
  pluck ((rows, k) -> {
    accountId: (k splitBy "|")[0],
    date: (k splitBy "|")[1],
    total: sum(rows.amount)
  })
  orderBy ((r) -> r.accountId ++ r.date)
```

---

### 68. SOAP-like envelope: success vs fault

**Problem:** If `Envelope.Body.Fault` exists, return `{ ok: false, code, message }`. Else unwrap `Envelope.Body` as `{ ok: true, data }` (the body without `Fault`).

**Input:**

```json
{
  "Envelope": {
    "Body": {
      "Fault": {
        "faultcode": "soap:Server",
        "faultstring": "credit check failed"
      }
    }
  }
}
```

**Expected:**

```json
{
  "ok": false,
  "code": "soap:Server",
  "message": "credit check failed"
}
```

**Interview talking point:** Always branch on **fault vs body** before mapping the happy path. In Mule, that often becomes a Choice router after a small DW expression — keep the script obvious.

**Solution:**

```dataweave
%dw 2.0
output application/json
var body = payload.Envelope.Body
var fault = body.Fault
---
if (fault != null)
  { ok: false, code: fault.faultcode, message: fault.faultstring }
else
  { ok: true, data: body - "Fault" }
```

---

### 69. Product variants cartesian-joined to a price book

**Problem:** For each **active** product, cartesian `colors` × `sizes`. Join `prices` by `sku` where `sku` = `productId + "-" + color + "-" + size`. Skip combos with no price.

**Input:**

```json
{
  "products": [
    {
      "id": "TEE",
      "active": true,
      "colors": ["R", "G"],
      "sizes": ["S", "M"]
    },
    {
      "id": "HAT",
      "active": false,
      "colors": ["B"],
      "sizes": ["L"]
    }
  ],
  "prices": [
    { "sku": "TEE-R-S", "price": 10 },
    { "sku": "TEE-R-M", "price": 12 },
    { "sku": "TEE-G-S", "price": 11 }
  ]
}
```

**Expected:**

```json
[
  { "sku": "TEE-R-S", "productId": "TEE", "color": "R", "size": "S", "price": 10 },
  { "sku": "TEE-R-M", "productId": "TEE", "color": "R", "size": "M", "price": 12 },
  { "sku": "TEE-G-S", "productId": "TEE", "color": "G", "size": "S", "price": 11 }
]
```

**Interview talking point:** Cartesian product is `flatMap` + `map`. Index prices with `groupBy` **once**. Inactive products must not leak SKUs.

**Solution:**

```dataweave
%dw 2.0
output application/json
var priceBySku = payload.prices groupBy ((p) -> p.sku)
---
payload.products
  filter ((p) -> p.active)
  flatMap ((p) ->
    p.colors flatMap ((c) ->
      p.sizes map (s) -> do {
        var sku = p.id ++ "-" ++ c ++ "-" ++ s
        var price = priceBySku[sku][0].price
        ---
        if (price == null) null
        else { sku: sku, productId: p.id, color: c, size: s, price: price }
      }
    )
  )
  filter $ != null
```

---

### 70. JSON Merge Patch (RFC 7396) plus changelog

**Problem:** Apply `patch` to `base`. `null` in patch **deletes** the key. Nested objects merge recursively; non-objects replace. Also return `changed` as sorted field paths that differ (`from` / `to`). Treat missing as `null`.

**Input:**

```json
{
  "base": { "name": "Asha", "age": 30, "addr": { "city": "Pune", "zip": "411" } },
  "patch": { "age": null, "addr": { "city": "Mumbai" }, "role": "eng" }
}
```

**Expected:**

```json
{
  "result": {
    "name": "Asha",
    "addr": { "city": "Mumbai", "zip": "411" },
    "role": "eng"
  },
  "changed": [
    { "path": "addr.city", "from": "Pune", "to": "Mumbai" },
    { "path": "age", "from": 30, "to": null },
    { "path": "role", "from": null, "to": "eng" }
  ]
}
```

**Interview talking point:** HTTP PATCH in APIs is often **merge-patch**, not a full PUT. Audit/changelog is a second walk (`diff`). `skipNullOn` would hide deletions — do not use it on the changelog.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun applyPatch(base, patch) =
  if (patch == null) null
  else if ((patch is Object) and (base is Object)) do {
    var keys = (namesOf(base) ++ namesOf(patch)) distinctBy $
    ---
    keys reduce ((k, acc = {}) ->
      if (namesOf(patch) contains k)
        (if (patch[k] == null) acc else acc ++ { (k): applyPatch(base[k], patch[k]) })
      else acc ++ { (k): base[k] }
    )
  }
  else patch
fun diffs(a, b, path) =
  if (a == b) []
  else if ((a is Object) and (b is Object)) do {
    var keys = (namesOf(a) ++ namesOf(b)) distinctBy $
    ---
    keys flatMap ((k) -> diffs(a[k], b[k], if (path == "") (k as String) else path ++ "." ++ (k as String)))
  }
  else [{ path: path, from: a default null, to: b default null }]
var result = applyPatch(payload.base, payload.patch)
---
{
  result: result,
  changed: diffs(payload.base, result, "") orderBy $.path
}
```

---

### 71. Batch API chunks with per-batch checksum

**Problem:** Split `records` into batches of `size`. Each batch: `batchId` (`B1`, `B2`, …), `count`, `ids`, `checksum` = sum of numeric `id`s.

**Input:**

```json
{
  "size": 2,
  "records": [
    { "id": 1 },
    { "id": 2 },
    { "id": 3 },
    { "id": 4 },
    { "id": 5 }
  ]
}
```

**Expected:**

```json
[
  { "batchId": "B1", "count": 2, "ids": [1, 2], "checksum": 3 },
  { "batchId": "B2", "count": 2, "ids": [3, 4], "checksum": 7 },
  { "batchId": "B3", "count": 1, "ids": [5], "checksum": 5 }
]
```

**Interview talking point:** Bulk HTTP/SFTP jobs need **stable batch ids** and a control total. `divideBy` is the Array helper; it materializes the list (streaming tradeoff).

**Solution:**

```dataweave
%dw 2.0
import divideBy from dw::core::Arrays
output application/json
---
(payload.records divideBy payload.size) map (chunk, idx) -> {
  batchId: "B" ++ (idx + 1),
  count: sizeOf(chunk),
  ids: chunk.id,
  checksum: sum(chunk.id)
}
```

---

### 72. Store-local business date from UTC plus offset hours

**Problem:** Convert each UTC timestamp to a **business date** using a fixed offset (`offsetHours`, e.g. IST = 5.5 → use `5` here for integer hours, or pass `offsetHours`: 5). Add `offsetHours * 3600` seconds, then take `yyyy-MM-dd`. Do not call `now()`.

**Input:**

```json
{
  "offsetHours": 5,
  "events": [
    { "id": "1", "utc": "2026-08-20T20:00:00Z" },
    { "id": "2", "utc": "2026-08-20T18:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "id": "1", "utc": "2026-08-20T20:00:00Z", "businessDate": "2026-08-21" },
  { "id": "2", "utc": "2026-08-20T18:00:00Z", "businessDate": "2026-08-20" }
]
```

**Interview talking point:** Offsets are a teaching stand-in. Production uses IANA zones and DST (`dw::core::Dates` / Java time). Never mix store-local “business date” with UTC `createdAt` without a written rule.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun businessDate(utc, offsetHours) = do {
  var dt = utc as DateTime
  var period = ("PT" ++ (offsetHours as String) ++ "H") as Period
  ---
  (dt + period) as String {format: "yyyy-MM-dd"}
}
---
payload.events map {
  id: $.id,
  utc: $.utc,
  businessDate: businessDate($.utc, payload.offsetHours)
}
```

---

### 73. Recursive BOM explode with cycle guard

**Problem:** Explode `parentSku` through `components` to a tree. If a sku is already on the path, emit `{ sku, cycle: true, children: [] }` and stop that branch. Unknown sku: `{ sku, missing: true, children: [] }`.

**Input:**

```json
{
  "catalog": [
    { "sku": "P", "name": "Pump", "components": ["G", "S"] },
    { "sku": "G", "name": "Gasket", "components": ["S"] },
    { "sku": "S", "name": "Screw", "components": ["P"] }
  ],
  "parentSku": "P"
}
```

**Expected (shape):** Pump → Gasket → Screw → **cycle back to P**; Pump → Screw → cycle to P.

**Interview talking point:** Multi-level BOM **must** carry a visited path. Production graphs (items, parties, categories) are not trees.

**Solution:**

```dataweave
%dw 2.0
output application/json
var bySku = payload.catalog groupBy ((c) -> c.sku)
fun explode(sku, visited) =
  if (visited contains sku)
    { sku: sku, cycle: true, missing: false, name: null, children: [] }
  else do {
    var c = (bySku[sku] default [])[0]
    ---
    if (c == null)
      { sku: sku, cycle: false, missing: true, name: null, children: [] }
    else {
      sku: sku,
      name: c.name,
      cycle: false,
      missing: false,
      children: (c.components default []) map explode($, visited ++ [sku])
    }
  }
---
explode(payload.parentSku, [])
```

---

### 74. Flatten nested JSON to dotted paths

**Problem:** Produce a flat object for analytics/CSV. Object keys join with `.`. Arrays use numeric indexes. Leaf values stay as-is.

**Input:**

```json
{
  "orderId": "O-1",
  "customer": { "name": "Asha", "addr": { "city": "Pune" } },
  "lines": [
    { "sku": "A", "qty": 2 },
    { "sku": "B", "qty": 1 }
  ]
}
```

**Expected:**

```json
{
  "orderId": "O-1",
  "customer.name": "Asha",
  "customer.addr.city": "Pune",
  "lines.0.sku": "A",
  "lines.0.qty": 2,
  "lines.1.sku": "B",
  "lines.1.qty": 1
}
```

**Interview talking point:** Dotted flatten is how many data lakes ingest API JSON. Watch streaming: this **walks the whole tree**.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun joinPath(prefix, key) =
  if (prefix == "") key else prefix ++ "." ++ key
fun flatten(x, prefix) =
  x match {
    case o is Object ->
      o pluck ((v, k) -> flatten(v, joinPath(prefix, k as String)))
        reduce ((part, acc = {}) -> acc ++ part)
    case a is Array ->
      a map ((item, idx) -> flatten(item, joinPath(prefix, idx as String)))
        reduce ((part, acc = {}) -> acc ++ part)
    else -> { (prefix): x }
  }
---
flatten(payload, "")
```

---

### 75. Scatter-gather: merge three connector responses

**Problem:** `responses` is what a Scatter-Gather (or parallel HTTP) returns. Status `200–299` → put `body` under `ok[name]`. Anything else → `errors[]`. Do not drop successes because one leg failed.

**Input:**

```json
{
  "responses": [
    { "name": "crm", "status": 200, "body": { "id": "C1" } },
    { "name": "erp", "status": 500, "body": { "error": "down" } },
    { "name": "mdm", "status": 200, "body": { "id": "M1" } }
  ]
}
```

**Expected:**

```json
{
  "ok": {
    "crm": { "id": "C1" },
    "mdm": { "id": "M1" }
  },
  "errors": [
    { "name": "erp", "status": 500, "body": { "error": "down" } }
  ]
}
```

**Interview talking point:** HTTP 207 / partial aggregation is the integration default. Map **per leg**, then decide in Choice whether the flow can continue.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun okStatus(n) = (n as Number) >= 200 and (n as Number) < 300
var good = payload.responses filter ((r) -> okStatus(r.status))
var bad = payload.responses filter ((r) -> !okStatus(r.status))
---
{
  ok: good reduce ((r, acc = {}) -> acc ++ { (r.name): r.body }),
  errors: bad map { name: $.name, status: $.status, body: $.body }
}
```

---

### 76. Salesforce-style composite upsert records

**Problem:** Map canonical accounts to a Composite-like body: `allOrNone: false`, each record has `attributes.type = "Account"`, `Name`, and `ExternalId__c` from `sourceId`. Skip rows with empty `name`.

**Input:**

```json
{
  "accounts": [
    { "sourceId": "E-1", "name": "Acme" },
    { "sourceId": "E-2", "name": "" },
    { "sourceId": "E-3", "name": "Globex" }
  ]
}
```

**Expected:**

```json
{
  "allOrNone": false,
  "records": [
    { "attributes": { "type": "Account" }, "Name": "Acme", "ExternalId__c": "E-1" },
    { "attributes": { "type": "Account" }, "Name": "Globex", "ExternalId__c": "E-3" }
  ]
}
```

**Interview talking point:** `allOrNone: false` is partial success at the SaaS API. Pair with Lab 55-style `errors[]` on the way back.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  allOrNone: false,
  records: payload.accounts
    filter ((a) -> !isEmpty(a.name default ""))
    map (a) -> {
      attributes: { "type": "Account" },
      Name: a.name,
      "ExternalId__c": a.sourceId
    }
}
```

---

### 77. Keep latest version per id (upsert projection)

**Problem:** Event log of `{ id, version, payload }`. Keep the row with the **highest** `version` per `id`. If versions tie, keep the last in array order.

**Input:**

```json
[
  { "id": "A", "version": 1, "payload": { "name": "old" } },
  { "id": "B", "version": 1, "payload": { "name": "b" } },
  { "id": "A", "version": 3, "payload": { "name": "new" } },
  { "id": "A", "version": 2, "payload": { "name": "mid" } }
]
```

**Expected:**

```json
[
  { "id": "A", "version": 3, "payload": { "name": "new" } },
  { "id": "B", "version": 1, "payload": { "name": "b" } }
]
```

**Interview talking point:** This is an **in-memory projection**. True source of truth is the event store; DataWeave only shapes the current snapshot for a target API.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
valuesOf(
  payload reduce ((e, acc = {}) -> do {
    var cur = acc[e.id]
    ---
    if (cur == null or (e.version as Number) >= (cur.version as Number))
      acc ++ { (e.id): e }
    else acc
  })
)
```

---

### 78. Catalog copy with locale fallback

**Problem:** Resolve `hi` and `bye` for `locale`, then `fallback`. Missing key → `null` (do not fail).

**Input:**

```json
{
  "locale": "de",
  "fallback": "en",
  "copy": {
    "en": { "hi": "Hello", "bye": "Bye" },
    "fr": { "hi": "Bonjour" }
  }
}
```

**Expected:**

```json
{
  "locale": "de",
  "hi": "Hello",
  "bye": "Bye"
}
```

**Interview talking point:** Storefront and notification templates always need **fallback chains**. Same pattern as MDM field precedence (Lab 56).

**Solution:**

```dataweave
%dw 2.0
output application/json
fun label(key) =
  payload.copy[payload.locale][key] default payload.copy[payload.fallback][key] default null
---
{
  locale: payload.locale,
  hi: label("hi"),
  bye: label("bye")
}
```

---

### 79. Log-safe HTTP headers (redact secrets)

**Problem:** Copy headers for logging. Keys `authorization`, `cookie`, `x-api-key` (any case) become `"****"`. Keep `x-correlation-id` as-is.

**Input:**

```json
{
  "headers": {
    "Authorization": "Bearer secret",
    "X-Correlation-Id": "corr-9",
    "Cookie": "sid=abc",
    "Accept": "application/json"
  }
}
```

**Expected:**

```json
{
  "Authorization": "****",
  "X-Correlation-Id": "corr-9",
  "Cookie": "****",
  "Accept": "application/json"
}
```

**Interview talking point:** Never log inbound HTTP before this map. Pair with Lab 39 (body PII). Correlation id is the one header you **must** keep.

**Solution:**

```dataweave
%dw 2.0
output application/json
var secret = ["authorization", "cookie", "x-api-key"]
---
payload.headers mapObject ((v, k) -> {
  (k): if (secret contains lower(k as String)) "****" else v
})
```

---

### 80. SLA overdue flags (injected clock)

**Problem:** For each open ticket, if `dueAt` < `now` then `OVERDUE`, else `ON_TRACK`. Closed tickets stay `CLOSED`. Use `payload.now` (do not call `now()`).

**Input:**

```json
{
  "now": "2026-08-20T12:00:00Z",
  "tickets": [
    { "id": "T1", "status": "OPEN", "dueAt": "2026-08-20T11:00:00Z" },
    { "id": "T2", "status": "OPEN", "dueAt": "2026-08-20T13:00:00Z" },
    { "id": "T3", "status": "CLOSED", "dueAt": "2026-08-19T00:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "id": "T1", "sla": "OVERDUE" },
  { "id": "T2", "sla": "ON_TRACK" },
  { "id": "T3", "sla": "CLOSED" }
]
```

**Interview talking point:** Clocks are **inputs** so MUnit stays deterministic. Compare `DateTime`, not strings, if formats vary.

**Solution:**

```dataweave
%dw 2.0
output application/json
var clock = payload.now as DateTime
---
payload.tickets map (t) -> {
  id: t.id,
  sla: t.status match {
    case "CLOSED" -> "CLOSED"
    else ->
      if ((t.dueAt as DateTime) < clock) "OVERDUE" else "ON_TRACK"
  }
}
```

---

### 81. Dead-letter / replay envelope

**Problem:** Wrap a failed record for a DLQ or object store: `replayKey` (stable), `failedAt` from injected `now`, `errorType`, and `original` (the record only).

**Input:**

```json
{
  "now": "2026-08-20T08:00:00Z",
  "errorType": "HTTP:CONNECTIVITY",
  "record": { "orderId": "O-1", "customerId": "C1" }
}
```

**Expected:**

```json
{
  "replayKey": "C1|O-1",
  "failedAt": "2026-08-20T08:00:00Z",
  "errorType": "HTTP:CONNECTIVITY",
  "original": { "orderId": "O-1", "customerId": "C1" }
}
```

**Interview talking point:** Replay keys must match Lab 62 (idempotency). Store the **canonical** original, not the raw connector error HTML.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  replayKey: payload.record.customerId ++ "|" ++ payload.record.orderId,
  failedAt: payload.now,
  errorType: payload.errorType,
  original: payload.record
}
```

---

### 82. Heterogeneous payments to a canonical charge

**Problem:** `method` is `card`, `upi`, or `netbanking`. Map to `{ method, instrument, ref }`. Unknown method → `{ method: "other", instrument: null, ref: null }` (do not fail the batch).

**Input:**

```json
{
  "payments": [
    { "method": "card", "last4": "4242", "authCode": "A1" },
    { "method": "upi", "vpa": "asha@upi", "txnId": "U9" },
    { "method": "netbanking", "bank": "HDFC", "refNo": "N3" },
    { "method": "wallet", "id": "w1" }
  ]
}
```

**Expected:**

```json
[
  { "method": "card", "instrument": "4242", "ref": "A1" },
  { "method": "upi", "instrument": "asha@upi", "ref": "U9" },
  { "method": "netbanking", "instrument": "HDFC", "ref": "N3" },
  { "method": "other", "instrument": null, "ref": null }
]
```

**Interview talking point:** PSP webhooks are **union types**. `match` on `method` (or `type`) is the production pattern — not a pile of `if` with missing `else`.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun charge(p) =
  p.method match {
    case "card" -> { method: "card", instrument: p.last4, ref: p.authCode }
    case "upi" -> { method: "upi", instrument: p.vpa, ref: p.txnId }
    case "netbanking" -> { method: "netbanking", instrument: p.bank, ref: p.refNo }
    else -> { method: "other", instrument: null, ref: null }
  }
---
payload.payments map charge($)
```

---

## How to practice (production)

1. Write the **rules** in comments (`var` names: `good`, `errors`, `byId`) before the mapping.
2. Fail closed: missing FX, bad qty, trailer mismatch → explicit fields, not silent `default 0` unless the business says so.
3. Index the right-hand side once (`groupBy`). Never `lookup` inside `map`.
4. Inject time and ids (`payload.now`, `eventId`) for deterministic tests.

## Production whiteboard set (pick 4)

| # | Problem | Tests |
| --- | --- | --- |
| 55 | Canonical order + `errors[]` | partial success |
| 56 | Customer 360 | precedence + nulls |
| 63 | FIFO allocate | running remainder |
| 70 | Merge patch + diff | nested delete |
| 73 | Recursive BOM | cycle guard |
| 75 | Scatter-gather merge | partial HTTP |
| 82 | Payment union types | `match` else |

---

*DataWeave 2.x / Mule 4.3+ recommended (`update`, `divideBy`, `drop` / `take`).*
