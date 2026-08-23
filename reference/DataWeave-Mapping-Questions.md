# DataWeave Mapping — 30 complex industry sets

Interview-hard **end-to-end mappings** (labs **59–88**). Each payload is a realistic integration shape:
Salesforce composite, SAP/GST, Shopify, Stripe, ServiceNow, CDC, SOAP, FX, inventory, claims.
Playground-friendly: lookup tables sit **on the payload** (no required Mule `vars`).

Try the script before opening `instructor/solutions`.

---

## Complex industry mappings (59–88)

### 59. Salesforce Account composite to nested customer API

**Problem:** Join `contacts` onto `accounts` by AccountId. Output `accountId`, `name`, `city`, and `contacts[]` with `fullName` and `email`. Empty contact list if none. Do not call lookup.

**Input:**

```json
{
  "accounts": [
    { "Id": "001xxA", "Name": "Acme Pvt", "BillingCity": "Pune" },
    { "Id": "001xxB", "Name": "Globex", "BillingCity": "Mumbai" }
  ],
  "contacts": [
    { "AccountId": "001xxA", "FirstName": "Asha", "LastName": "Rao", "Email": "asha@acme.com" },
    { "AccountId": "001xxA", "FirstName": "Ben", "LastName": "Cole", "Email": "ben@acme.com" }
  ]
}
```

**Expected:**

```json
[
  {
    "accountId": "001xxA",
    "name": "Acme Pvt",
    "city": "Pune",
    "contacts": [
      { "fullName": "Asha Rao", "email": "asha@acme.com" },
      { "fullName": "Ben Cole", "email": "ben@acme.com" }
    ]
  },
  {
    "accountId": "001xxB",
    "name": "Globex",
    "city": "Mumbai",
    "contacts": []
  }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var byAcct = payload.contacts groupBy $.AccountId
---
payload.accounts map (a) -> {
  accountId: a.Id,
  name: a.Name,
  city: a.BillingCity,
  contacts: (byAcct[a.Id] default []) map {
    fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
    email: $.Email
  }
}
```

---

### 60. SAP-style order JSON to canonical invoice with GST

**Problem:** Skip lines with qty 0. `fun money`. Line net = qty * price * (1 - discount). CGST+SGST vs IGST 18% by comparing ship-from and ship-to state. Grand total = subtotal + tax.

**Input:**

```json
{
  "vbeln": "80001234",
  "waerk": "INR",
  "shipFromState": "MH",
  "shipToState": "MH",
  "lines": [
    { "matnr": "MAT-1", "qty": "2", "netpr": "100.00", "disc": "0.10" },
    { "matnr": "MAT-2", "qty": "0", "netpr": "50", "disc": "0" },
    { "matnr": "MAT-3", "qty": 1, "netpr": "40.5", "disc": 0 }
  ]
}
```

**Expected:**

```json
{
  "invoiceId": "80001234",
  "currency": "INR",
  "taxCode": "CGST_SGST",
  "lines": [
    { "sku": "MAT-1", "qty": 2, "net": 180.00 },
    { "sku": "MAT-3", "qty": 1, "net": 40.50 }
  ],
  "subtotal": 220.50,
  "tax": 39.69,
  "grandTotal": 260.19
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var intra = payload.shipFromState == payload.shipToState
var raw = payload.lines filter ((l) -> (l.qty as Number) > 0) map (l) -> do {
  var qty = l.qty as Number
  var price = l.netpr as Number
  var disc = (l.disc default 0) as Number
  ---
  { sku: l.matnr, qty: qty, net: money(qty * price * (1 - disc)) }
}
var sub = money(sum(raw.net))
var tax = money(sub * 0.18)
---
{
  invoiceId: payload.vbeln,
  currency: payload.waerk,
  taxCode: if (intra) "CGST_SGST" else "IGST",
  lines: raw,
  subtotal: sub,
  tax: tax,
  grandTotal: money(sub + tax)
}
```

