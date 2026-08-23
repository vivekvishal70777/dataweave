# DataWeave Programming Questions (industry / interview)

Hands-on **DataWeave 2.0** problems shaped like **Mule 4 production mappings**: Salesforce-style records, commerce orders, SOAP/XML, dirty CSV, CDC diffs, and bulk APIs. Each item has a problem, sample payload, expected output, and a solution.

Levels: **Easy (1–18)** still teach one operator each, but on **real-shaped JSON**. **Moderate (19–36)** are integration patterns. **Hard (37–54)** are **interview-hard** whiteboard programs. **Industry extras (55–58)** cover Arrays helpers, timezones, `zip`, and Transform-style multi-target output.

Try the problem before reading the answer. Playground MIME type must match the sample (`application/json`, `application/xml`, or `application/csv`).

---

## Easy (1–18)

### 1. Map Salesforce Contact to a shorter API shape

**Problem:** From each Contact, output `fullName` (FirstName + LastName, single space) and `dept` from `Department`. Skip building Java-style loops.

**Input:**

```json
[
  { "Id": "003xx000001", "FirstName": "Asha", "LastName": "Rao", "Department": "IT", "Email": "asha@acme.com" },
  { "Id": "003xx000002", "FirstName": "Ben", "LastName": "Cole", "Department": "Finance", "Email": "ben@acme.com" }
]
```

**Expected:**

```json
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "Finance" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
  dept: $.Department
}
```

---

### 2. Filter settled commerce orders

**Problem:** Keep orders where status is `PAID` or `SETTLED` (any case) **and** `amount` as Number is greater than 0. Drop cancelled/zero-value noise.

**Input:**

```json
[
  { "id": "ORD-1", "status": "paid", "amount": "100.00" },
  { "id": "ORD-2", "status": "NEW", "amount": "50" },
  { "id": "ORD-3", "status": "SETTLED", "amount": 75 },
  { "id": "ORD-4", "status": "PAID", "amount": 0 }
]
```

**Expected:**

```json
[
  { "id": "ORD-1", "status": "paid", "amount": "100.00" },
  { "id": "ORD-3", "status": "SETTLED", "amount": 75 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload filter ((o) ->
  (["paid", "settled"] contains lower(o.status as String))
  and ((o.amount as Number) > 0)
)
```

---

### 3. Sum invoice line amounts (string money)

**Problem:** Return the numeric total of `amount` on each line. Incoming amounts are **strings** (typical ERP/CSV). Coerce, then `sum`.

**Input:**

```json
[
  { "sku": "SKU-A", "amount": "10.50" },
  { "sku": "SKU-B", "amount": "20" },
  { "sku": "SKU-C", "amount": "30.25" }
]
```

**Expected:** `60.75`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
sum(payload.amount map ($ as Number))
```

---

### 4. Uppercase string fields on an address object

**Problem:** Uppercase every **string** value; leave numbers as-is. Production addresses mix `city` and `postalCode`.

**Input:**

```json
{ "city": "pune", "country": "india", "postalCode": 411001 }
```

**Expected:**

```json
{ "city": "PUNE", "country": "INDIA", "postalCode": 411001 }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload mapObject ((v, k) -> {
  (k): v match {
    case s is String -> upper(s)
    else -> v
  }
})
```

---

### 5. Default missing email on an Account

**Problem:** If `Email` is null or missing, use `"noreply@acme.invalid"`. Keep `Name`.

**Input:**

```json
{ "Name": "Sam Logistics" }
```

**Expected:**

```json
{ "Name": "Sam Logistics", "Email": "noreply@acme.invalid" }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  Name: payload.Name,
  Email: payload.Email default "noreply@acme.invalid"
}
```

---

### 6. Split a CSV line into fields

**Problem:** Split a single inbound line `"Asha,IT,Pune"` on comma (no quoted commas). Output an array of fields.

**Input:**

```text
Asha,IT,Pune
```

**Expected:** `["Asha", "IT", "Pune"]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload splitBy ","
```

---

### 7. Join SKUs into a comma-separated string

**Problem:** Join `["SKU-A", "SKU-B", "SKU-C"]` with `","` for a query parameter or header.

**Input:**

```json
["SKU-A", "SKU-B", "SKU-C"]
```

**Expected:** `"SKU-A,SKU-B,SKU-C"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload joinBy ","
```

---

### 8. Add GST to a unit price (2 decimal money)

**Problem:** GST 18%. Return `{ price, tax, total }` as numbers with **2 decimal places** (writer-style rounding via `format`).

**Input:**

```json
{ "price": 99.99 }
```

**Expected:**

```json
{ "price": 99.99, "tax": 18.00, "total": 117.99 }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var rate = 0.18
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  price: money(payload.price),
  tax: money(payload.price * rate),
  total: money(payload.price * (1 + rate))
}
```

---

### 9. Extract unique billing cities, sorted

**Problem:** Unique `BillingCity` values, case-preserving first seen, then sorted A–Z. Typical Salesforce Account list.

**Input:**

```json
[
  { "BillingCity": "Pune" },
  { "BillingCity": "Mumbai" },
  { "BillingCity": "Pune" },
  { "BillingCity": "Bengaluru" }
]
```

**Expected:** `["Bengaluru", "Mumbai", "Pune"]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.BillingCity distinctBy $ orderBy $
```

---

### 10. Count line items in a composite payload

**Problem:** Return how many records are in `payload.records` (Salesforce Composite / bulk query shape).

**Input:**

```json
{
  "done": true,
  "records": [
    { "Id": "a1" },
    { "Id": "a2" },
    { "Id": "a3" }
  ]
}
```

**Expected:** `3`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
sizeOf(payload.records)
```

