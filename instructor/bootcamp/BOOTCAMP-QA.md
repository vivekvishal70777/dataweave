# Interview bootcamp — Set B (answers)

Use this **only while recording** the last Udemy section. Same 80 skills as the course bank,
new wording so students cannot recite the Section 2–12 questions from memory.

**Do not zip this file into the student pack.** Students get `student/resources/bootcamp-prompts.md`.

Course twins: each answer ends with `Course twin: Qn` (the teaching-bank number).

---

## Easy (B1–B20)

### B1. In one sentence, what problem does DataWeave solve in a Mule 4 API?

**Answer:** It turns one payload shape into another (JSON, XML, CSV, Java). You write it in Transform Message and in `#[...]`. It is not Java and not MEL.

Course twin: Q1.

### B2. A teammate still writes `%dw 1.0` and `%output`. What do you change for Mule 4, and why would an interviewer care?

**Answer:** Header becomes `%dw 2.0`. Output becomes `output application/json` (no `%output`). Mule 4 uses DataWeave in `#[...]` instead of MEL. Interviews almost always want **2.0**.

| Old (Mule 3) | New (Mule 4) |
| --- | --- |
| `%dw 1.0` | `%dw 2.0` |
| MEL + DW | DW everywhere |
| `%output ...` | `output ...` |

Course twin: Q2.

### B3. Walk me through a hello-world script that greets `payload.customerName`. Name the three parts.

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{ hello: "Hi " ++ payload.customerName }
```

Header (version, output, vars/funs), `---`, then the body that becomes the payload.

Course twin: Q3.

### B4. You need a GST rate of 18% used in several fields. How do you store it, and can you change it later in the same script?

**Answer:** `var gst = 0.18` in the header (or inside `do`). Variables are **immutable** — you do not reassign. Comments: `//` and `/* */`.

```dataweave
%dw 2.0
output application/json
var gst = 0.18
---
{ gross: payload.net * (1 + gst) }
```

Course twin: Q4.

### B5. Write a small `fun` that builds `sku + "-" + plant` with types on the arguments.

**Answer:**

```dataweave
%dw 2.0
output application/json
fun plantSku(sku: String, plant: String): String = sku ++ "-" ++ plant
---
plantSku(payload.sku, payload.plant)
```

You can overload by types. Prefer annotations in modules.

Course twin: Q5.

### B6. Name at least eight DataWeave types you would list on a whiteboard.

**Answer:** `String`, `Boolean`, `Number`, `Date`, `DateTime`, `LocalDateTime`, `Time`, `Period`, `Regex`, `Array`, `Object`, `Null`, `Binary`, `Type`, `Any`. Capital letters. `Any` means you did not specify.

```dataweave
fun gst(n: Number): Number = n * 1.18
```

Course twin: Q6.

### B7. The ERP sends `"qty": "12"`. How do you make it a number, and what if the text is garbage?

**Answer:** `payload.qty as Number`. Dates need `{format: "yyyy-MM-dd"}`. Failed `as` throws — wrap with `try` / `orElse`. `default` does **not** catch conversion errors.

Course twin: Q7.

### B8. You have a list of shipments. Keep only `IN_TRANSIT`, then output `{ awb, dest }`. Which operator runs first?

**Answer:** `filter` first (smaller list), then `map` (new shape). Predicate must be `true` to keep a row.

```dataweave
payload.shipments
  filter ((s) -> s.status == "IN_TRANSIT")
  map ((s) -> { awb: s.awb, dest: s.destination })
```

Course twin: Q8.

### B9. A config object `{ host, port, tls }` must become an array of `{ name, value }`. Which function, and why not `map`?

**Answer:** `pluck` walks an **object** and returns an **array**. `map` walks arrays.

```dataweave
payload.pluck ((v, k) -> { name: k, value: v })
```

Course twin: Q9.

### B10. What is wrong with `payload.first ++ payload.last` vs `payload.qty + payload.bonus`? When do you use `++` on objects?

**Answer:** `++` joins strings and arrays. `+` adds numbers. `++` on objects is a **shallow** merge; right-hand key wins. Do not use `+` on strings.

