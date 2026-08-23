# MuleSoft DataWeave Interview Questions and Answers

A practical set of **60 DataWeave questions** for **Mule 4 / DataWeave 2.x production interviews**. Answers include the syntax plus what a senior interviewer expects next (streaming, N+1, money rounding, namespaces). Pair with the industry-shaped drills in [DataWeave-Programming-Questions.md](DataWeave-Programming-Questions.md).

For hands-on coding drills (input → expected output → solution), see [DataWeave-Programming-Questions.md](DataWeave-Programming-Questions.md).

---

## Easy (Questions 1–20)

### 1. What is DataWeave?

**Answer:** DataWeave is MuleSoft’s functional data transformation language. In Mule 4 it is the primary way to map, filter, enrich, and convert payloads between formats such as JSON, XML, CSV, Java objects, and strings. Scripts run inside the Transform Message component and also as DataWeave expressions (`#[...]`) in other processors.

### 2. What is the difference between DataWeave 1.0 and DataWeave 2.0?

**Answer:**

| Area | DataWeave 1.0 (Mule 3) | DataWeave 2.0 (Mule 4) |
| --- | --- | --- |
| Header | `%dw 1.0` | `%dw 2.0` |
| Language | MEL + DW 1.0 | DataWeave everywhere (`#[...]`) |
| Operators | `map` / `mapObject` syntax differences | Unified functions, modules (`dw::core::*`) |
| Null handling | More implicit | Explicit (`default`, `?`, `try`) |
| Output | `%output application/json` | `output application/json` |

Interviews almost always expect **DataWeave 2.0**.

### 3. What is the basic structure of a DataWeave script?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  greeting: "Hello " ++ payload.name
}
```

- Header: version, output MIME type, imports, functions, variables.
- `---` separates header from body.
- Body: the expression that becomes the output payload.

### 4. How do you declare a variable in DataWeave?

**Answer:** Use `var` in the header (script-scoped) or inside a `do` block.

```dataweave
%dw 2.0
output application/json
var taxRate = 0.18
---
{
  total: payload.amount * (1 + taxRate)
}
```

Variables are immutable. Comments: `//` and `/* */` in header or body.

### 5. How do you define a custom function?

**Answer:**

```dataweave
%dw 2.0
output application/json
fun fullName(first: String, last: String) = first ++ " " ++ last
---
fullName(payload.firstName, payload.lastName)
```

Functions can be overloaded by argument types and arity.

### 6. What are the main DataWeave data types?

**Answer:** `String`, `Boolean`, `Number`, `Date`, `DateTime`, `LocalDateTime`, `Time`, `Period`, `Regex`, `Array`, `Object`, `Null`, `Binary`, `Type`, and `Any`. Type annotations are optional but useful in interviews and modules:

```dataweave
fun add(a: Number, b: Number): Number = a + b
```

### 7. How do you convert types (`as`)?

**Answer:** Use `as` for coercion:

```dataweave
payload.age as Number
payload.createdAt as Date {format: "yyyy-MM-dd"}
payload as String {encoding: "UTF-8"}
```

If coercion fails, the script errors unless you use `try` / `default`.

### 8. How do `map` and `filter` work on arrays?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
payload.orders
  filter ((order) -> order.status == "PAID")
  map ((order) -> {
    id: order.id,
    total: order.amount
  })