---

### 11. Convert JSON array to XML with a single root

**Problem:** Wrap users as XML `users/user`. XML **must** have one root. Set MIME `application/xml`.

**Input:**

```json
[{ "id": "U-1", "name": "Asha Rao" }, { "id": "U-2", "name": "Ben Cole" }]
```

**Expected:**

```xml
<users>
  <user>
    <id>U-1</id>
    <name>Asha Rao</name>
  </user>
  <user>
    <id>U-2</id>
    <name>Ben Cole</name>
  </user>
</users>
```

**Solution:**

```dataweave
%dw 2.0
output application/xml
---
users: {
  user: payload map {
    id: $.id,
    name: $.name
  }
}
```

---

### 12. Read XML attributes vs element text

**Problem:** From an order XML with `id` **attribute** and `amount` **element**, output JSON `{ "id", "amount" }` with amount as Number.

**Input:**

```xml
<order id="O-9"><amount>50.00</amount></order>
```

**Expected:**

```json
{ "id": "O-9", "amount": 50.00 }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  id: payload.order.@id,
  amount: payload.order.amount as Number
}
```

---

### 13. Classify an HTTP/integration status

**Problem:** From `{ "httpStatus": 503 }`, return `"retry"` for 408/429/5xx, `"client"` for 4xx, `"ok"` for 2xx, else `"other"`. No Java ternary.

**Input:**

```json
{ "httpStatus": 503 }
```

**Expected:** `"retry"`

**Solution:**

```dataweave
%dw 2.0
output application/json
var s = payload.httpStatus as Number
---
if ([408, 429] contains s) "retry"
else if (s >= 500 and s < 600) "retry"
else if (s >= 200 and s < 300) "ok"
else if (s >= 400 and s < 500) "client"
else "other"
```

---

### 14. Index each batch row (1-based)

**Problem:** Add a 1-based `rowNum` for error reports. `$` is value, `$$` is 0-based index.

**Input:**

```json
["alpha", "beta"]
```

**Expected:**

```json
[{ "rowNum": 1, "value": "alpha" }, { "rowNum": 2, "value": "beta" }]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  rowNum: $$ + 1,
  value: $
}
```

---

### 15. Flatten one level of nested arrays

**Problem:** Flatten one level only: `[[1, 2], [3], [4, 5]]` → `[1, 2, 3, 4, 5]`. Deeper trees are a later lab.

**Input:**

```json
[[1, 2], [3], [4, 5]]
```

**Expected:** `[1, 2, 3, 4, 5]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
flatten(payload)
```

---

### 16. Object keys to array of `{ key, value }`

**Problem:** Convert a config object `{ "timeout": 30, "retries": 3 }` to entries for logging or CSV.

**Input:**

```json
{ "timeout": 30, "retries": 3 }
```

**Expected:**

```json
[{ "key": "timeout", "value": 30 }, { "key": "retries", "value": 3 }]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload pluck ((v, k) -> { key: k as String, value: v })
```

---

### 17. Boolean flag from dirty string

**Problem:** `"Y"` / `"yes"` / `"true"` / `"1"` (any case) → `true`, else `false`. Common in SAP/legacy flags.

**Input:**

```json
{ "active": "Yes" }
```

**Expected:**

```json
{ "active": true }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  active: ["y", "yes", "true", "1"] contains lower(payload.active as String)
}
```

---

### 18. SKU prefix before hyphen

**Problem:** From `"MULE-12345"` take the product family `"MULE"` (split on `-`, first segment).

**Input:**

```text
MULE-12345
```