Course twin: Q10.

### B11. `payload.account.iban` is sometimes missing. How do you avoid a crash, and when is `default` the wrong tool?

**Answer:** `payload.account.iban default ""` or `payload.account.?iban`. `default` replaces null. It does **not** catch `as Number` failures — that is `try`.

Course twin: Q11.

### B12. Classify `payload.score` as `"gold"` / `"silver"` / `"bronze"` with a DataWeave `if`. Why is `score > 90 ? "gold" : "silver"` wrong?

**Answer:** DataWeave has no Java ternary. Every `if` needs `else` because it is an expression.

```dataweave
if (payload.score >= 90) "gold"
else if (payload.score >= 70) "silver"
else "bronze"
```

Course twin: Q12.

### B13. When do you write `payload."item-code"`, `payload[2]`, `payload.*Line`, and `payload..gstin`?

**Answer:**

- `.name` — normal key
- `["item-code"]` — hyphen / reserved key
- `[2]` — array index (0-based)
- `.*Line` — all repeating children (XML)
- `..gstin` — that field at any depth

Course twin: Q13.

### B14. Turn a JSON array of plants into XML. What breaks if you forget a single root?

**Answer:** `output application/xml` and wrap in one root, e.g. `plants: { plant: payload map { code: $.code } }`. XML writers need **one root**. Reverse: `output application/json` and `payload.plants.plant.@code` for attributes.

Course twin: Q14.

### B15. You need to know if `payload.batches` has rows. Compare `sizeOf` and `isEmpty`. Which phrase do you use in an interview?

**Answer:** `sizeOf` is length (array, object keys, or string). `isEmpty` is true for `[]`, `{}`, `""`, and often null. Say **prefer `isEmpty`** over `sizeOf(x) == 0`.

Course twin: Q15.

### B16. Split a pipe-separated plant list, join SKUs with commas, and uppercase a material name. Which module?

**Answer:** `dw::core::Strings`: `splitBy`, `joinBy`, `upper` / `lower` / `capitalize`, plus `trim`, `substringBefore`, `replace`.

```dataweave
import * from dw::core::Strings
---
{
  plants: payload.list splitBy "|",
  skus: payload.skus joinBy ",",
  mat: upper(payload.material)
}
```

Course twin: Q16.

### B17. In Transform Message, where do you read a flow variable `plant`, a query param `page`, and a property `sap.host`?

**Answer:** `vars.plant`, `attributes.queryParams.page`, `p("sap.host")` (or `Mule::p`). Also `attributes.headers['authorization']`, `attributes.uriParams.id`. `error.*` belongs in On Error scopes.

Course twin: Q17.

### B18. When is a Set Payload `#[payload.awb]` enough, and when must you open Transform Message?

**Answer:** `#[...]` is one expression. Transform Message is a full script: header, preview, several targets (payload + vars). Fat mappings belong in Transform Message.

Course twin: Q18.

### B19. A CSV column holds a JSON **string**. How do you parse it without changing the script’s `output` MIME? How do you log a compact JSON snapshot?

**Answer:** `read(payload.jsonColumn, "application/json")` and `write(payload.row, "application/json", { indent: false })`. That is **not** the same as `output application/json` on the script. Huge `write(payload)` can break streaming.

Course twin: Q19.

### B20. You do not want `null` IBAN fields in the JSON response. Which writer property, and name two others (CSV / compact JSON)?

**Answer:** `output application/json skipNullOn="everywhere"`. Also `indent=false`, CSV `header=true, separator=","`, XML `duplicateKeyAsArray=true`.

Course twin: Q20.


---

## Moderate (B21–B40)

### B21. Uppercase every **key** on `{ plant: "P001", qty: 2 }` and keep object shape. Why is `map` the wrong first choice?

**Answer:** `map` returns an array. `mapObject` returns an object.

```dataweave
payload mapObject ((v, k) -> { (upper(k as String)): v })
```

Course twin: Q21.

### B22. From a list of invoices, group by `plant`, sort by `docDate`, and unique by `vendorGstin`. What type does `groupBy` return?