```

- `$` is the current item, `$$` is the index: `payload map { index: $$, value: $ }`.
- `filter` keeps elements where the predicate is `true`.

### 9. What is `pluck`?

**Answer:** `pluck` turns an object into an array by iterating keys/values.

```dataweave
{ a: 1, b: 2 } pluck ((value, key, index) -> { k: key, v: value })
// [{k: "a", v: 1}, {k: "b", v: 2}]
```

Use it when you need an array from an object’s fields.

### 10. How do you concatenate strings and arrays?

**Answer:**

- Strings: `++` (`"Hello" ++ " " ++ "World"`)
- Arrays: `++` (`[1, 2] ++ [3]`)
- Objects: `++` merges keys (right side wins on conflict)

`+` is numeric addition, not concatenation.

### 11. How do you handle missing fields and nulls?

**Answer:**

```dataweave
payload.email default "unknown"
payload.address.city default ""
payload.address.?city          // null-safe selector; returns null if address is null
```

`default` replaces `null` (and missing values that evaluate to null). It does **not** catch errors—use `try` for that.

### 12. How do you write if/else in DataWeave?

**Answer:** DataWeave uses expressions, not statements:

```dataweave
if (payload.age >= 18) "adult"
else if (payload.age >= 13) "teen"
else "child"
```

There is no ternary `? :` operator like Java.

### 13. What is the difference between `.` and `[]` selectors?

**Answer:**

- `payload.customer.name` — named key selector.
- `payload[0]` — array index.
- `payload["first-name"]` — key that is not a valid identifier.
- `payload.*item` — multi-value selector (all `item` children, useful in XML).
- `payload..id` — descendants selector (all `id` fields at any depth).

### 14. How do you transform JSON to XML (and vice versa)?

**Answer:** Change the `output` MIME type and shape the tree:

```dataweave
%dw 2.0
output application/xml
---
orders: {
  order: payload map {
    id: $.id,
    amount: $.amount
  }
}
```

JSON to XML needs a **single root**. XML to JSON is the reverse: `output application/json` and select elements/attributes (`payload.orders.order.@id` for attributes).

### 15. What does `sizeOf` and `isEmpty` do?

**Answer:**

```dataweave
sizeOf(payload.items)     // array length, object key count, or string length
isEmpty(payload.items)    // true for [], {}, "", or null in many cases
```

Prefer `isEmpty` over `sizeOf(x) == 0` in interviews.

### 16. How do you split, join, and change case of strings?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  parts: payload.csvLine splitBy ",",
  csv: ["a", "b"] joinBy ",",
  upper: upper(payload.name),
  lower: lower(payload.name),
  cap: capitalize(payload.name)
}
```

`splitBy` returns an array; `joinBy` builds a string. Industry follow-ups from `dw::core::Strings`: `trim`, `replace`, `substringAfter` / `substringBefore`, `pad`, `repeat`, and regex `find` / `scan` (see Q68).

### 17. How do you read Mule variables, attributes, and properties in DataWeave?

**Answer:**

```dataweave
vars.customerId
attributes.headers["content-type"]
attributes.queryParams.page
p("http.host")               // from configuration properties
Mule::p("api.version")       // same idea in some contexts
```

In Transform Message you can also map from the **input graph** (`payload`, `vars`, `attributes`). HTTP Listener extras interviewers want: `attributes.method`, `attributes.requestPath` / `rawRequestUri`, `attributes.uriParams.orderId`, `attributes.queryParams.page`, `attributes.headers['authorization']` (often lower-cased). `error.errorType` / `error.errorMessage.payload` belong in **On Error** scopes, not in a happy-path script (see Q73).

### 18. What is the difference between Transform Message and a DataWeave expression in a Set Payload?

**Answer:**

- **Transform Message**: full script with header, preview, metadata, multiple outputs (`payload`, `variables`).
- **`#[...]` expression**: a DataWeave expression (often without a full header) used inline, e.g. `#[payload.orderId]`.

Both use DataWeave 2 in Mule 4.

### 19. How do you `write` and `read` data inside a script?

**Answer:** Use `write(value, mimeType, properties)` to serialize a value to String/Binary without changing the Transform **output** MIME, and `read(binaryOrString, mimeType)` to parse. Typical interview case: log a JSON snapshot, or parse a JSON **string field** inside XML/CSV.

```dataweave
%dw 2.0
output application/json
---
{
  asText: write(payload.order, "application/json", { indent: false }),
  nested: read(payload.jsonBlob, "application/json")
}
```

This is **not** the same as `output application/json` on the script (that sets the Mule payload writer). Follow-up: huge `write(payload)` can break streaming.

### 20. What does `output application/json skipNullOn="everywhere"` do?

**Answer:** Writer properties control serialization. `skipNullOn="everywhere"` omits fields whose values are `null` from JSON/XML output. Other common properties:

- `indent=false` — compact JSON
- `duplicateKeyAsArray=true` — XML
- `header=true` / `separator=","` — CSV

```dataweave
%dw 2.0
output application/json skipNullOn="everywhere", indent=false
---
{ a: 1, b: null }   // { "a": 1 }
```

---

## Moderate (Questions 21–40)

### 21. Explain `mapObject`. When do you use it instead of `map`?

**Answer:** `map` iterates **arrays** and returns an **array**. `mapObject` iterates **objects** and returns an **object**.

