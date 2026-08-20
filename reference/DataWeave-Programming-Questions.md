# DataWeave Programming Questions

Hands-on **DataWeave 2.0** coding problems for interviews and practice. Each item has a problem, sample `payload`, expected output, and a solution. Try the problem before reading the answer.

Levels: **Easy (1–18)** · **Moderate (19–36)** · **Hard (37–54)** — **54 programs**.

---

## Easy (1–18)

### 1. Map employee JSON to a shorter shape

**Problem:** From each employee, output `fullName` (first + last) and `dept`.

**Input:**

```json
[
  { "firstName": "Asha", "lastName": "Rao", "department": "IT" },
  { "firstName": "Ben", "lastName": "Cole", "department": "HR" }
]
```

**Expected:**

```json
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "HR" }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  fullName: $.firstName ++ " " ++ $.lastName,
  dept: $.department
}
```

---

### 2. Filter paid orders

**Problem:** Keep only orders with `status == "PAID"`.

**Input:**

```json
[
  { "id": 1, "status": "PAID", "amount": 100 },
  { "id": 2, "status": "NEW", "amount": 50 },
  { "id": 3, "status": "PAID", "amount": 75 }
]
```

**Expected:** orders `1` and `3` only.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload filter ((o) -> o.status == "PAID")
```

---

### 3. Sum array of numbers

**Problem:** Return the total of `payload`.

**Input:** `[10, 20, 30, 40]`

**Expected:** `100`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
sum(payload)
```

---

### 4. Uppercase all string values in an object

**Problem:** Convert every value to upper case; keep the same keys.

**Input:** `{ "city": "pune", "country": "india" }`

**Expected:** `{ "city": "PUNE", "country": "INDIA" }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload mapObject ((v, k) -> { (k): upper(v as String) })
```

---

### 5. Default missing email

**Problem:** If `email` is null or missing, use `"na@example.com"`.

**Input:** `{ "name": "Sam" }`

**Expected:** `{ "name": "Sam", "email": "na@example.com" }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  name: payload.name,
  email: payload.email default "na@example.com"
}
```

---

### 6. Split a CSV line into fields

**Problem:** Split `"Asha,IT,Pune"` on comma.

**Expected:** `["Asha", "IT", "Pune"]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload splitBy ","
```

---

### 7. Join array into a comma-separated string

**Problem:** Join `["red", "green", "blue"]` with `","`.

**Expected:** `"red,green,blue"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload joinBy ","
```

---

### 8. Add tax to price

**Problem:** Add 18% tax. Return `{ price, tax, total }` with 2 decimal places as numbers.

**Input:** `{ "price": 100 }`

**Expected:** `{ "price": 100, "tax": 18, "total": 118 }`

**Solution:**

```dataweave
%dw 2.0
output application/json
var rate = 0.18
---
{
  price: payload.price,
  tax: payload.price * rate,
  total: payload.price * (1 + rate)
}
```

---

### 9. Extract unique cities

**Problem:** Unique `city` values, sorted.

**Input:**

```json
[
  { "city": "Pune" },
  { "city": "Mumbai" },
  { "city": "Pune" }
]
```

**Expected:** `["Mumbai", "Pune"]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload.city distinctBy $ orderBy $
```

---

### 10. Count items in an array

**Problem:** Return how many products are in `payload`.

**Input:** `[{ "sku": "A" }, { "sku": "B" }, { "sku": "C" }]`

**Expected:** `3`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
sizeOf(payload)
```

---

### 11. Convert JSON array to XML with a root

**Problem:** Wrap users as XML `users/user`.

**Input:** `[{ "id": 1, "name": "Asha" }, { "id": 2, "name": "Ben" }]`

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

**Expected (shape):**

```xml
<users>
  <user><id>1</id><name>Asha</name></user>
  <user><id>2</id><name>Ben</name></user>
</users>
```

---

### 12. Read XML attributes

**Problem:** From `<order id="O-9"><amount>50</amount></order>`, output JSON `{ "id", "amount" }`.

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

### 13. If/else grade from score

**Problem:** `>=90` A, `>=75` B, `>=50` C, else F.

**Input:** `{ "score": 76 }` → `"B"`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
if (payload.score >= 90) "A"
else if (payload.score >= 75) "B"
else if (payload.score >= 50) "C"
else "F"
```

---

### 14. Index each element

**Problem:** Add a 1-based `index` field.

**Input:** `["a", "b"]`

**Expected:** `[{ "index": 1, "value": "a" }, { "index": 2, "value": "b" }]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  index: $$ + 1,
  value: $
}
```

---

### 15. Flatten one level

**Problem:** Flatten `[[1, 2], [3], [4, 5]]` → `[1, 2, 3, 4, 5]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
flatten(payload)
```

---

### 16. Object keys to array of `{ key, value }`