**Answer:** `groupBy` → **object** of arrays. `orderBy` sorts. `distinctBy` keeps the **first** match.

```dataweave
{
  byPlant: payload groupBy $.plant,
  byDate: payload orderBy $.docDate,
  vendors: payload distinctBy $.vendorGstin
}
```

Course twin: Q22.

### B23. Sum `payload.lines.amount` with `reduce`, then also build `{ sku: qty }` with `reduce`. What if you omit the seed?

**Answer:**

```dataweave
payload.lines reduce ((l, acc = 0) -> acc + (l.amount as Number))
payload.lines reduce ((l, acc = {}) -> acc ++ { (l.sku): l.qty })
```

No seed → first item is the accumulator; iteration starts at the second item.

Course twin: Q23.

### B24. `[["A"], ["B","C"]]` should become `["A","B","C"]`. Is `flatten` enough for a 3-level tree?

**Answer:** `flatten` is **one** level. Deeper trees need recursion or repeated flatten. Lab 15 is one level; Lab 37 is deep.

Course twin: Q24.

### B25. `{ tax: { cgst: 9 } } ++ { tax: { sgst: 9 } }` — what is in `tax` after the merge? How do you deep-merge?

**Answer:** Shallow `++`: `tax` becomes **only** `{ sgst: 9 }` (right wins the whole nested object). Deep merge: `import mergeWith from dw::core::Objects`. Drop keys with `payload - "password"`.

Course twin: Q25.

### B26. Uppercase `payload.vendor.address.city` without rewriting the whole vendor object. Which operator and which Mule version?

**Answer:** `update` (DW 2.3 / Mule **4.3+**):

```dataweave
payload update {
  case .vendor.address.city -> upper($)
}
```

Course twin: Q26.

### B27. Inside `map` over invoices you need a local `var tds`. Why put it in a `do` block instead of the header?

**Answer:** `do` is a local scope so the header stays small.

```dataweave
payload map (inv) -> do {
  var tds = (inv.amount as Number) * 0.01
  ---
  { id: inv.id, net: (inv.amount as Number) - tds }
}
```

Course twin: Q27.

### B28. Map SAP status `A` / `B` / anything starting with `E` / a Number / else. Show a `match`.

**Answer:**

```dataweave
payload.stat match {
  case "A" -> "open"
  case "B" -> "posted"
  case s if s startsWith "E" -> "error"
  case n is Number -> "numeric"
  else -> "other"
}
```

Literals, `is` types, `if` guards, `else`.

Course twin: Q28.

### B29. `payload.rate` is the string `"N/A"`. How do you coerce to Number without failing the whole script? Is this a Mule HTTP error handler?

**Answer:** `try(() -> payload.rate as Number) orElse 0`. Catches **script** failures only, not connector HTTP 500 (that is On Error).

Course twin: Q29.

### B30. Format today as `dd-MMM-yyyy`, parse `20-08-2026`, add seven days. Why is `now()` risky inside a pricing module?

**Answer:** `now() as String {format: "dd-MMM-yyyy"}`, `"20-08-2026" as Date {format: "dd-MM-yyyy"}`, `(now() as Date) + |P7D|`. Inject `asOf` into modules so tests are deterministic. Shift zones with `>> "Asia/Kolkata"`.

Course twin: Q30.

### B31. Finance sends CSV with header `Vendor,Amount` and semicolon separators. How do you get JSON numbers?

**Answer:** Reader MIME `application/csv` with `header=true, separator=";"`. Body: `payload map { vendor: $.Vendor, amount: $.Amount as Number }`. CSV arrives as an **array of objects**.

Course twin: Q31.

### B32. Export invoices to CSV with columns `Doc` and `Gross`. How do headers appear?

**Answer:** `output application/csv header=true` and map to those exact keys. Keys become the header row.

Course twin: Q32.

### B33. XML `<Delivery id="D1"><Item>X</Item><Item>Y</Item></Delivery>`. How do you read `id` vs items vs write an attribute?

**Answer:** Read: `payload.Delivery.@id`, `payload.Delivery.*Item`. Write: `Delivery @(id: payload.id): { Item: payload.sku }`.