```dataweave
payload mapObject ((value, key) -> {
  (upper(key as String)): value
})
```

Use `mapObject` to rename keys, drop/keep fields, or transform every value while keeping object shape.

### 22. How do `groupBy`, `orderBy`, and `distinctBy` work?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  byCity: payload groupBy ((c) -> c.city),
  sorted: payload orderBy ((c) -> c.name),
  unique: payload distinctBy ((c) -> c.email)
}
```

`groupBy` returns an **object** whose keys are group names and values are arrays.

### 23. Explain `reduce`. Give an example of a sum and of building an object.

**Answer:** `reduce` folds an array into a single value.

```dataweave
[1, 2, 3] reduce ((item, acc = 0) -> acc + item)   // 6

payload reduce ((item, acc = {}) -> acc ++ {
  (item.id): item.name
})
```

If you omit the accumulator initializer, the first element is the seed and iteration starts at the second element.

### 24. How do you flatten nested arrays?

**Answer:**

```dataweave
flatten([[1, 2], [3], [4, 5]])     // [1, 2, 3, 4, 5]
```

`flatten` is only one level. For deeper trees, write a recursive function or flatten in steps.

### 25. How do you merge two objects? What happens with duplicate keys?

**Answer:** `++` and `dw::core::Objects::mergeWith`:

```dataweave
%dw 2.0
import mergeWith from dw::core::Objects
output application/json
---
{
  concat: { a: 1, b: 2 } ++ { b: 9, c: 3 },     // {a:1, b:9, c:3} — right wins
  merged: { a: {x: 1} } mergeWith { a: {y: 2} } // deep merge depending on values
}
```

`++` is a **shallow** merge (right key overwrites the whole nested object). `mergeWith` is the interview follow-up for **deep** merge of nested objects. Minus on objects (`payload - "password"`) drops keys. For arrays of objects, merge by `id` is Lab 49, not `++`.

### 26. How do you update a nested field without rebuilding the whole object?

**Answer:** Use the `update` operator (DataWeave 2.3+ / Mule 4.3+):

```dataweave
%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
  case .items[0].qty -> $ + 1
}
```

This is preferred in interviews over copying every field by hand.

### 27. What is a `do` block and why is it useful?

**Answer:** `do` creates a local scope for `var` / `fun` so the header stays clean.

```dataweave
payload.orders map (order) -> do {
  var tax = order.amount * 0.18
  ---
  { id: order.id, total: order.amount + tax }
}
```

Use it for intermediate values inside `map`/`filter`.

### 28. How does pattern matching (`match`) work?

**Answer:**

```dataweave
payload.status match {
  case "NEW" -> "created"
  case "PAID" -> "completed"
  case s if s startsWith "ERR" -> "failed"
  case n is Number -> "numeric-status"
  else -> "unknown"
}
```

`match` is exhaustive-style pattern matching: literals, types (`is`), conditions, and `else`.

### 29. How do you handle errors in DataWeave (`try`)?

**Answer:**

```dataweave
%dw 2.0
import try, orElse, orElseTry from dw::Runtime
output application/json
---
{
  n: try(() -> payload.age as Number) orElse 0,
  safe: try(() -> 1 / payload.divisor)
}
```

`try` returns `{ success: true, result: ... }` or `{ success: false, error: ... }`. Combine with `orElse` for fallbacks. This is **not** a Mule error handler; it only catches failures **inside** the script.

### 30. How do you work with dates and periods?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  today: now(),
  formatted: now() as String {format: "dd-MMM-yyyy"},
  parsed: "2026-08-20" as Date {format: "yyyy-MM-dd"},
  nextWeek: (now() as Date) + |P7D|,
  ageDays: |P1Y2M| 
}
```

Date literals use pipes: `|2026-08-20|`, `|P7D|` (ISO-8601 periods). Prefer injecting time as a field (Lab 28) over `now()` in reusable modules. Timezones: `DateTime` has an offset; `LocalDateTime` does not. Shift with `payload.ts as DateTime >> "Asia/Kolkata"`. More helpers: `dw::core::Dates` (`daysBetween`, `atBeginningOfDay`) — Q66–Q67.