---

### 61. Workday workers to HR API (active only)

**Problem:** Keep Active workers (any case). `fullName` from legal names. `managerId` from `manager.wid` (null-safe). Coerce `fte`.

**Input:**

```json
{
  "Report_Entry": [
    { "wid": "W1", "Legal_First": "Ira", "Legal_Last": "Shah", "Status": "Active", "FTE": "1.0", "manager": { "wid": "W9" } },
    { "wid": "W2", "Legal_First": "Jon", "Legal_Last": "Lee", "Status": "Terminated", "FTE": "1", "manager": {} },
    { "wid": "W3", "Legal_First": "Mia", "Legal_Last": "Das", "Status": "active", "FTE": 0.5 }
  ]
}
```

**Expected:**

```json
[
  { "id": "W1", "fullName": "Ira Shah", "fte": 1.0, "managerId": "W9" },
  { "id": "W3", "fullName": "Mia Das", "fte": 0.5, "managerId": null }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.Report_Entry
  filter ((w) -> lower(w.Status) == "active")
  map {
    id: $.wid,
    fullName: ($.Legal_First default "") ++ " " ++ ($.Legal_Last default ""),
    fte: $.FTE as Number,
    managerId: $.manager.wid default null
  }
```

---

### 62. Shopify order to ERP sales order

**Problem:** Map line_items; skip SKU GIFT. Money strings. soldTo = last then first. channel WEB.

**Input:**

```json
{
  "id": 991,
  "currency": "USD",
  "shipping_address": { "first_name": "Sam", "last_name": "Patel" },
  "line_items": [
    { "sku": "TEE-M", "quantity": 2, "price": "19.99" },
    { "sku": "GIFT", "quantity": 1, "price": "25.00" },
    { "sku": "HAT", "quantity": 1, "price": "12.5" }
  ]
}
```

**Expected:**

```json
{
  "erpOrderId": "991",
  "currency": "USD",
  "channel": "WEB",
  "soldTo": "Patel Sam",
  "lines": [
    { "sku": "TEE-M", "qty": 2, "unitPrice": 19.99 },
    { "sku": "HAT", "qty": 1, "unitPrice": 12.50 }
  ]
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  erpOrderId: payload.id as String,
  currency: payload.currency,
  channel: "WEB",
  soldTo: (payload.shipping_address.last_name default "") ++ " " ++ (payload.shipping_address.first_name default ""),
  lines: payload.line_items
    filter ((l) -> l.sku != "GIFT")
    map { sku: $.sku, qty: $.quantity as Number, unitPrice: money($.price as Number) }
}
```

---

### 63. Stripe charges enriched with customer

**Problem:** Join charges to customers. Amount cents/100. Missing email unknown.

**Input:**

```json
{
  "customers": [
    { "id": "cus_1", "email": "a@x.com" }
  ],
  "charges": {
    "data": [
      { "id": "ch_1", "customer": "cus_1", "amount": 1999, "paid": true },
      { "id": "ch_2", "customer": "cus_missing", "amount": 500, "paid": false }
    ]
  }
}
```

**Expected:**

```json
[
  { "chargeId": "ch_1", "email": "a@x.com", "amount": 19.99, "paid": true },
  { "chargeId": "ch_2", "email": "unknown", "amount": 5.00, "paid": false }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var byId = payload.customers groupBy $.id
---
payload.charges.data map (c) -> {
  chargeId: c.id,
  email: (byId[c.customer][0].email) default "unknown",
  amount: money((c.amount as Number) / 100),
  paid: c.paid
}
```

---

### 64. ServiceNow incident plus CMDB lookup

**Problem:** ciName from cmdb; missing UNASSIGNED. Priority 1-2 stay, else sev 3.

**Input:**