**Expected:** `"MULE"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
(payload splitBy "-")[0]
```

---

## Moderate (19–36)

### 19. Group orders by customerId

**Problem:** Group the commerce array by `customerId`. `groupBy` returns an **object** of arrays — say that in interviews.

**Input:**

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": 10 },
  { "id": "ORD-2", "customerId": "C2", "amount": 20 },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

**Expected:**

```json
{
  "C1": [
    { "id": "ORD-1", "customerId": "C1", "amount": 10 },
    { "id": "ORD-3", "customerId": "C1", "amount": 15 }
  ],
  "C2": [
    { "id": "ORD-2", "customerId": "C2", "amount": 20 }
  ]
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
```

---

### 20. Total amount per customer (groupBy + sum)

**Problem:** Return `{ customerId, orderCount, total }` per customer. Coerce amounts. This is the standard interview follow-up to `groupBy`.

**Input:**

```json
[
  { "id": "ORD-1", "customerId": "C1", "amount": "10.00" },
  { "id": "ORD-2", "customerId": "C2", "amount": "20" },
  { "id": "ORD-3", "customerId": "C1", "amount": 15 }
]
```

**Expected:**

```json
[
  { "customerId": "C1", "orderCount": 2, "total": 25.00 },
  { "customerId": "C2", "orderCount": 1, "total": 20 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
  pluck ((orders, customerId) -> {
    customerId: customerId,
    orderCount: sizeOf(orders),
    total: sum(orders.amount map ($ as Number))
  })
```

---

### 21. Sort products by unitPrice descending

**Problem:** Highest price first (catalog / pricing API).

**Input:**

```json
[
  { "sku": "SKU-A", "unitPrice": 30 },
  { "sku": "SKU-B", "unitPrice": 90 },
  { "sku": "SKU-C", "unitPrice": 90 }
]
```