**Problem:** Convert `{ "a": 1, "b": 2 }` to entries.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload pluck ((v, k) -> { key: k, value: v })
```

---

### 17. Boolean flag from string

**Problem:** `"Y"` / `"yes"` / `"true"` (any case) → `true`, else `false`.

**Input:** `{ "active": "Yes" }` → `{ "active": true }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
{
  active: ["y", "yes", "true"] contains lower(payload.active)
}
```

---

### 18. First three characters of a code

**Problem:** From `"MULE-12345"` take `"MULE"` (split on `-`, take first part) or first 4 chars.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
(payload splitBy "-")[0]
```

---

## Moderate (19–36)

### 19. Group orders by customer

**Problem:** Group the array by `customerId`.

**Input:**

```json
[
  { "id": 1, "customerId": "C1", "amount": 10 },
  { "id": 2, "customerId": "C2", "amount": 20 },
  { "id": 3, "customerId": "C1", "amount": 15 }
]
```

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
```

**Expected keys:** `C1` → orders 1 and 3; `C2` → order 2.

---

### 20. Total amount per customer

**Problem:** Return `{ customerId, total }` for each customer.

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy ((o) -> o.customerId)
  pluck ((orders, customerId) -> {
    customerId: customerId,
    total: sum(orders.amount)
  })
```

---

### 21. Sort products by price descending

**Input:** `[{ "name": "A", "price": 30 }, { "name": "B", "price": 90 }]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload orderBy ((p) -> -p.price)
```

---

### 22. Pivot array to object keyed by id

**Problem:** `[{ "id": "u1", "name": "Asha" }]` → `{ "u1": "Asha" }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((item, acc = {}) -> acc ++ { (item.id): item.name })
```

---

### 23. Expand order lines (flatMap)

**Problem:** One row per line item with `orderId` and `sku`.

**Input:**

```json
[
  {
    "orderId": "O1",
    "items": [{ "sku": "A" }, { "sku": "B" }]
  }
]
```

**Expected:** `[{ "orderId": "O1", "sku": "A" }, { "orderId": "O1", "sku": "B" }]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload flatMap ((order) ->
  order.items map (item) -> {
    orderId: order.orderId,
    sku: item.sku
  }
)
```

---

### 24. Remove password and ssn keys

**Input:** `{ "name": "Asha", "password": "secret", "ssn": "123", "city": "Pune" }`

**Expected:** `{ "name": "Asha", "city": "Pune" }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload filterObject ((v, k) -> !(["password", "ssn"] contains (k as String)))
```

---

### 25. Merge two objects (right wins)

**Problem:** Merge `vars.base` with `payload`.

Assume `vars.base = { "a": 1, "b": 2 }` and payload `{ "b": 9, "c": 3 }`.

**Expected:** `{ "a": 1, "b": 9, "c": 3 }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
vars.base ++ payload
```

---

### 26. Update nested city to uppercase

**Input:** `{ "customer": { "address": { "city": "pune" } } }`

**Expected:** city `"PUNE"`.

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

### 27. Parse mixed date formats

**Problem:** Accept `yyyy-MM-dd` or `dd/MM/yyyy`. Invalid → `null`.

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

### 28. Format `now()` as `dd-MMM-yyyy`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
now() as String {format: "dd-MMM-yyyy"}
```

---

### 29. CSV to JSON with number coercion

**Problem:** Incoming CSV (header row): `Name,Amount` / `Asha,10.5`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number
}
```

---

### 30. JSON to CSV

**Problem:** Write `id,name` CSV with header.

**Solution:**

```dataweave
%dw 2.0
output application/csv header=true
---
payload map {
  id: $.id,
  name: $.name
}
```

---

### 31. Left join orders to customers

**Problem:** `payload.orders` left-join `payload.customers` on `customerId` / `id`. Output `orderId`, `customerName` (`null` if missing).

**Input:**

```json
{
  "orders": [{ "id": "O1", "customerId": "C1" }],
  "customers": [{ "id": "C1", "name": "Asha" }]
}
```

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

### 32. Join without `leftJoin` (groupBy lookup)

**Same problem as 31**, using an index:

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

### 33. Pattern match status codes

**Problem:** Map HTTP-like `code`: 2xx → `ok`, 4xx → `client`, 5xx → `server`, else `other`.

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

### 34. Window / paginate an array

**Problem:** Page 2, size 2 of `[1,2,3,4,5]` → `[3,4]`

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

### 35. Deduplicate by email, keep last record

**Input:**

```json
[
  { "email": "a@x.com", "name": "Old" },
  { "email": "a@x.com", "name": "New" }
]
```

**Expected:** `[{ "email": "a@x.com", "name": "New" }]`

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

### 36. Dynamic object keys from an array of pairs

**Input:** `[{ "k": "env", "v": "prod" }, { "k": "region", "v": "in" }]`

**Expected:** `{ "env": "prod", "region": "in" }`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((p, acc = {}) -> acc ++ { (p.k): p.v })
```

---

## Hard (37–54)

### 37. Recursively flatten nested arrays

**Input:** `[1, [2, [3, 4], 5], 6]`

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

**Input:**

```json
{
  "id": "root",
  "child": { "id": "c1", "items": [{ "id": "i1" }, { "sku": "x" }] }
}
```

**Expected:** `["root", "c1", "i1"]` (order may follow tree walk)

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload..id
```