```json
{
  "cmdb": [
    { "sys_id": "ci1", "name": "sap-prd-db" }
  ],
  "incidents": [
    { "number": "INC001", "cmdb_ci": "ci1", "priority": "1", "opened_at": "2026-08-01T04:00:00Z" },
    { "number": "INC002", "cmdb_ci": "gone", "priority": "3", "opened_at": "2026-08-02T10:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "ticket": "INC001", "ciName": "sap-prd-db", "sev": 1, "openedAt": "2026-08-01T04:00:00Z" },
  { "ticket": "INC002", "ciName": "UNASSIGNED", "sev": 3, "openedAt": "2026-08-02T10:00:00Z" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var cis = payload.cmdb groupBy $.sys_id
fun sev(p) = if ((p as Number) <= 2) (p as Number) else 3
---
payload.incidents map {
  ticket: $.number,
  ciName: (cis[$.cmdb_ci][0].name) default "UNASSIGNED",
  sev: sev($.priority),
  openedAt: $.opened_at
}
```

---

### 65. Debezium CDC envelope to flat upsert rows

**Problem:** c/u → UPSERT from after; d → DELETE from before. Include tsMs.

**Input:**

```json
{
  "changes": [
    { "op": "c", "ts_ms": 100, "before": null, "after": { "id": "A1", "status": "NEW" } },
    { "op": "u", "ts_ms": 101, "before": { "id": "A1", "status": "NEW" }, "after": { "id": "A1", "status": "PAID" } },
    { "op": "d", "ts_ms": 102, "before": { "id": "B9", "status": "X" }, "after": null }
  ]
}
```

**Expected:**

```json
[
  { "action": "UPSERT", "id": "A1", "status": "NEW", "tsMs": 100 },
  { "action": "UPSERT", "id": "A1", "status": "PAID", "tsMs": 101 },
  { "action": "DELETE", "id": "B9", "status": "X", "tsMs": 102 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.changes map (c) -> do {
  var row = if (c.op == "d") c.before else c.after
  ---
  {
    action: if (c.op == "d") "DELETE" else "UPSERT",
    id: row.id,
    status: row.status,
    tsMs: c.ts_ms
  }
}
```

---

### 66. Product variants color times size SKUs

**Problem:** Cartesian colors x sizes. Skip discontinued colors. SKU base-color-size.

**Input:**

```json
{
  "base": "TEE",
  "colors": [
    { "code": "BLK", "discontinued": false },
    { "code": "RED", "discontinued": true },
    { "code": "WHT", "discontinued": false }
  ],
  "sizes": ["S", "M"]
}
```

**Expected:**

```json
[
  { "sku": "TEE-BLK-S" },
  { "sku": "TEE-BLK-M" },
  { "sku": "TEE-WHT-S" },
  { "sku": "TEE-WHT-M" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.colors
  filter ((c) -> c.discontinued == false)
  flatMap ((c) ->
    payload.sizes map (sz) -> {
      sku: payload.base ++ "-" ++ c.code ++ "-" ++ sz
    }
  )
```

---

### 67. Multi-currency lines to USD using FX table

**Problem:** usd = amount / perUsd. Skip unknown currency. fun money.

**Input:**

```json
{
  "fx": [
    { "ccy": "USD", "perUsd": 1 },
    { "ccy": "INR", "perUsd": 83 },
    { "ccy": "EUR", "perUsd": 0.92 }
  ],
  "lines": [
    { "id": "L1", "amount": "8300", "currency": "INR" },
    { "id": "L2", "amount": "10", "currency": "USD" },
    { "id": "L3", "amount": "9.2", "currency": "EUR" },
    { "id": "L4", "amount": "1", "currency": "JPY" }
  ]
}
```

**Expected:**

```json
{
  "lines": [
    { "id": "L1", "usd": 100.00 },
    { "id": "L2", "usd": 10.00 },
    { "id": "L3", "usd": 10.00 }
  ],
  "totalUsd": 120.00
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var rates = payload.fx groupBy $.ccy
var converted = payload.lines
  filter ((l) -> rates[l.currency] != null)
  map (l) -> {
    id: l.id,
    usd: money((l.amount as Number) / (rates[l.currency][0].perUsd as Number))
  }
---
{
  lines: converted,
  totalUsd: money(sum(converted.usd))
}
```