Course twin: Q33.

### B34. Show three `import` styles (star from Strings, one function from your module, Arrays as a prefix).

**Answer:**

```dataweave
import * from dw::core::Strings
import withTax from modules::Pricing
import dw::core::Arrays
---
Arrays.drop(payload, 1)
```

Custom modules: `src/main/resources/modules/*.dwl`.

Course twin: Q34.

### B35. In `payload map { n: $$ + 1, v: $ }`, what are `$` and `$$`? When do you use `$$$`? What do you say if the interviewer hates dollars?

**Answer:** `$` = item, `$$` = 0-based index (or key in some object functions), `$$$` = third arg in `mapObject`/`pluck`. Prefer named `(row, idx) ->`.

Course twin: Q35.

### B36. Drop keys `iban`, `pan`, `password` from an unknown object of secrets. Which function?

**Answer:** `filterObject ((v, k) -> !( ["iban","pan","password"] contains lower(k as String) ))`. Known paths can use `mask` / `update`.

Course twin: Q36.

### B37. Join `payload.deliveries` to `payload.plants` on `plantCode` / `code` like SQL LEFT JOIN. What does each result row look like?

**Answer:** `import * from dw::core::Arrays` then `leftJoin(deliveries, plants, (d) -> d.plantCode, (p) -> p.code)`. Rows are `{ l: ..., r: ... }`. Also `join` / `outerJoin`. Or `groupBy` plus index (Lab 32).

Course twin: Q37.

### B38. You need a UUID. Show a Java call. When do you refuse to call Java from DataWeave?

**Answer:** `import java!java::util::UUID` then `UUID::randomUUID() as String`. Refuse Java for normal mapping, inside every `map` iteration, or when streaming matters. Prefer DW; Java is for libraries DW cannot do.

Course twin: Q38.

### B39. `"INV-4401"` — contrast `startsWith "INV"`, `contains "440"`, and `matches /INV-[0-9]+/`.

**Answer:** `startsWith` = prefix. `contains` = substring or array membership. `matches` = **whole string** regex. Partial regex: `find` / `scan`.

Course twin: Q39.

### B40. Why is `lookup("get-plant", { id: $.plant })` inside `map` a red flag? What do you do instead?

**Answer:** N+1 synchronous flow calls. Fetch plants **once**, `groupBy` code, then map. Config: `p()`. Do not hide HTTP inside Transform Message.

Course twin: Q40.


---

## Hard (B41–B60)

### B41. A 2 GB CSV must become JSON lines. Which DW operations destroy streaming?

**Answer:** Streaming works for one-pass `map`/`filter`. It **breaks** with `sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, `reduce` on the whole file, touching payload twice, random index, or `payload as String`.

Course twin: Q41.

### B42. Write `fun leaves(x)` that returns every primitive in a mixed JSON tree (objects + arrays).

**Answer:**

```dataweave
fun leaves(x) =
  x match {
    case a is Array -> a flatMap leaves($)
    case o is Object -> leaves(valuesOf(o))
    else -> [x]
  }
```

`match` on types + recursion. Course twin: Q42.

### B43. Each delivery has `packages[]`. You need one output row per package with `awb` copied down. Name the operator.

**Answer:** `flatMap` (map then flatten one level):

```dataweave
payload.deliveries flatMap ((d) ->
  d.packages map (p) -> { awb: d.awb, pkg: p.id }
)
```

Same as `flatten(payload.deliveries map ...)`. Course twin: Q43.

### B44. SOAP body uses `xmlns:del="http://logistics.example/del"`. How do you **write** `del:Shipment` with an `id` attribute?

**Answer:**

```dataweave
ns del http://logistics.example/del
output application/xml
---
del#Shipment @(id: payload.id): {
  del#Awb: payload.awb
}
```

Prefix is yours; **URI must match**. Read with `payload.del#Shipment`. Course twin: Q44.

### B45. Webhook vs file checksum: when `hashWith` vs `HMACBinary`? What type is the payload?