### 31. How do you transform CSV to JSON?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number
}
```

CSV is typically read as an **array of objects** (header row = keys). Reader properties: `header=true`, `separator=";"`, `quoteValues=true`.

### 32. How do you generate CSV from JSON?

**Answer:**

```dataweave
%dw 2.0
output application/csv header=true, separator=","
---
payload map {
  OrderId: $.id,
  Total: $.amount
}
```

Keys become column headers when `header=true`.

### 33. How do you read XML attributes vs elements?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  id: payload.order.@id,           // attribute
  name: payload.order.customer,    // element text / child
  items: payload.order.*item       // repeating child elements
}
```

To **write** attributes:

```dataweave
order @(id: payload.id): {
  customer: payload.name
}
```

### 34. What are DataWeave modules? How do you import them?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
import someFun from modules::MyModule
import dw::core::Arrays
output application/json
---
Arrays.drop(payload, 2)
```

Built-in modules include `dw::Core`, `dw::core::Strings`, `Arrays`, `Objects`, `Dates`, `Periods`, `Binaries`, `URL`, `Crypto`, `Runtime`, `dw::util::Values`. Custom modules are `.dwl` files under `src/main/resources/modules`.

### 35. Explain `$`, `$$`, and `$$$` in lambdas.

**Answer:** Implicit parameters in function literals:

- `$` — first argument (item / value)
- `$$` — second (index / key depending on function)
- `$$$` — third (index in `mapObject` / `pluck`)

```dataweave
["a", "b"] map upper($)
{ a: 1 } mapObject ((v, k) -> { (k): v }) 
```

Interview tip: named parameters (`(item, index) ->`) are clearer than `$`/`$$`.

### 36. How do you filter object keys dynamically?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Objects
output application/json
---
payload filterObject ((value, key) -> !(["password", "ssn"] contains (key as String)))
```

`filterObject` keeps entries where the predicate is true. `dw::util::Values::mask` is another option for hiding fields.

### 37. How do you join two arrays like a SQL join?

**Answer:** `dw::core::Array` join functions:

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
leftJoin(payload.orders, payload.customers,
  (o) -> o.customerId,
  (c) -> c.id)
```

Also: `join` (inner), `outerJoin`, `leftJoin`. Result items look like `{ l: leftItem, r: rightItem }`. For simple lookups, `groupBy` plus indexing is common.

### 38. How do you call Java from DataWeave? When should you not?

**Answer:**

```dataweave
%dw 2.0
import java!java::util::UUID
output application/json
---
{
  id: UUID::randomUUID() as String
}
```

You can invoke static methods and, with care, instance methods. Prefer pure DataWeave for transformations. Use Java for libraries you cannot reproduce (special crypto, proprietary parsers). Java calls add coupling and can hurt streaming/performance.

### 39. What is the difference between `startsWith`, `contains`, and `matches`?

**Answer:**

```dataweave
"MuleSoft" startsWith "Mule"     // true
["a", "b"] contains "a"          // true
"abc123" matches /[a-z]+[0-9]+/  // true (full match vs regex)
```

`matches` uses a regular expression against the whole string. For partial regex, use `payload find /pattern/` or `contains` for substrings.

### 40. How do you use `lookup` (Mule 4) vs DataWeave-only alternatives?

**Answer:** Flow `lookup` (from `dw::Runtime` / Mule functions) invokes **another flow** and returns its payload—useful for enrichment, but it is synchronous and expensive.

```dataweave
lookup("get-customer-flow", { id: payload.customerId })
```

Prefer **lookup tables as objects**, `groupBy`, database/HTTP connectors **outside** Transform Message, or `Mule::p()` for config. Mention in interviews: do not hide heavy I/O inside every `map` iteration if you can batch it.

---

## Hard (Questions 41–60)

### 41. How does DataWeave streaming work? When does it break?

**Answer:** For large JSON/XML/CSV, DataWeave can stream if the script is **incremental** (e.g. `payload map ...` without needing the whole document). Streaming **breaks** when you:

- Use `sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, `reduce` on the whole payload
- Access the same payload twice
- Use random index access on the full array
- Convert the entire payload to String

Interview talking point: design maps as **one-pass** `map`/`filter` when files are large; set streaming in the MIME type / reader config.

### 42. Write a recursive function to flatten a nested tree of objects/arrays.

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

### 43. How do you implement `flatMap` / why does it matter?

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

### 44. How do you preserve XML namespaces and generate namespaced output?

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