---

### 68. Normalize IN vs US postal addresses

**Problem:** IN: pin as postal. US: first 5 of zip. Uppercase city.

**Input:**

```json
[
  { "country": "IN", "addr1": "Lane 2", "city": "pune", "pin": "411001", "zip": null },
  { "country": "US", "addr1": "1 Main", "city": "austin", "pin": null, "zip": "78701-1234" }
]
```

**Expected:**

```json
[
  { "country": "IN", "line1": "Lane 2", "city": "PUNE", "postal": "411001" },
  { "country": "US", "line1": "1 Main", "city": "AUSTIN", "postal": "78701" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map (a) -> {
  country: a.country,
  line1: a.addr1,
  city: upper(a.city),
  postal: if (a.country == "IN") a.pin as String
          else (a.zip as String)[0 to 4]
}
```

---

### 69. EDI-like PO JSON to procurement canonical

**Problem:** Header po/vendor. Skip qty 0. needBy from yyyyMMdd to yyyy-MM-dd.

**Input:**

```json
{
  "BEG": { "po": "PO-77", "vendor": "V-9" },
  "PO1": [
    { "sku": "BOLT", "qty": "10", "aaa": "20260820" },
    { "sku": "NUT", "qty": "0", "aaa": "20260821" }
  ]
}
```

**Expected:**

```json
{
  "poNum": "PO-77",
  "vendor": "V-9",
  "lines": [
    { "sku": "BOLT", "qty": 10, "needBy": "2026-08-20" }
  ]
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  poNum: payload.BEG.po,
  vendor: payload.BEG.vendor,
  lines: payload.PO1
    filter ((l) -> (l.qty as Number) > 0)
    map {
      sku: $.sku,
      qty: $.qty as Number,
      needBy: ($.aaa as Date {format: "yyyyMMdd"}) as String {format: "yyyy-MM-dd"}
    }
}
```

---

### 70. Bank statement lines to signed running ledger

**Problem:** CR positive, DR negative. Running balance from 0. fun money.

**Input:**

```json
[
  { "nar": "SALARY", "dc": "CR", "amt": "1000.00" },
  { "nar": "UPI", "dc": "DR", "amt": "250.5" },
  { "nar": "REV", "dc": "CR", "amt": "50" }
]
```

**Expected:**

```json
[
  { "narration": "SALARY", "amount": 1000.00, "balance": 1000.00 },
  { "narration": "UPI", "amount": -250.50, "balance": 749.50 },
  { "narration": "REV", "amount": 50.00, "balance": 799.50 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload reduce ((row, acc = { bal: 0, out: [] }) -> do {
  var signed = if (row.dc == "DR") -(row.amt as Number) else (row.amt as Number)
  var next = acc.bal + signed
  ---
  {
    bal: next,
    out: acc.out ++ [{
      narration: row.nar,
      amount: money(signed),
      balance: money(next)
    }]
  }
}).out
```

---

### 71. IdP userinfo plus groups to application roles

**Problem:** Map groups to roles via table. Unique sorted roles. admin group → role ADMIN plus USER.

**Input:**

```json
{
  "roleMap": [
    { "group": "finance", "role": "FIN_READ" },
    { "group": "admin", "role": "ADMIN" },
    { "group": "admin", "role": "USER" }
  ],
  "user": { "sub": "u1", "email": "x@y.com", "groups": ["finance", "admin", "unknown"] }
}
```

**Expected:**