**Answer:** Hash = one-way integrity (`SHA-256`). HMAC = shared secret (webhooks). Both want **Binary**. Then often `toBase64`. Do not invent your own encoding.

Course twin: Q45.

### B46. Sketch `modules/Money.dwl` with `fun rupees(n)` and how you import it. What must stay out of a pure module?

**Answer:** File under `src/main/resources/modules`. `fun rupees(n: Number) = n as String {format: "0.00"} as Number`. `import rupees from modules::Money`. No `lookup`, no `now()` — inject time and data.

Course twin: Q46.

### B47. For `{ gstin: "...", pan: "..." }`, contrast `keysOf`, `namesOf`, `valuesOf`, `entriesOf`.

**Answer:** `keysOf` → Key types (XML-aware). `namesOf` → Strings (usual JSON). `valuesOf` → values array. `entriesOf` → `{key, value}` array.

Course twin: Q47.

### B48. `payload.pairs` is `[{ code: "P1", qty: 2 }]`. Build `{ P1: 2 }` with a **dynamic** key. What happens without parentheses?

**Answer:**

```dataweave
payload.pairs reduce ((p, acc = {}) -> acc ++ { (p.code): p.qty })
```

Without `(p.code)` the key is the literal string `p.code`.

Course twin: Q48.

### B49. `vars.before` and `payload` are two flat invoice objects. List fields that changed (`field`, `from`, `to`).

**Answer:** `namesOf(payload) filter ((k) -> vars.before[k] != payload[k]) map (k) -> { field: k, from: vars.before[k], to: payload[k] }`. Nested: recursive `match`. Mention `dw::util::Diff::diff` if the runtime has it.

Course twin: Q49.

### B50. Overload `fun label` for String, Number, Array, and Any. Who wins?

**Answer:** Most **specific** signature wins.

```dataweave
fun label(x: String) = "s"
fun label(x: Number) = "n"
fun label(x: Array) = "a"
fun label(x: Any) = "?"
```

Same idea as `match { case x is Date -> }`.

Course twin: Q50.

### B51. Invoice dates arrive as `yyyy-MM-dd` **or** `dd/MM/yyyy`. Write a robust `fun parseInv`.

**Answer:** `try` + `orElseTry` + `orElse null` (or fail the row). Set `{format: ...}` each time. Locale if months are names. Business decides null vs reject.

Course twin: Q51.

### B52. You receive a Base64 PDF in `vars.pdfB64`. How do you get Binary, and how do you encode Binary to Base64? Multipart?

**Answer:** `import * from dw::core::Binaries` — `fromBase64` / `toBase64`. Multipart: `payload.parts.file.content`. Do not load huge files as String. Output `application/octet-stream` when it must stay binary.

Course twin: Q52.

### B53. Name two reader/writer knobs each for JSON, XML, and CSV.

**Answer:** JSON: `streaming`, `indent`, `skipNullOn`, `duplicateKeyAsArray`. XML: `encoding`, `writeDeclaration`, `ignoreRootElement`. CSV: `header`, `separator`, `quote`, `ignoreEmptyLine`. Incoming MIME often holds **reader** props.

Course twin: Q53.

### B54. `vars.page` and `vars.size` paginate `payload`. Write `drop` / `take`. Name `divideBy`.

**Answer:** `payload drop ((vars.page default 1) - 1) * (vars.size default 20) take (vars.size default 20)`. `divideBy(payload, 200)` chunks for Salesforce composite. May still load the array into memory.

Course twin: Q54.

### B55. CDC list has duplicate `gstin`; **last** row should win. Why is `distinctBy` alone wrong?

**Answer:** `distinctBy` keeps **first**. Last-wins: `reduce` into object keyed by `gstin`, then `valuesOf`. Or reverse, distinctBy, reverse.

Course twin: Q55.

### B56. After `filter`, you want `{ count, rows }` without a header `var`. Show `then`. What does `also` return?

**Answer:** `payload.rows filter $.ok then (rows) -> { count: sizeOf(rows), rows: rows }`. `also` returns the **original** left value. Prefer `do` if the chain gets cute.

Course twin: Q56.