**Expected:** SKU-B and SKU-C before SKU-A (equal prices keep relative order).

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload orderBy ((p) -> -p.unitPrice)
```

---

### 22. Pivot array to object keyed by Id

**Problem:** `[{ "Id": "001xxA", "Name": "Acme" }]` → `{ "001xxA": "Acme" }` for O(1) lookup. Dynamic key **must** use parentheses.

**Input:**

```json
[
  { "Id": "001xxA", "Name": "Acme Corp" },
  { "Id": "001xxB", "Name": "Globex" }
]
```

**Expected:**

```json
{ "001xxA": "Acme Corp", "001xxB": "Globex" }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((item, acc = {}) -> acc ++ { (item.Id): item.Name })
```

---

### 23. Expand order lines (flatMap)

**Problem:** One canonical row per line: `orderId`, `sku`, `qty`. Nested `items` must not remain nested arrays.

**Input:**

```json
[
  {
    "orderId": "O-1001",
    "items": [
      { "sku": "SKU-A", "qty": 2 },
      { "sku": "SKU-B", "qty": 1 }
    ]
  }
]
```

**Expected:**

```json
[
  { "orderId": "O-1001", "sku": "SKU-A", "qty": 2 },
  { "orderId": "O-1001", "sku": "SKU-B", "qty": 1 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload flatMap ((order) ->
  (order.items default []) map (item) -> {
    orderId: order.orderId,
    sku: item.sku,
    qty: item.qty as Number
  }
)
```

---

### 24. Strip password, ssn, and accessToken keys

**Problem:** Drop secret keys from a flat object before logging. Keys compared as strings.

**Input:**

```json
{
  "name": "Asha Rao",
  "password": "s3cret",
  "ssn": "AAAAA1234A",
  "accessToken": "00Dxx...",
  "city": "Pune"
}
```

**Expected:**

```json
{ "name": "Asha Rao", "city": "Pune" }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var deny = ["password", "ssn", "accesstoken"]
---
payload filterObject ((v, k) -> !(deny contains lower(k as String)))
```

---

### 25. Merge config overlay (right wins)

**Problem:** Shallow-merge `base` with `overlay`. Right-hand keys win. Both objects live on **payload** so this runs in the Playground (no Mule `vars` required).

**Input:**

```json
{
  "base": { "timeout": 30, "retries": 2, "region": "us-east-1" },
  "overlay": { "retries": 5, "region": "ap-south-1" }
}
```

**Expected:**

```json
{ "timeout": 30, "retries": 5, "region": "ap-south-1" }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.base ++ payload.overlay
```

---

### 26. Update nested city to uppercase (Mule 4.3+)

**Problem:** Uppercase `customer.address.city` without rebuilding the whole tree by hand.

**Input:**

```json
{ "customer": { "id": "C-9", "address": { "city": "pune", "postalCode": "411001" } } }
```

**Expected:** city `"PUNE"`, other fields unchanged.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
}
```

---

### 27. Parse mixed date formats (ISO or dd/MM/yyyy)

**Problem:** Accept `yyyy-MM-dd` or `dd/MM/yyyy`. Invalid → `null`. Do **not** use `default` for failed `as Date` (that is `try`).

**Input:**

```json
[
  { "id": "E-1", "date": "2026-08-20" },
  { "id": "E-2", "date": "21/08/2026" },
  { "id": "E-3", "date": "not-a-date" }
]
```

**Expected:** first two parse to dates; third `date` is `null`.

**Solution:**

```dataweave
%dw 2.0
import try, orElseTry, orElse from dw::Runtime
output application/json
fun parseDate(s) =
  try(() -> s as Date {format: "yyyy-MM-dd"})
    orElseTry (() -> s as Date {format: "dd/MM/yyyy"})
    orElse null
---
payload map { id: $.id, date: parseDate($.date as String) }
```

---

### 28. Format an event timestamp as `dd-MMM-yyyy`

**Problem:** Format `occurredAt` (ISO-8601 DateTime) as `dd-MMM-yyyy`. Do **not** use `now()` in the lab — interviews want deterministic transforms (inject time).

**Input:**

```json
{ "occurredAt": "2026-08-20T14:05:00Z" }
```

**Expected:** `"20-Aug-2026"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
(payload.occurredAt as DateTime) as String {format: "dd-MMM-yyyy"}
```

---

### 29. CSV to JSON with number coercion

**Problem:** Incoming CSV with header. Coerce `Amount` to Number. MIME `application/csv`.

**Input:**

```csv
Name,Amount,City
Asha,10.5,Pune
Ben,3,Mumbai
```

**Expected:**

```json
[
  { "name": "Asha", "amount": 10.5, "city": "Pune" },
  { "name": "Ben", "amount": 3, "city": "Mumbai" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number,
  city: $.City
}
```

---

### 30. JSON to CSV for finance export

**Problem:** Write `orderId,customerId,amount` CSV with header. MIME `application/csv`.

**Input:**

```json
[
  { "orderId": "O-1", "customerId": "C1", "amount": 100.5 },
  { "orderId": "O-2", "customerId": "C2", "amount": 40 }
]
```

**Expected:** CSV with header row `orderId,customerId,amount`.

**Solution:**

```dataweave
%dw 2.0
output application/csv header=true
---
payload map {
  orderId: $.orderId,
  customerId: $.customerId,
  amount: $.amount
}
```

---

### 31. Left join orders to customers

**Problem:** `payload.orders` left-join `payload.customers` on `customerId` / `id`. Output `orderId`, `customerName` (`null` if missing). Include the unmatched order.

**Input:**

```json
{
  "orders": [
    { "id": "O1", "customerId": "C1" },
    { "id": "O2", "customerId": "C9" }
  ],
  "customers": [{ "id": "C1", "name": "Asha Rao" }]
}
```

**Expected:** O1 named, O2 `customerName` null.

**Solution:**

```dataweave
%dw 2.0
import leftJoin from dw::core::Arrays
output application/json
---
leftJoin(payload.orders, payload.customers, (o) -> o.customerId, (c) -> c.id)
  map {
    orderId: $.l.id,
    customerName: $.r.name default null
  }
```

---

### 32. Join without leftJoin (groupBy lookup)

**Problem:** Same result as 31, **without** `leftJoin`. Index customers once. This is the interview answer for “avoid O(n²) and N+1 lookup”.

**Input:**

```json
{
  "orders": [
    { "id": "O1", "customerId": "C1" },
    { "id": "O2", "customerId": "C9" }
  ],
  "customers": [{ "id": "C1", "name": "Asha Rao" }]
}
```

**Expected:** same as Lab 31.

**Solution:**

```dataweave
%dw 2.0
output application/json
var byId = payload.customers groupBy ((c) -> c.id)
---
payload.orders map (o) -> {
  orderId: o.id,
  customerName: (byId[o.customerId][0].name) default null
}
```

---

### 33. Pattern match HTTP status class

**Problem:** Map `code`: 2xx → `ok`, 4xx → `client`, 5xx → `server`, else `other`. Prefer `match` over a pile of ifs in interviews.

**Input:**

```json
{ "code": 404 }
```

**Expected:** `"client"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.code match {
  case n if n >= 200 and n < 300 -> "ok"
  case n if n >= 400 and n < 500 -> "client"
  case n if n >= 500 and n < 600 -> "server"
  else -> "other"
}
```

---

### 34. Window / paginate a bulk array

**Problem:** Page 2, size 2 of a 5-item work queue → items 3 and 4. Import `dw::core::Arrays`.

**Input:**

```json
[10, 20, 30, 40, 50]
```

**Expected:** `[30, 40]`

**Solution:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
var page = 2
var size = 2
---
payload drop ((page - 1) * size) take size
```

---

### 35. Deduplicate by email, keep last record (CDC)

**Problem:** `distinctBy` keeps **first**. For last-wins upsert, reduce into an object keyed by email, then `valuesOf`.

**Input:**

```json
[
  { "email": "a@acme.com", "name": "Old" },
  { "email": "b@acme.com", "name": "Bee" },
  { "email": "a@acme.com", "name": "New" }
]
```

**Expected:** New Asha-row for `a@acme.com`, plus Bee.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
valuesOf(
  payload reduce ((item, acc = {}) -> acc ++ { (item.email): item })
)
```

---

### 36. Dynamic object keys from header pairs

**Problem:** HTTP/query pairs `[{ "k": "X-Request-Id", "v": "abc" }]` → object. Parentheses around the key expression.

**Input:**

```json
[
  { "k": "X-Request-Id", "v": "abc-123" },
  { "k": "X-Correlation-Id", "v": "corr-9" }
]
```

**Expected:**

```json
{ "X-Request-Id": "abc-123", "X-Correlation-Id": "corr-9" }
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((p, acc = {}) -> acc ++ { (p.k): p.v })
```

---

## Hard (37–54) — interview whiteboard

### 37. Recursively flatten nested arrays

**Problem:** Deep-flatten mixed arrays to a single list of leaves. One `flatten` is **not** enough.

**Input:**

```json
[1, [2, [3, 4], 5], 6]
```

**Expected:** `[1, 2, 3, 4, 5, 6]`

**Solution:**

```dataweave
%dw 2.0
output application/json
fun deepFlatten(x) =
  x match {
    case a is Array -> a flatMap deepFlatten($)
    else -> [x]
  }
---
deepFlatten(payload)
```

---

### 38. Collect all `id` fields at any depth

**Problem:** Return every `id` in a nested integration payload. Descendant `payload..id` is acceptable; be ready to recurse if the interviewer forbids `..`.

**Input:**

```json
{
  "id": "root",
  "child": { "id": "c1", "items": [{ "id": "i1" }, { "sku": "x" }] }
}
```

**Expected:** `["root", "c1", "i1"]` (walk order may vary)

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload..id
```

---

### 39. Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`)

**Problem:** Replace those keys with `"****"` at **any** nesting level before logging. Production follow-up: do not log the pre-mask payload.

**Input:**

```json
{
  "name": "Asha Rao",
  "email": "asha@acme.com",
  "address": { "ssn": "AAAAA1234A", "city": "Pune" },
  "auth": { "accessToken": "00Dxx...", "password": "x" }
}
```

**Expected:** secret fields `"****"`, `name` and `city` unchanged.

**Solution:**

```dataweave
%dw 2.0
output application/json
var hidden = ["ssn", "password", "email", "accesstoken"]
fun mask(x) =
  x match {
    case o is Object -> o mapObject ((v, k) -> {
      (k): if (hidden contains lower(k as String)) "****" else mask(v)
    })
    case a is Array -> a map mask($)
    else -> x
  }
---
mask(payload)
```

---

### 40. Recursively sum all numbers in a mixed tree

**Problem:** Sum numeric leaves in a mixed JSON document; ignore strings.

**Input:**

```json
{ "a": 1, "b": [2, { "c": 3.5 }], "d": "skip" }
```

**Expected:** `6.5`

**Solution:**

```dataweave
%dw 2.0
output application/json
fun sumNums(x) =
  x match {
    case n is Number -> n
    case a is Array -> sum(a map sumNums($))
    case o is Object -> sum(valuesOf(o) map sumNums($))
    else -> 0
  }
---
sumNums(payload)
```

---

### 41. SOAP namespaced purchase order to canonical JSON

**Problem:** Strip SOAP envelope, read `ord:PurchaseOrder` attributes and repeating `ord:Line` attributes. Two prefixes. This is a standard hard XML interview.

**Input:**

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ord="http://acme.com/order">
  <soap:Body>
    <ord:PurchaseOrder id="PO-1001" currency="INR">
      <ord:Line sku="SKU-A" qty="2" unitPrice="50.00"/>
      <ord:Line sku="SKU-B" qty="1" unitPrice="100.00"/>
    </ord:PurchaseOrder>
  </soap:Body>
</soap:Envelope>
```

**Expected:**

```json
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

**Solution:**

```dataweave
%dw 2.0
ns soap http://schemas.xmlsoap.org/soap/envelope/
ns ord http://acme.com/order
output application/json
---
{
  orderId: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@id,
  currency: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@currency,
  lines: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.*ord#Line map {
    sku: $.@sku,
    qty: $.@qty as Number,
    unitPrice: $.@unitPrice as Number
  }
}
```

---

### 42. Write namespaced XML from canonical JSON

**Problem:** Inverse of 41: JSON → `ord:PurchaseOrder` with line attributes. One root. MIME `application/xml`.

**Input:**

```json
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

**Solution:**

```dataweave
%dw 2.0
ns ord http://acme.com/order
output application/xml
---
ord#PurchaseOrder @(id: payload.orderId, currency: payload.currency): {
  (payload.lines map (li) -> {
    ord#Line @(sku: li.sku, qty: li.qty, unitPrice: li.unitPrice): {}
  })
}
```

---

### 43. CDC flat diff (before vs after)

**Problem:** Compare `before` and `after` on the same payload. List `{ field, from, to }` for changed or missing keys. Platform event / Salesforce CDC style.

**Input:**

```json
{
  "before": { "status": "NEW", "amount": 10, "owner": "Asha" },
  "after": { "status": "PAID", "amount": 10, "paidAt": "2026-08-20" }
}
```

**Expected:** `status` and `owner`/`paidAt` appear as diffs; `amount` omitted.

**Solution:**

```dataweave
%dw 2.0
output application/json
var old = payload.before
var newp = payload.after
var allKeys = (namesOf(old) ++ namesOf(newp)) distinctBy $
---
allKeys
  filter ((k) -> old[k] != newp[k])
  map (k) -> { field: k, from: old[k], to: newp[k] }
