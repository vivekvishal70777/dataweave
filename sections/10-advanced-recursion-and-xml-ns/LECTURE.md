# Section — Advanced: recursion, namespaces, diffs

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/10-advanced-recursion-and-xml-ns/README.md`](../../student/tutorials/10-advanced-recursion-and-xml-ns/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Walk trees with `match` + recursion.
- Read/write namespaced XML.
- Build diffs, org charts, and invoice totals.

## Suggested video breakdown

- Split into 4–5 videos: recursion, SOAP ns (Lab 41), dynamic keys, capstone invoice (Lab 54).
- Lab 39 PII mask as a production story.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 37
- Lab 38
- Lab 39
- Lab 40
- Lab 41
- Lab 42
- Lab 43
- Lab 44
- Lab 46
- Lab 47
- Lab 48
- Lab 49
- Lab 50
- Lab 51
- Lab 53
- Lab 54

## Teach these interview questions

### Q41. How does DataWeave streaming work? When does it break?

**Answer:** For large JSON/XML/CSV, DataWeave can stream if the script is **incremental** (e.g. `payload map ...` without needing the whole document). Streaming **breaks** when you:

- Use `sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, `reduce` on the whole payload
- Access the same payload twice
- Use random index access on the full array
- Convert the entire payload to String

Interview talking point: design maps as **one-pass** `map`/`filter` when files are large; set streaming in the MIME type / reader config.

---

### Q42. Write a recursive function to flatten a nested tree of objects/arrays.

**Answer:**

```dataweave
%dw 2.0
output application/json
fun flattenTree(x) =
  x match {
    case a is Array -> a flatMap flattenTree($)
    case o is Object -> flattenTree(valuesOf(o))
    else -> [x]
  }
---
flattenTree(payload)
```

`flatMap` is `flatten(map(...))`. Recursion plus `match` on types is a classic hard-level question.

---

### Q43. How do you implement `flatMap` / why does it matter?

**Answer:** `flatMap` maps then flattens one level—ideal for 1-to-many expansions:

```dataweave
payload.orders flatMap ((order) ->
  order.items map (item) -> {
    orderId: order.id,
    sku: item.sku
  }
)
```

This “explodes” nested line items without nested arrays in the output. Writing it as `flatten(payload.orders map ...)` is equivalent.

---

### Q44. How do you preserve XML namespaces and generate namespaced output?

**Answer:**

```dataweave
%dw 2.0
ns ns0 http://example.com/order
output application/xml
---
ns0#Orders: {
  ns0#Order @(id: payload.id): {
    ns0#Amount: payload.amount
  }
}
```

Incoming XML: declare `ns` and use `payload.ns0#Orders`. Hard interviews ask about default vs prefixed namespaces and `@(xmlns: ...)`.

---

### Q47. What is the difference between `valuesOf`, `keysOf`, `namesOf`, and `entriesOf`?

**Answer:**

```dataweave
%dw 2.0
output application/json
var obj = { a: 1, b: 2 }
---
{
  keys: keysOf(obj),       // ["a", "b"] as Keys
  names: namesOf(obj),     // ["a", "b"] as Strings
  values: valuesOf(obj),   // [1, 2]
  entries: entriesOf(obj)  // [{key: "a", value: 1}, ...]
}
```

`keysOf` returns `Key` types (XML-aware). `namesOf` is usually what you want for JSON string keys.

---

### Q48. How do you dynamically construct object keys?

**Answer:** Wrap the expression in parentheses:

```dataweave
%dw 2.0
output application/json
---
payload.fields reduce ((f, acc = {}) -> acc ++ {
  (f.name): f.value
})
```

Without `( )`, `f.name` would be a literal key. This is a very common gotcha.

---

### Q49. How do you compare two payloads and produce a diff of changed fields?

**Answer:** Example approach:

```dataweave
%dw 2.0
output application/json
var old = vars.oldPayload
var newp = payload
---
namesOf(newp) filter ((k) -> old[k] != newp[k]) map (k) -> {
  field: k,
  from: old[k],
  to: newp[k]
}
```

Harder variant: recursive diff for nested objects/arrays (walk both trees with `match` on types). Mention `dw::util::Diff::diff` if the runtime version includes it.

---

### Q50. Explain function overloading and type patterns in DataWeave.

**Answer:**

```dataweave
fun describe(x: String) = "string: " ++ x
fun describe(x: Number) = "number: " ++ (x as String)
fun describe(x: Array) = "array size " ++ sizeOf(x)
fun describe(x: Any) = "other"
```

The most specific matching signature wins. Combined with `match { case x is Date -> ... }`, this is how you write type-safe polymorphic transforms.

---

### Q51. How do you parse a non-standard date or mixed-format field robustly?

**Answer:**

```dataweave
%dw 2.0
import try, orElseTry, orElse from dw::Runtime
output application/json
fun parseDate(s: String) =
  try(() -> s as Date {format: "yyyy-MM-dd"})
    orElseTry (() -> s as Date {format: "dd/MM/yyyy"})
    orElseTry (() -> s as Date {format: "dd-MMM-yyyy"})
    orElse null
---
payload map { id: $.id, date: parseDate($.date) }
```

Discuss locale (`locale: "en"`) and why silent `null` vs failing the record is a business decision.

---

### Q54. How do you implement pagination-style `take` / `drop` / windows on arrays?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
var page = vars.page default 1
var size = vars.pageSize default 20
---
payload drop ((page - 1) * size) take size
```

Also: `slice(array, from, until)`, `divideBy(array, n)` for chunking (e.g. batch API calls). Mention memory: `drop`/`take` on a streamed payload may still force materialization.

---

### Q55. How would you de-duplicate while keeping the last occurrence?

**Answer:** `distinctBy` keeps the **first** match. For last-wins:

```dataweave
%dw 2.0
output application/json
---
payload
  reduce ((item, acc = {}) -> acc ++ { (item.id): item })
  then valuesOf($)
```

Or reverse, `distinctBy`, reverse again. The `reduce` into an object keyed by id is O(n) and interview-friendly.

---

### Q56. Explain `then`, `also`, and chaining vs nested calls.

**Answer:** `then` passes the left value as `$` to the right expression:

```dataweave
payload.orders
  filter ($.active)
  then (orders) -> { count: sizeOf(orders), orders: orders }
```

Useful to name an intermediate without a `do`/`var`. `also` returns the **original** left value after a side-effect-style expression (rare in pure transforms). Prefer readable `do` blocks if chaining becomes clever rather than clear.

---

### Q57. How do you mask PII in a payload of unknown shape?

**Answer:** Recursive walk:

```dataweave
%dw 2.0
output application/json
var secretKeys = ["ssn", "password", "email"]
fun mask(x) =
  x match {
    case o is Object -> o mapObject ((v, k) -> {
      (k): if (secretKeys contains lower(k as String)) "****" else mask(v)
    })
    case a is Array -> a map mask($)
    else -> x
  }
---
mask(payload)
```

Mention `dw::util::Values::mask` / `update` with cases for known paths. Hard follow-up: do not log payloads before masking.

---