### B57. Mask any key named `pan`, `aadhaar`, or `iban` at unknown depth. Sketch `fun redact`.

**Answer:** Recursive `match`: Object → `mapObject` and replace if key in the list; Array → `map redact($)`; else keep. Known paths: `update` / `Values::mask`. Never `log` before redact.

Course twin: Q57.

### B58. List six performance answers an interviewer wants, including money and I/O.

**Answer:** `groupBy`/`orderBy` on huge arrays; nested map/filter O(n²); `lookup` inside `map`; `payload as String`; `..` on fat XML; breaking streaming; deep recursion; Java HashMap of the whole file; float money without `fun money`; HTTP inside Transform. Fix: index once with `groupBy`, coerce once, mask before log.

Course twin: Q58.

### B59. Write `fun twice(x, f)` that applies `f` two times. Call it with `upper` and with a lambda. What is a higher-order function?

**Answer:** A function that takes or returns a function. `map`/`filter`/`reduce` already are.

```dataweave
fun twice(x, f) = f(f(x))
---
{ a: twice("ab", upper), b: twice(2, (n) -> n * 3) }
```

Course twin: Q59.

### B60. Talk through SAP IDoc XML → canonical invoice JSON in eight beats (no long script).

**Answer:** 1) Reader: `ns`, IDoc/segment, `*E1EDP01`, `@`. 2) Types: `as Number`, date formats. 3) `fun money` / `do` line totals. 4) Customer from `vars` already fetched — no `lookup` per line. 5) Shape `invoiceId`, `currency`, `lines`. 6) `skipNullOn="everywhere"`. 7) `try` on bad price. 8) One-pass `map`, no `orderBy` unless the API sorts. Same design as course Q60 / Labs 41 and 54.

Course twin: Q60.


---

## Industry / Mule message (B61–B80)

### B61. Besides `map`/`filter`, name `maxBy`, `firstWith`, `some`, `every`, `countBy`. What does `maxBy` return?

**Answer:** Import `dw::core::Arrays`. `maxBy` / `minBy` return the **item**, not the number. Guard empty arrays. `firstWith` = first match. `indexOf`, `countBy`.

Course twin: Q61.

### B62. What is `payload[0 to 2]` vs `slice(payload, 1, 4)` vs `1 to 5`?

**Answer:** `[0 to 2]` inclusive indexes. `1 to 5` is a range array. `slice` / `take` / `drop` for production. Out-of-range is usually safer than Java — still do not rely on it.

Course twin: Q62.

### B63. `payload.cols` and `payload.cells` are same-length arrays. Zip them into `{ name, value }` objects, then into one object.

**Answer:** `import zip from dw::core::Arrays`. `zip(cols, cells) map { name: $[0], value: $[1] }` then reduce with `(pair[0]): pair[1]`. Length = shorter array.

Course twin: Q63.

### B64. How do you ask “is this an Array?” without Java `instanceof`?

**Answer:** `payload is Array`, `payload.amount is Number`, `typeOf(payload)`. Trees: `match { case x is Object -> }`.

Course twin: Q64.

### B65. Name number helpers plus how you round INR to 2 decimals without `BigDecimal`.

**Answer:** `sum`, `avg`, `min`, `max`, `mod`, `abs`, `ceil`, `floor`, `round`. Money: `n as String {format: "0.00"} as Number` (`fun rupees`). Coerce ERP strings first. `sum([])` needs a guard.

Course twin: Q65.

### B66. `payload.postedAt` is ISO-8601. Show UTC and IST display. What do you store in the canonical API?

**Answer:** `ts as DateTime >> "UTC"` and `>> "Asia/Kolkata"`. Store **UTC**; convert at the edge. `LocalDateTime` has no offset.

Course twin: Q66.

### B67. Invoice due date is start + 1 month. Days between two dates? Start of that day?

**Answer:** `dw::core::Dates`: `daysBetween`, `atBeginningOfDay`. `(d as Date) + |P1M|`. Periods `|P7D|`, `|PT2H|`.

Course twin: Q67.

### B68. Redact `INV-\d+` in notes, extract those ids, and take the SKU family before `-`.