```

---

### 44. Recursive nested diff

**Problem:** Return a nested object of **only** differences. Unchanged subtrees omitted. Use `payload.before` / `payload.after`.

**Input:**

```json
{
  "before": { "a": 1, "nested": { "x": 1, "y": 2 } },
  "after": { "a": 1, "nested": { "x": 1, "y": 9 } }
}
```

**Expected:** `{ "nested": { "y": { "from": 2, "to": 9 } } }` (shape may wrap `from`/`to`).

**Solution:**

```dataweave
%dw 2.0
output application/json skipNullOn="everywhere"
fun diff(a, b) =
  if (a == b) null
  else (a match {
    case ao is Object if b is Object -> do {
      var keys = (namesOf(ao) ++ namesOf(b)) distinctBy $
      var kids = keys reduce ((k, acc = {}) -> do {
        var d = diff(ao[k], b[k])
        ---
        if (d == null) acc else acc ++ { (k): d }
      })
      ---
      if (isEmpty(kids)) null else kids
    }
    else -> { from: a, to: b }
  })
---
diff(payload.before, payload.after)
```

---

### 45. Chunk array into batches of N (Salesforce Composite / bulk)

**Problem:** Split work into batches of 2 for a bulk API that caps records per call.

**Input:**

```json
[1, 2, 3, 4, 5]
```

**Expected:** `[[1, 2], [3, 4], [5]]`

**Solution:**

```dataweave
%dw 2.0
import divideBy from dw::core::Arrays
output application/json
---
payload divideBy 2
```

---

### 46. Running totals (ledger)

**Problem:** `[10, 20, 30]` → `[10, 30, 60]` (cumulative sum). Interview: immutable reduce, not a mutable Java total.

**Input:**

```json
[10, 20, 30]
```

**Expected:** `[10, 30, 60]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((n, acc = []) -> acc ++ [(acc[-1] default 0) + n])
```

---

### 47. Error-code frequency from log lines

**Problem:** Count case-insensitive tokens in an ops log string (same skill as word frequency). Ignore empty pieces.

**Input:**

```text
TIMEOUT timeout 429 TIMEOUT mule
```

**Expected:** `{ "timeout": 3, "429": 1, "mule": 1 }` (key order may vary)

**Solution:**

```dataweave
%dw 2.0
output application/json
var words = lower(payload) splitBy /[^a-z0-9]+/
---
(words filter !isEmpty($))
  groupBy $
  mapObject ((v, k) -> { (k): sizeOf(v) })