### 45. Explain `dw::Crypto` hashing vs HMAC. When is each used?

**Answer:**

```dataweave
%dw 2.0
import dw::Crypto
output application/json
---
{
  sha: Crypto::hashWith(payload as Binary, "SHA-256"),
  hmac: Crypto::HMACBinary(payload as Binary, "secret" as Binary, "HmacSHA256")
}
```

Hashing is one-way checksums (file integrity). HMAC signs with a secret (webhook verification). Never roll your own encoding; watch Binary vs String and Base64 wrapping (`dw::core::Binaries::toBase64`).

### 46. How do you write a reusable `.dwl` module and unit-test it?

**Answer:**

`src/main/resources/modules/Pricing.dwl`:

```dataweave
%dw 2.0
fun withTax(amount: Number, rate: Number = 0.18) = amount * (1 + rate)
```

Import: `import withTax from modules::Pricing`.

Tests: MUnit with DataWeave assertions, or a `src/test/resources` script. Interview plus: default argument values, type signatures, and keeping modules **pure** (no `lookup`, no `now()` if you want determinism—inject time as a parameter).

### 47. What is the difference between `valuesOf`, `keysOf`, `namesOf`, and `entriesOf`?

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

### 48. How do you dynamically construct object keys?

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

### 49. How do you compare two payloads and produce a diff of changed fields?

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

### 50. Explain function overloading and type patterns in DataWeave.

**Answer:**

```dataweave
fun describe(x: String) = "string: " ++ x
fun describe(x: Number) = "number: " ++ (x as String)
fun describe(x: Array) = "array size " ++ sizeOf(x)
fun describe(x: Any) = "other"
```

The most specific matching signature wins. Combined with `match { case x is Date -> ... }`, this is how you write type-safe polymorphic transforms.

### 51. How do you parse a non-standard date or mixed-format field robustly?

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

### 52. How do you process multipart / binary / Base64 in DataWeave?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Binaries
output application/json
---
{
  b64: toBase64(payload as Binary),
  bytes: fromBase64(vars.fileBase64),
  asText: (payload as Binary) as String {encoding: "UTF-8"}
}
```

For multipart, Mule gives `parts` (e.g. `payload.parts.file.content`). Avoid loading huge binaries as String. Set `output application/octet-stream` when the result must stay binary.

### 53. What are reader/writer properties you should mention for XML, JSON, and CSV?

**Answer:**

**JSON:** `streaming`, `indexed`, `duplicateKeyAsArray`

**XML:** `ignoreRootElement`, `nullValueOn`, `writeDeclaration`, `encoding`, `indent`, `escapeCR`

**CSV:** `header`, `separator`, `quote`, `escape`, `bodyStartLineNumber`, `ignoreEmptyLine`

Example:

```dataweave
%dw 2.0
output application/xml writeDeclaration=true, encoding="UTF-8"
---
root: payload
```

Reader properties are often set on the **MIME type of the incoming message**, not only in the script header.

### 54. How do you implement pagination-style `take` / `drop` / windows on arrays?

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

### 55. How would you de-duplicate while keeping the last occurrence?

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

### 56. Explain `then`, `also`, and chaining vs nested calls.

**Answer:** `then` passes the left value as `$` to the right expression:

```dataweave
payload.orders
  filter ($.active)
  then (orders) -> { count: sizeOf(orders), orders: orders }