**Answer:** `replace` with regex, `find` / `scan` to extract, `substringBefore(sku, "-")`, `trim`. `matches` is full-string only.

Course twin: Q68.

### B69. One Transform Message must set JSON payload **and** variable `docCount`. How?

**Answer:** Two **targets**, two scripts (each with a header). Payload = body. Variable `docCount` = `sizeOf(payload)`. Do not abuse `also` for that. Preview each target.

Course twin: Q69.

### B70. After a Salesforce connector the MIME is `application/java`. Do you `read` it as JSON? When do you **output** Java?

**Answer:** Select `.Name` as usual on Map/List. Do not `as String` + `read` unless you must. Output Java only if the **next** connector needs a Java object. APIs still write JSON.

Course twin: Q70.

### B71. Plant codes live in `classpath://modules/plants.json`. `read` or `readUrl`? When is File connector better?

**Answer:** `readUrl("classpath://modules/plants.json", "application/json")` for small tables. `read` is in-memory. Do not `readUrl` inside `map`. Large files: File connector + one Transform.

Course twin: Q71.

### B72. How do you log `payload.docId` inline, dump DW preview, and still not leak PAN?

**Answer:** `log("DEBUG", payload.docId)` returns the value. `output application/dw` for Studio. Never log raw PII (Lab 39). `log` is not `try` or On Error.

Course twin: Q72.

### B73. Dirty `qty` vs HTTP 504 from SAP — which is DataWeave `try`, which is On Error?

**Answer:** `try` = expression (`as Number`, /0). On Error = connector/flow (`HTTP:TIMEOUT`, `error.errorMessage.payload`). Dirty rows: `try` inside `map`. Timeout: On Error + retry.

Course twin: Q73.

### B74. Memorize five HTTP `attributes` fields and say Listener vs Request.

**Answer:** `method`, `uriParams.id`, `queryParams.page` (often **String**), `headers['x-correlation-id']`, `statusCode` on **Request response**. Know which processor wrote `attributes`.

Course twin: Q74.

### B75. Default `xmlns="http://sap.example/idoc"` with no prefix on the XML. How do you select the root in DW? CDATA? Mixed content?

**Answer:** You still declare `ns idoc http://sap.example/idoc` and use `idoc#ORDERS05` — URI must match. CDATA ≈ text. Mixed content: `trim` + `.*` or reject in the contract. SOAP: Envelope/Body first.

Course twin: Q75.

### B76. Can DW read YAML, Excel, and EDI flat file in the Playground?

**Answer:** MIME-driven. YAML often yes. Excel usually **Excel module** / File then DW on rows. EDI/fixed width = `application/flatfile` schema, not `splitBy`. Say Playground may lack a MIME.

Course twin: Q76.

### B77. When is `Values::mask` enough, and when must you recurse like Lab 39?

**Answer:** Mask/`update` for **known paths**. Recurse when `pan`/`email` appear at unknown depth. Interview both. Log after mask.

Course twin: Q77.

### B78. Rewrite Java `status.equals("OPEN") && qty > 0` in DataWeave. Precedence of `not` / `and` / `or`?

**Answer:** `and` `or` `not` — no `&&`. `not` tightest, then `and`, then `or`. Parenthesize. `if` always has `else`.

```dataweave
(upper(o.status) == "OPEN") and ((o.qty as Number) > 0)
```

Course twin: Q78.

### B79. Sort plants by `region` A–Z, then `amount` descending. Why is `orderBy` then `orderBy` a trap?

**Answer:** One `orderBy` = one key. Desc numbers: `-o.amount`. Two calls are **not** SQL `ORDER BY a, b` unless you bet on stability (do not). Composite key or group-then-sort.

Course twin: Q79.

### B80. A 50k-line invoice file needs mapping, and some rows call SAP. DW, For Each, Batch, or Java — pick and say why.

**Answer:** DW = CPU map, streaming. For Each = connector per item. Batch = huge file + per-record retry. Java = vendor SDK / crypto DW cannot do. Anti-pattern: HTTP inside `map`.

Course twin: Q80.