```

---

### 48. Validate and partition good vs bad rows

**Problem:** Valid if `email` contains `"@"` and `age` as Number `>= 18`. Return `{ valid, invalid }`. Coercion failures are invalid (`try`).

**Input:**

```json
[
  { "email": "a@acme.com", "age": 20 },
  { "email": "bad", "age": 17 },
  { "email": "b@acme.com", "age": "x" }
]
```

**Expected:** one valid, two invalid.

**Solution:**

```dataweave
%dw 2.0
import try from dw::Runtime
output application/json
fun isValid(r) = do {
  var ageOk = try(() -> (r.age as Number) >= 18).success default false
  ---
  (r.email default "") contains "@" and ageOk
}
---
{
  valid: payload filter isValid($),
  invalid: payload filter !isValid($)
}
```

---

### 49. Outer-join style merge of two lists by `id`

**Problem:** Union by `id`; fields from left and right, **right overwrites** on conflict (master-data merge).

**Input:**

```json
{
  "left": [{ "id": "1", "a": 1, "name": "old" }],
  "right": [{ "id": "1", "b": 2, "name": "new" }, { "id": "2", "b": 3 }]
}
```

**Expected:** id `1` has `a`, `b`, `name=new`; id `2` from right only.

**Solution:**

```dataweave
%dw 2.0
output application/json
var left = payload.left groupBy ((x) -> x.id)
var right = payload.right groupBy ((x) -> x.id)
var ids = (namesOf(left) ++ namesOf(right)) distinctBy $
---
ids map (id) -> (left[id][0] default {}) ++ (right[id][0] default {})
```

---

### 50. Tree map: apply `f` to every leaf string

**Problem:** Uppercase every string leaf; leave numbers as-is. Same recursion skeleton as PII mask.

**Input:**

```json
{ "a": "ok", "b": 2, "c": ["wait", 3] }
```

**Expected:** `{ "a": "OK", "b": 2, "c": ["WAIT", 3] }`

**Solution:**

```dataweave
%dw 2.0
output application/json
fun mapLeaves(x) =
  x match {
    case s is String -> upper(s)
    case a is Array -> a map mapLeaves($)
    case o is Object -> o mapObject ((v, k) -> { (k): mapLeaves(v) })
    else -> x
  }