```json
{
  "userId": "u1",
  "email": "x@y.com",
  "roles": ["ADMIN", "FIN_READ", "USER"]
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var byG = payload.roleMap groupBy $.group
---
{
  userId: payload.user.sub,
  email: payload.user.email,
  roles: (
    payload.user.groups
      flatMap ((g) -> (byG[g] default []) map $.role)
      distinctBy $
      orderBy $
  )
}
```

---

### 72. Allocate warehouse stock to order lines FIFO

**Problem:** For each order line, allocated = min(qty, stock for sku). leftover stock is not required. Unmatched sku allocated 0.

**Input:**

```json
{
  "stock": [
    { "sku": "A", "onHand": 5 },
    { "sku": "B", "onHand": 1 }
  ],
  "order": [
    { "sku": "A", "qty": 3 },
    { "sku": "A", "qty": 4 },
    { "sku": "C", "qty": 2 }
  ]
}
```

**Expected:**

```json
[
  { "sku": "A", "requested": 3, "allocated": 3 },
  { "sku": "A", "requested": 4, "allocated": 2 },
  { "sku": "C", "requested": 2, "allocated": 0 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.order reduce ((line, acc = { stock: payload.stock groupBy $.sku, out: [] }) -> do {
  var have = (acc.stock[line.sku][0].onHand default 0) as Number
  var give = min([line.qty as Number, have])
  var rest = have - give
  ---
  {
    stock: acc.stock mapObject ((v, k) ->
      if ((k as String) == line.sku) { (k): [{ sku: line.sku, onHand: rest }] }
      else { (k): v }
    ),
    out: acc.out ++ [{ sku: line.sku, requested: line.qty as Number, allocated: give }]
  }
}).out
```

---

### 73. India GST split CGST SGST vs IGST by state

**Problem:** Same state: half of 18% each CGST and SGST. Different: full IGST 18%. fun money on taxable amount.

**Input:**

```json
{
  "fromState": "KA",
  "toState": "MH",
  "taxable": "1000.00"
}
```

**Expected:**

```json
{
  "taxable": 1000.00,
  "cgst": 0.00,
  "sgst": 0.00,
  "igst": 180.00
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var t = payload.taxable as Number
var intra = payload.fromState == payload.toState
---
{
  taxable: money(t),
  cgst: if (intra) money(t * 0.09) else 0.00,
  sgst: if (intra) money(t * 0.09) else 0.00,
  igst: if (intra) 0.00 else money(t * 0.18)
}
```

---

### 74. Loyalty points from paid orders

**Problem:** 1 point per whole INR of paid amount. status PAID/SETTLED any case. Sum points per customerId.

**Input:**

```json
[
  { "customerId": "C1", "status": "paid", "amount": "199.9" },
  { "customerId": "C1", "status": "NEW", "amount": "50" },
  { "customerId": "C2", "status": "SETTLED", "amount": "10.1" }
]
```

**Expected:**

```json
[
  { "customerId": "C1", "points": 199 },
  { "customerId": "C2", "points": 10 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((o) -> ["paid", "settled"] contains lower(o.status))
  groupBy $.customerId
  pluck ((rows, cid) -> {
    customerId: cid,
    points: floor(sum(rows.amount map ($ as Number)))
  })
```

---

### 75. Appointment slots to IST display with duration

**Problem:** Parse start/end ISO. Shift both to Asia/Kolkata. durationMinutes from period. Inject times — no now().

**Input:**

```json
{
  "id": "APT-1",
  "start": "2026-08-20T03:30:00Z",
  "end": "2026-08-20T04:00:00Z"
}
```

**Expected:**

```json
{
  "id": "APT-1",
  "startIst": "20-Aug-2026 09:00",
  "endIst": "20-Aug-2026 09:30",
  "durationMinutes": 30
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var s = payload.start as DateTime
var e = payload.end as DateTime
---
{
  id: payload.id,
  startIst: (s >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  endIst: (e >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  durationMinutes: ((e as Number) - (s as Number)) / 60000
}
```

---

### 76. BOM explode one level to pick list