```

Useful to name an intermediate without a `do`/`var`. `also` returns the **original** left value after a side-effect-style expression (rare in pure transforms). Prefer readable `do` blocks if chaining becomes clever rather than clear.

### 57. How do you mask PII in a payload of unknown shape?

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

### 58. What performance pitfalls do interviewers expect you to name?

**Answer:**

1. `groupBy` / `orderBy` on huge in-memory arrays  
2. Nested `filter`/`map` causing O(n²) (use `groupBy` to index first)  
3. `lookup` inside `map` (N+1 flow calls)  
4. Repeated `payload as String` then parse  
5. XML `..` descendant selector on large documents  
6. Breaking streaming (see Q41)  
7. Recursive functions without considering depth  
8. Converting entire files to Java `HashMap` unnecessarily  

9. Money as floating `Number` without a `format` round-trip (prefer `fun money`)  
10. Putting connector I/O (`lookup`, HTTP) inside Transform Message instead of before/after the map  

Fix pattern: index the right-hand collection once (`groupBy` id), then `map` the left side with O(1)/O(k) lookups. Coerce dirty strings once. Mask PII before `log`.

### 59. How do you write an infix-friendly custom function and use lambdas as arguments (higher-order functions)?

**Answer:** Functions are values:

```dataweave
%dw 2.0
output application/json
fun applyTwice(x, f) = f(f(x))
fun increment(n) = n + 1
---
{
  a: applyTwice(3, increment),
  b: applyTwice("ha", (s) -> s ++ s)
}
```

Many core functions (`map`, `filter`, `reduce`) are higher-order. Interviewers may ask you to write `compose` or a generic `treeMap`.

### 60. End-to-end: map a nested order XML to a canonical JSON API model (talk through the design).

**Answer:** A strong verbal solution covers:

1. **Reader:** SOAP or namespaced XML; declare each `ns`; `Envelope/Body` then `.*Line`.  
2. **Normalize:** attributes `@sku` → fields; dirty money `as Number`; dates with explicit `{format:...}`.  
3. **Enrich:** tax/total via `do` / `fun money` (`line = qty * price * (1 - discount)`).  
4. **Join:** customer from `vars.customer` already fetched — **not** `lookup` per line.  
5. **Shape:** canonical keys (`orderId`, `currency`, `lines[]`); drop zero-qty lines.  
6. **Writer:** `application/json skipNullOn="everywhere"`.  
7. **Errors:** invalid price `try` → `errors[]`, do not fail the whole batch unless the SLA says so.  
8. **Scale:** one-pass `map` on line items; no `orderBy` unless the API contract requires sorted lines.

Sketch:

```dataweave
%dw 2.0
ns ns0 http://acme.com/order
output application/json skipNullOn="everywhere"
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  orderId: payload.ns0#order.@id,
  customerId: payload.ns0#order.ns0#customer.@id,
  lines: payload.ns0#order.*ns0#lineItem map (li) -> do {
    var qty = li.@qty as Number
    var price = li.ns0#price as Number
    ---
    { sku: li.@sku, qty: qty, lineTotal: money(qty * price) }
  },
  orderTotal: money(
    sum(payload.ns0#order.*ns0#lineItem map ((li) -> (li.@qty as Number) * (li.ns0#price as Number)))
  )
}
```

This question scores well if you mention namespaces, repeating elements, types, and where **not** to put I/O.

---

### 61. What `dw::core::Arrays` helpers do interviewers expect besides map/filter?

**Answer:** Import `dw::core::Arrays` (Mule 4.3+ / current core):

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy $.amount,
  cheapest: payload minBy $.amount,
  firstPaid: payload firstWith ((o) -> o.status == "PAID"),
  anyOver: payload some ((o) -> (o.amount as Number) > 1000),
  allPositive: payload every ((o) -> (o.amount as Number) > 0),
  idx: indexOf(payload, ((o) -> o.id == "O1")),
  countPaid: payload countBy ((o) -> o.status == "PAID")
}
```

`maxBy` / `minBy` return the **item**, not the number. Empty arrays: guard with `isEmpty` or `default`.

### 62. How do ranges and `slice` work?

**Answer:**

```dataweave
%dw 2.0
import slice from dw::core::Arrays
output application/json
---
{
  firstThree: payload[0 to 2],
  nums: 1 to 5,
  mid: slice(payload, 1, 4)
}
```

`[0 to 2]` is inclusive. Out-of-range indexes are safer than Java (often empty, not an exception) — still do not assume that in every runtime; prefer `slice` / `take` / `drop` in production.

### 63. How do you `zip` two arrays?

**Answer:** Pair headers with values (dynamic CSV / Excel columns):

```dataweave
%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  map { name: $[0], value: $[1] }
```

Length is the shorter array. Interview follow-up: building an object with `(pair[0]): pair[1]` (dynamic keys).

### 64. How do you test types (`is`, `typeOf`)?

**Answer:** There is no Java `===`. Use `is` and `typeOf`:

```dataweave
payload is Object
payload.amount is Number
typeOf(payload)     // "Object" | "Array" | "String" | ...
```

`match { case x is Array -> ... }` is the same idea for trees (Q42, Q57).

### 65. Which number helpers should you name?