---
mapLeaves(payload)
```

---

### 51. Cartesian product of SKU options

**Problem:** Product configurator: every color × every size.

**Input:**

```json
{ "colors": ["R", "G"], "sizes": ["S", "M"] }
```

**Expected:** four objects `{ color, size }`.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.colors flatMap ((c) ->
  payload.sizes map (s) -> { color: c, size: s }
)
```

---

### 52. Safe unit price with `try`

**Problem:** `amount / qty`; if `qty` is 0 or not numeric, return `null`. Contrast with `default` (nulls only).

**Input:**

```json
[
  { "id": "L-1", "amount": "10", "qty": "2" },
  { "id": "L-2", "amount": 10, "qty": 0 },
  { "id": "L-3", "amount": 10, "qty": "n/a" }
]
```

**Expected:** unit `5`, then `null`, then `null`.

**Solution:**

```dataweave
%dw 2.0
import try, orElse from dw::Runtime
output application/json
---
payload map {
  id: $.id,
  unit: try(() -> ($.amount as Number) / ($.qty as Number)) orElse null
}
```

---

### 53. Build a nested org chart from a flat HR list

**Problem:** Flat employees + `managerId` → nested `children`. Index by manager. Roots have `managerId: null`.

**Input:**

```json
[
  { "id": "1", "name": "CEO", "managerId": null },
  { "id": "2", "name": "Eng", "managerId": "1" },
  { "id": "3", "name": "Dev", "managerId": "2" }
]
```

**Expected:** CEO → children Eng → children Dev.

**Solution:**

```dataweave
%dw 2.0
output application/json
var byMgr = payload groupBy ((e) -> e.managerId default "ROOT")
fun node(e) = {
  id: e.id,
  name: e.name,
  children: (byMgr[e.id] default []) map node($)
}
---
(byMgr["ROOT"] default []) map node($)
```

---

### 54. Production invoice: discounts, tax, skip zero qty

**Problem:** Drop lines with `qty` ≤ 0. `lineTotal = qty * price * (1 - discountPct)` rounded to 2 decimals. `subtotal` = sum of line totals. `tax` = subtotal × `taxRate`. `grandTotal` = subtotal + tax. Header `var` / `fun money`.

**Input:**

```json
{
  "taxRate": 0.18,
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "price": 50, "discountPct": 0.10 },
    { "sku": "SKU-B", "qty": 1, "price": 100, "discountPct": 0 },
    { "sku": "SKU-Z", "qty": 0, "price": 999, "discountPct": 0 }
  ]
}
```

**Expected:** SKU-Z omitted; SKU-A `lineTotal` 90.00; SKU-B 100.00; `subtotal` 190.00; `tax` 34.20; `grandTotal` 224.20.