**Problem:** Each finished SKU has components. Explode order lines to component qty = parent qty * per. Skip unknown BOM.

**Input:**

```json
{
  "bom": [
    { "parent": "BIKE", "component": "FRAME", "per": 1 },
    { "parent": "BIKE", "component": "WHEEL", "per": 2 }
  ],
  "orders": [
    { "sku": "BIKE", "qty": 3 },
    { "sku": "UNK", "qty": 1 }
  ]
}
```

**Expected:**

```json
[
  { "component": "FRAME", "qty": 3 },
  { "component": "WHEEL", "qty": 6 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var byP = payload.bom groupBy $.parent
---
payload.orders
  flatMap ((o) ->
    (byP[o.sku] default []) map (b) -> {
      component: b.component,
      qty: (o.qty as Number) * (b.per as Number)
    }
  )
```

---

### 77. RMA restock vs refund split

**Problem:** reason DAMAGED → refund only (restock false). Else restock true. Amount = qty * unit. fun money.

**Input:**

```json
[
  { "rma": "R1", "reason": "DAMAGED", "qty": "2", "unit": "10.00" },
  { "rma": "R2", "reason": "SIZE", "qty": 1, "unit": "15.5" }
]
```

**Expected:**

```json
[
  { "rma": "R1", "restock": false, "refund": 20.00 },
  { "rma": "R2", "restock": true, "refund": 15.50 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload map {
  rma: $.rma,
  restock: upper($.reason) != "DAMAGED",
  refund: money(($.qty as Number) * ($.unit as Number))
}
```

---

### 78. Catalog pick locale with English fallback

**Problem:** For each product pick name[locale] default name.en. Drop other locales.

**Input:**

```json
{
  "locale": "hi",
  "products": [
    { "id": "P1", "name": { "en": "Shirt", "hi": "Kamiz" } },
    { "id": "P2", "name": { "en": "Hat" } }
  ]
}
```

**Expected:**

```json
[
  { "id": "P1", "title": "Kamiz" },
  { "id": "P2", "title": "Hat" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var loc = payload.locale
---
payload.products map {
  id: $.id,
  title: ($.name[loc]) default $.name.en
}
```

---

### 79. Partner catalog XML to JSON products

**Problem:** Read attributes id and repeating Item. price as Number. Single XML root.

**Input:**

```xml
<Catalog xmlns="http://partner.example/cat">
  <Item id="I1"><Name>Bolt</Name><Price>2.5</Price></Item>
  <Item id="I2"><Name>Nut</Name><Price>0.75</Price></Item>
</Catalog>
```

**Expected:**

```json
[
  { "id": "I1", "name": "Bolt", "price": 2.5 },
  { "id": "I2", "name": "Nut", "price": 0.75 }
]
```

**Solution:**

```dataweave
%dw 2.0
ns cat http://partner.example/cat
output application/json
---
payload.cat#Catalog.*cat#Item map {
  id: $.@id,
  name: $.cat#Name,
  price: $.cat#Price as Number
}
```

---

### 80. Health claims flatten ICD diagnosis codes

**Problem:** One output row per diagnosis. Copy claimId and member. Skip empty codes.

**Input:**

```json
{
  "claims": [
    { "claimId": "CL-1", "member": "M9", "dx": ["E11.9", "I10"] },
    { "claimId": "CL-2", "member": "M9", "dx": [""] }
  ]
}
```

**Expected:**

```json
[
  { "claimId": "CL-1", "member": "M9", "icd": "E11.9" },
  { "claimId": "CL-1", "member": "M9", "icd": "I10" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.claims
  flatMap ((c) ->
    (c.dx default [])
      filter ((code) -> !isEmpty(code))
      map { claimId: c.claimId, member: c.member, icd: $ }
  )
```

---

### 81. Telecom CDR aggregate minutes by MSISDN

**Problem:** Sum durationSec/60 floor per msisdn. Drop failed calls (status != OK).