**Answer:** `sum`, `avg`, `min`, `max`, `mod`, `abs`, `ceil`, `floor`, `round`, plus **money** via `as String {format: "0.00"} as Number`. Coerce ERP strings **before** arithmetic. `sum([])` is a common trap — skip empty or `default 0`. Do not use Java `BigDecimal` unless the interviewer asks; `fun money` is the DW answer.

### 66. How do you handle timezones?

**Answer:** `DateTime` includes an offset; `LocalDateTime` / `Date` do not. Parse ISO-8601, then shift:

```dataweave
%dw 2.0
output application/json
var ts = payload.occurredAt as DateTime
---
{
  utc: ts >> "UTC",
  ist: ts >> "Asia/Kolkata",
  display: (ts >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"}
}
```

Store UTC in canonical APIs; convert only at the edge. Do not call `now()` inside a pricing module (inject `asOf`).

### 67. What is in `dw::core::Dates` / `Periods`?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Dates
output application/json
---
{
  days: daysBetween(payload.start as Date, payload.end as Date),
  startOfDay: atBeginningOfDay(payload.occurredAt as DateTime),
  nextMonth: (payload.start as Date) + |P1M|
}
```

Period literals: `|P7D|`, `|PT2H|`. Interview: SLA clocks and invoice due dates, not “print today”.

### 68. How do you `replace`, `find`, and split SKUs with Strings helpers?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  redacted: replace(payload.notes, /INV-\d+/, "REDACTED"),
  ids: payload.notes find /INV-\d+/,
  family: substringBefore(payload.sku, "-"),
  trimmed: trim(payload.name)
}
```

`matches` is a **full-string** regex (Q39). `find` / `scan` extract parts. `replace` can take a regex or a literal.

### 69. How does Transform Message set payload **and** variables?

**Answer:** One Transform Message can have **multiple output targets**: Payload, Variable, Attributes (metadata). Each target is its own DataWeave script (own header). Typical pattern: payload = canonical JSON; variable `correlationId` = `attributes.headers['x-correlation-id'] default uuid()`; variable `recordCount` = `sizeOf(payload)`.

Do not cram side effects into `also` just to avoid a second target. Preview each target in Studio.

### 70. When is `application/java` the payload type?

**Answer:** After Java/Salesforce/JMS connectors, payload is often `Map` / `List` (`application/java`), not a JSON string. DataWeave still selects `.field` the same way. Traps: Java `null` vs DW `null`, calendar types vs `DateTime`, and **don’t** `payload as String` then `read` unless you must. Output `application/java` only when the next processor needs a Java object (e.g. some connectors). Canonical APIs should still **write JSON**.

### 71. What is `readUrl` vs `read`?

**Answer:** `read(binaryOrString, mime)` parses a value already in memory (Q19). `readUrl` loads from a URL or classpath:

```dataweave
readUrl("classpath://modules/iso-countries.json", "application/json")
```

Use for small lookup tables shipped in the app. Do not `readUrl` a huge file inside `map` (I/O per item). File connector + one Transform is cleaner for large blobs.

### 72. How do you debug DataWeave (`log`, `application/dw`)?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  seen: log("DEBUG", payload.id),
  body: payload
}
```

`log` returns the value (so it can sit inline). `output application/dw` dumps the DW view of the data (Studio/debug). **Never** log raw payloads with PII (Lab 39). `log` is not a substitute for `try` or Mule On Error.

### 73. DataWeave `try` vs Mule On Error?

**Answer:** `try` / `orElse` catch **expression** failures (bad `as Number`, divide by zero) and keep the script running. They do **not** catch HTTP 500 from a connector. Connector and flow failures use **On Error Continue / Propagate**, `error.errorType` (`HTTP:TIMEOUT`, `VALIDATION:INVALID_BOOLEAN`), `error.description`, `error.errorMessage.payload`. Interview: validation of dirty rows → `try` inside `map`; Salesforce timeout → On Error + retry.

### 74. Which HTTP `attributes` should you memorize?

**Answer:**

| Field | Use |
| --- | --- |
| `attributes.method` | GET/POST routing in DW (rare; prefer Choice) |
| `attributes.uriParams.id` | `/orders/{id}` |
| `attributes.queryParams.page` | pagination (Lab 34) |
| `attributes.headers['x-correlation-id']` | tracing |
| `attributes.statusCode` | HTTP Request **response** attributes |

Listener vs Request: know which processor produced `attributes`. Query params are often **strings** — coerce `as Number`.

### 75. Default XML namespaces, CDATA, mixed content?

**Answer:** Default `xmlns="http://acme.com/order"` still needs `ns ord http://acme.com/order` and `ord#PurchaseOrder` in DW — the prefix is yours, the URI must match. CDATA usually becomes element text. Mixed content (`<note>Pay <b>now</b></note>`) is messy; normalize with `trim` + `.*` children or refuse it in the contract. SOAP: always walk `Envelope/Body` (Lab 41).