(Descendant selector. For a custom walk, recurse with `match` on Array/Object.)

---

### 39. Deep mask PII keys (`ssn`, `password`, `email`)

**Problem:** Replace those keys with `"****"` at any nesting level.

**Solution:**

```dataweave
%dw 2.0
output application/json
var hidden = ["ssn", "password", "email"]
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

**Input:** `{ "a": 1, "b": [2, { "c": 3 }], "d": "skip" }` → `6`

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

### 41. XML namespaced order to canonical JSON

**Problem:** Map `ns0:order` with repeating `ns0:line` and attribute `id`.

**Solution:**

```dataweave
%dw 2.0
ns ns0 http://acme.com/order
output application/json
---
{
  orderId: payload.ns0#order.@id,
  lines: payload.ns0#order.*ns0#line map {
    sku: $.@sku,
    qty: $.@qty as Number
  }
}
```

---

### 42. Write XML with attributes and namespace

**Problem:** Inverse of 41: JSON → namespaced XML.

**Solution:**

```dataweave
%dw 2.0
ns ns0 http://acme.com/order
output application/xml
---
ns0#order @(id: payload.orderId): {
  (payload.lines map (li) -> {
    ns0#line @(sku: li.sku, qty: li.qty): {}
  })
}
```

---

### 43. Diff two flat objects (changed keys)

**Problem:** `vars.old` vs `payload`. List `{ field, from, to }` for keys whose values changed (and keys only in one side).

**Solution:**

```dataweave
%dw 2.0
output application/json
var old = vars.old
var newp = payload
var allKeys = (namesOf(old) ++ namesOf(newp)) distinctBy $
---
allKeys
  filter ((k) -> old[k] != newp[k])
  map (k) -> { field: k, from: old[k], to: newp[k] }
```

---

### 44. Recursive nested diff

**Problem:** Return a nested object of only differences. Unchanged subtrees omitted.

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
diff(vars.old, payload)
```

---

### 45. Chunk array into batches of N (for bulk APIs)

**Input:** `[1,2,3,4,5]`, size `2` → `[[1,2],[3,4],[5]]`

**Solution:**

```dataweave
%dw 2.0
import divideBy from dw::core::Arrays
output application/json
---
payload divideBy 2
```

---

### 46. Running totals

**Input:** `[10, 20, 30]` → `[10, 30, 60]`

**Solution:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((n, acc = []) -> acc ++ [ (acc[-1] default 0) + n ])
```

---

### 47. Word frequency (case-insensitive)

**Input:** `"DataWeave dataweave mule Data"`

**Expected:** `{ "dataweave": 2, "mule": 1, "data": 1 }` (key order may vary)

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

**Problem:** A row is valid if `email` contains `"@"` and `age` is a Number `>= 18`. Return `{ valid, invalid }`.

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

**Problem:** Union by `id`; fields from left and right, right overwrites on conflict.

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

**Problem:** Uppercase every string leaf; leave numbers as-is.

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

### 51. Combinations: cartesian product of two arrays

**Input:** `{ "colors": ["R","G"], "sizes": ["S","M"] }`

**Expected:** `[{ "color": "R", "size": "S" }, { "color": "R", "size": "M" }, ...]` (4 objects)

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

### 52. Safe divide with `try`

**Problem:** `amount / qty`; if `qty` is 0 or not numeric, return `null`.

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

### 53. Build a nested org chart from a flat list

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

### 54. Invoice: compute line totals, tax, and grand total

**Input:**

```json
{
  "taxRate": 0.18,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50 },
    { "sku": "B", "qty": 1, "price": 100 }
  ]
}
```

**Expected:** each line has `lineTotal`; document has `subtotal` `200`, `tax` `36`, `grandTotal` `236`.

**Solution:**

```dataweave
%dw 2.0
output application/json
var lines = payload.lines map (l) -> l ++ { lineTotal: l.qty * l.price }
var subtotal = sum(lines.lineTotal)
var tax = subtotal * payload.taxRate
---
{
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: subtotal + tax
}
```

---

## How to practice

1. Cover the **Input** with a note and write the script first.
2. Check **Expected**, then compare with **Solution**.
3. In Anypoint Studio / DataWeave Playground, set MIME type to `application/json` (or XML/CSV as stated).
4. Stretch: change keys, add `skipNullOn`, or switch output to CSV.

## Interview whiteboard set (pick 5)

| # | Problem | Tests |
| --- | --- | --- |
| 23 | `flatMap` line items | nested arrays |
| 20 | totals per customer | `groupBy` + `sum` |
| 32 | join via `groupBy` | no nested loops |
| 39 | recursive mask | tree walk |
| 53 | org chart | recursion + `groupBy` |
| 54 | invoice totals | `do` / `var` in header |

---

*DataWeave 2.x / Mule 4. `update` and some `dw::core::Arrays` helpers need Mule 4.3+.*