**Input:**

```json
[
  { "msisdn": "91A", "durationSec": 90, "status": "OK" },
  { "msisdn": "91A", "durationSec": 30, "status": "FAIL" },
  { "msisdn": "91B", "durationSec": 120, "status": "ok" }
]
```

**Expected:**

```json
[
  { "msisdn": "91A", "minutes": 1 },
  { "msisdn": "91B", "minutes": 2 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((c) -> lower(c.status) == "ok")
  groupBy $.msisdn
  pluck ((rows, m) -> {
    msisdn: m,
    minutes: floor(sum(rows.durationSec) / 60)
  })
```

---

### 82. Listings filter amenities and map geo

**Problem:** Keep listings that contain amenity parking (any case). Output id, lat, lng, price as Number.

**Input:**

```json
[
  { "id": "L1", "geo": { "lat": 18.5, "lng": 73.8 }, "price": "90", "amenities": ["POOL", "Parking"] },
  { "id": "L2", "geo": { "lat": 19.0, "lng": 72.8 }, "price": "70", "amenities": ["gym"] }
]
```

**Expected:**

```json
[
  { "id": "L1", "lat": 18.5, "lng": 73.8, "price": 90 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((l) -> (l.amenities map lower($)) contains "parking")
  map { id: $.id, lat: $.geo.lat, lng: $.geo.lng, price: $.price as Number }
```

---

### 83. SCIM-style patch merge on user

**Problem:** Apply replace email and add phone. Reduce over ops starting from user.

**Input:**

```json
{
  "user": { "id": "U1", "email": "old@x.com", "phones": ["111"] },
  "ops": [
    { "op": "replace", "path": "email", "value": "new@x.com" },
    { "op": "add", "path": "phones", "value": "222" }
  ]
}
```

**Expected:**

```json
{
  "id": "U1",
  "email": "new@x.com",
  "phones": ["111", "222"]
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.ops reduce ((op, acc = payload.user) ->
  if (op.op == "replace" and op.path == "email")
    acc ++ { email: op.value }
  else if (op.op == "add" and op.path == "phones")
    acc ++ { phones: (acc.phones default []) ++ [op.value] }
  else acc
)
```

---

### 84. Payment recon: bank UTR vs gateway charges

**Problem:** Match on utr. Status MATCHED if amounts equal (as Number), AMOUNT_MISMATCH if both exist else UNMATCHED. Include both sides.

**Input:**

```json
{
  "bank": [
    { "utr": "U1", "amt": "100.00" },
    { "utr": "U2", "amt": "40" }
  ],
  "gateway": [
    { "utr": "U1", "amt": 100 },
    { "utr": "U3", "amt": 9 }
  ]
}
```

**Expected:**

```json
[
  { "utr": "U1", "status": "MATCHED", "bank": 100.00, "gateway": 100.00 },
  { "utr": "U2", "status": "UNMATCHED", "bank": 40.00, "gateway": null },
  { "utr": "U3", "status": "UNMATCHED", "bank": null, "gateway": 9.00 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n) = if (n == null) null else (n as Number) as String {format: "0.00"} as Number
var b = payload.bank groupBy $.utr
var g = payload.gateway groupBy $.utr
var keys = (namesOf(b) ++ namesOf(g)) distinctBy $
---
keys map (k) -> do {
  var bv = b[k][0].amt default null
  var gv = g[k][0].amt default null
  ---
  {
    utr: k,
    status: if (bv != null and gv != null)
              if ((bv as Number) == (gv as Number)) "MATCHED" else "AMOUNT_MISMATCH"
            else "UNMATCHED",
    bank: money(bv),
    gateway: money(gv)
  }
}
```

---

### 85. Manufacturing routing duration by work order

**Problem:** Sum step minutes per wo, order steps by seq. Output wo, steps[], totalMinutes.

**Input:**