### 76. YAML, Excel, and flat file — does DataWeave do them?

**Answer:** DataWeave is MIME-driven. `application/yaml` is supported on current runtimes. Excel (`application/xlsx`) usually needs the **Excel module** / File connector, then DW on the sheet rows. EDI / fixed-width uses **flat file** schemas (`application/flatfile`), not ad-hoc `splitBy`. Playground may not offer every MIME — say that, then: set the reader MIME and map to canonical JSON. Do not parse XLSX by splitting strings.

### 77. `dw::util::Values::mask` vs recursive mask?

**Answer:** `mask` / `update` with known **paths** is best when the schema is stable (`case .customer.ssn -> "****"`). Recursive `match` on types (Lab 39) is required when **key names** appear at unknown depth (`email`, `ssn`, `accessToken`). Interview both. Never log before masking.

### 78. Boolean operators and precedence?

**Answer:** `and`, `or`, `not` — not Java `&&` / `||` / `!`. `not` binds tightest, then `and`, then `or`. Always parenthesize mixed conditions:

```dataweave
(lower(o.status) == "paid") and ((o.amount as Number) > 0)
```

`if` without `else` is illegal — every `if` is an expression (Q12).

### 79. How do you sort by two fields (region, then amount desc)?

**Answer:** `orderBy` is one key. Descending numbers: `-o.amount`. Multi-field: a **composite key** (or sort by the less-significant key first, then the primary — only if the runtime’s `orderBy` is stable, which you should not bet on in interviews). Safer:

```dataweave
payload orderBy ((o) -> o.region ++ "|" ++ leftPad((100000000 - (o.amount as Number)) as String, 12, "0"))
```

Cleaner production: `orderBy ((o) -> o.region)` then group and sort each bucket. Name the trap: two sequential `orderBy` calls do **not** automatically mean SQL `ORDER BY a, b`.

### 80. DataWeave vs For Each vs Batch Job vs Java?

**Answer:**

| Tool | Use |
| --- | --- |
| **DataWeave** | CPU-bound mapping, no I/O, streaming-friendly `map`/`filter` |
| **For Each** | Per-item **connector** calls (accept N+1 or collection-in) |
| **Batch Job** | Large files, aggregators, per-record retries, until-successful |
| **Java** | Libraries DW cannot express (special crypto, vendor SDK) |

Anti-pattern: `lookup` or HTTP inside `map` (Q40). Anti-pattern: Batch when a single Transform + streaming would do.

---

## Quick revision checklist

- `%dw 2.0` + `output` + `---`  
- `$` / `$$`, `map` vs `mapObject` vs `pluck`  
- `default` vs `?` vs `try`  
- `++` for string/array/object  
- Dynamic keys `(expr): value`  
- `update`, `do`, `match`  
- Modules: Strings, Arrays, Objects, Dates, Crypto, Runtime  
- XML `@attr`, `.*child`, `ns0#Element`, SOAP Envelope/Body  
- Streaming vs `groupBy`/`orderBy`/`sizeOf`  
- No N+1 `lookup` inside `map`  
- `maxBy` / `firstWith` / `zip` / ranges  
- Timezones (`>> "UTC"`), `readUrl`, TM multiple targets  
- `try` vs Mule On Error; never log PII  
- DW vs For Each vs Batch vs Java  

## Suggested practice prompts (whiteboard)

1. Convert nested JSON orders → CSV of line items.  
2. Group employees by department and compute average salary.  
3. Deep-merge two configs with array concatenation rules.  
4. Mask any key named `ssn` at any depth.  
5. Left-join orders to customers without `leftJoin` (use `groupBy`).  

---

*Aligned with Mule 4 and DataWeave 2.x. Confirm runtime version (4.3+ for `update`, newer cores for extra `dw::core::Arrays` helpers) for the job you are interviewing for.*