**Solution:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var lines = payload.lines
  filter ((l) -> (l.qty as Number) > 0)
  map (l) -> do {
    var qty = l.qty as Number
    var price = l.price as Number
    var disc = (l.discountPct default 0) as Number
    ---
    l ++ { lineTotal: money(qty * price * (1 - disc)) }
  }
var subtotal = money(sum(lines.lineTotal))
var tax = money(subtotal * payload.taxRate)
---
{
  currency: payload.currency,
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: money(subtotal + tax)
}
```

---

## Industry extras (55–58)

### 55. maxBy and firstWith on a work queue

**Problem:** From a list of orders, return `{ richest, firstPaid }`. `richest` is the item with max `amount` (coerce Number). `firstPaid` is the first item whose status is `PAID` (any case). Import `dw::core::Arrays`.

**Input:**

```json
[
  { "id": "O1", "status": "NEW", "amount": "40" },
  { "id": "O2", "status": "paid", "amount": "15" },
  { "id": "O3", "status": "PAID", "amount": 90 }
]
```

**Expected:**

```json
{
  "richest": { "id": "O3", "status": "PAID", "amount": 90 },
  "firstPaid": { "id": "O2", "status": "paid", "amount": "15" }
}
```

**Solution:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy ((o) -> o.amount as Number),
  firstPaid: payload firstWith ((o) -> lower(o.status as String) == "paid")
}
```

---

### 56. Shift DateTime to IST for display

**Problem:** Canonical APIs store UTC. Output `occurredAtIst` as `dd-MMM-yyyy HH:mm` in `Asia/Kolkata`. Do not use `now()`.

**Input:**

```json
{ "occurredAt": "2026-08-20T14:05:00Z" }
```

**Expected:** IST is UTC+5:30 → `20-Aug-2026 19:35`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  occurredAtIst: ((payload.occurredAt as DateTime) >> "Asia/Kolkata")
    as String {format: "dd-MMM-yyyy HH:mm"}
}
```

---

### 57. Zip headers with values into an object

**Problem:** Dynamic columns: `headers` + `values` (same length). Build `{ Name: "Asha", Amount: "10.5" }` using `zip` and dynamic keys.

**Input:**

```json
{
  "headers": ["Name", "Amount", "City"],
  "values": ["Asha", "10.5", "Pune"]
}
```

**Expected:**

```json
{ "Name": "Asha", "Amount": "10.5", "City": "Pune" }
```

**Solution:**

```dataweave
%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  reduce ((pair, acc = {}) -> acc ++ { (pair[0]): pair[1] })
```

---

### 58. Simulate Transform Message payload + vars

**Problem:** One script returns **two targets** as an object (Playground cannot set Mule vars). `payload` = `{ orderId, amount }` with amount as Number. `vars` = `{ correlationId, recordCount }`. `correlationId` from `payload.headers.xCorrelationId` default `"missing"`.

**Input:**

```json
{
  "headers": { "xCorrelationId": "corr-9" },
  "order": { "id": "O-1", "amount": "42.00" }
}
```

**Expected:**

```json
{
  "payload": { "orderId": "O-1", "amount": 42.00 },
  "vars": { "correlationId": "corr-9", "recordCount": 1 }
}
```

**Solution:**

```dataweave
%dw 2.0
output application/json
var canonical = {
  orderId: payload.order.id,
  amount: payload.order.amount as Number
}
---
{
  payload: canonical,
  vars: {
    correlationId: payload.headers.xCorrelationId default "missing",
    recordCount: 1
  }
}
```

---

## How to practice

1. Cover the **Input** and write the script first (interview rules).
2. Check **Expected**, then compare with **Solution**.
3. Set MIME to `application/json` (or XML/CSV as stated).
4. Stretch: `skipNullOn="everywhere"`, switch JSON → CSV, or inject `attributes.queryParams.page` instead of hard-coded page.

## Interview whiteboard set (pick 5)

| # | Problem | What they score |
| --- | --- | --- |
| 23 | `flatMap` line items | nested arrays, named lambdas |
| 20 | totals per customer | `groupBy` + coerce + `sum` |
| 32 | join via `groupBy` | no nested loops, no N+1 `lookup` |
| 39 | recursive PII mask | `match` on types, logging story |
| 41 | SOAP → canonical JSON | two `ns`, attributes, repeating lines |
| 53 | org chart | recursion + `groupBy` |
| 54 | invoice | `fun money`, `do`, filter zero qty |

---

*Aligned with Mule 4 / DataWeave 2.x. `update`, `leftJoin`, `divideBy`, `drop`/`take` need **Mule 4.3+** / current `dw::core::Arrays`.*