```json
[
  { "wo": "WO1", "seq": 20, "step": "PAINT", "min": "15" },
  { "wo": "WO1", "seq": 10, "step": "CUT", "min": 30 },
  { "wo": "WO2", "seq": 10, "step": "PACK", "min": 5 }
]
```

**Expected:**

```json
[
  {
    "wo": "WO1",
    "steps": [
      { "seq": 10, "step": "CUT", "min": 30 },
      { "seq": 20, "step": "PAINT", "min": 15 }
    ],
    "totalMinutes": 45
  },
  {
    "wo": "WO2",
    "steps": [
      { "seq": 10, "step": "PACK", "min": 5 }
    ],
    "totalMinutes": 5
  }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy $.wo
  pluck ((rows, wo) -> do {
    var ordered = rows orderBy $.seq map { seq: $.seq as Number, step: $.step, min: $.min as Number }
    ---
    { wo: wo, steps: ordered, totalMinutes: sum(ordered.min) }
  })
```

---

### 86. Event-sourced account balance

**Problem:** Apply events in order: credit add, debit subtract, hold subtract. Start 0. fun money. Final balance only plus last event id.

**Input:**

```json
{
  "events": [
    { "id": "e1", "type": "credit", "amt": "100" },
    { "id": "e2", "type": "debit", "amt": "30" },
    { "id": "e3", "type": "hold", "amt": "10.5" }
  ]
}
```

**Expected:**

```json
{
  "lastEvent": "e3",
  "balance": 59.50
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
fun apply(bal, e) =
  e.type match {
    case "credit" -> bal + (e.amt as Number)
    case "debit" -> bal - (e.amt as Number)
    case "hold" -> bal - (e.amt as Number)
    else -> bal
  }
---
{
  lastEvent: payload.events[-1].id,
  balance: money(payload.events reduce ((e, acc = 0) -> apply(acc, e)))
}
```

---

### 87. Multi-tenant config overlay (deep-ish merge)

**Problem:** Start from base. Overlay tenant object with ++ (right wins). Concat arrays for `plugins` only if both are arrays — interview: document ++ is shallow. Here: merge plugins with distinctBy.

**Input:**

```json
{
  "base": { "timeout": 30, "plugins": ["auth"], "theme": "light" },
  "tenant": { "timeout": 10, "plugins": ["audit"], "region": "IN" }
}
```

**Expected:**

```json
{
  "timeout": 10,
  "plugins": ["auth", "audit"],
  "theme": "light",
  "region": "IN"
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var b = payload.base
var t = payload.tenant
---
(b ++ t) ++ {
  plugins: ((b.plugins default []) ++ (t.plugins default [])) distinctBy $
}
```

---

### 88. Canonical product GTIN and UoM conversion

**Problem:** qty in EA. If uom CS, multiply qty by packSize. gtin from first barcode type EAN13. Skip items without GTIN.

**Input:**

```json
{
  "items": [
    { "sku": "S1", "qty": 2, "uom": "CS", "packSize": 10, "barcodes": [{ "type": "UPC", "id": "x" }, { "type": "EAN13", "id": "8901234567890" }] },
    { "sku": "S2", "qty": 3, "uom": "EA", "packSize": 1, "barcodes": [{ "type": "EAN13", "id": "8900000000001" }] },
    { "sku": "S3", "qty": 1, "uom": "EA", "barcodes": [] }
  ]
}
```

**Expected:**

```json
[
  { "sku": "S1", "gtin": "8901234567890", "qtyEa": 20 },
  { "sku": "S2", "gtin": "8900000000001", "qtyEa": 3 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.items
  map (i) -> {
    sku: i.sku,
    gtin: (i.barcodes filter ((b) -> b.type == "EAN13"))[0].id,
    qtyEa: if (upper(i.uom default "EA") == "CS") (i.qty as Number) * (i.packSize default 1)
           else (i.qty as Number)
  }
  filter ((r) -> r.gtin != null)
```

---
