# Interview bootcamp prompts — Set B (no answers)

These 80 questions test the **same skills** as the course, with **new wording**.
They are not a copy of the articles you already read.

**Answers are not in this file.** Speak 45–90 seconds, then resume the mock-interview video.

1. Read one prompt.
2. Pause.
3. Speak (hard questions: up to 3 minutes + a tiny script).
4. Play the model answer on the video, or replay the matching *concept* lecture from earlier sections.

---

## Easy (B1–B20)

### B1. In one sentence, what problem does DataWeave solve in a Mule 4 API?

_Speak, then check the video._

### B2. A teammate still writes `%dw 1.0` and `%output`. What do you change for Mule 4, and why would an interviewer care?

_Speak, then check the video._

### B3. Walk me through a hello-world script that greets `payload.customerName`. Name the three parts.

_Speak, then check the video._

### B4. You need a GST rate of 18% used in several fields. How do you store it, and can you change it later in the same script?

_Speak, then check the video._

### B5. Write a small `fun` that builds `sku + "-" + plant` with types on the arguments.

_Speak, then check the video._

### B6. Name at least eight DataWeave types you would list on a whiteboard.

_Speak, then check the video._

### B7. The ERP sends `"qty": "12"`. How do you make it a number, and what if the text is garbage?

_Speak, then check the video._

### B8. You have a list of shipments. Keep only `IN_TRANSIT`, then output `{ awb, dest }`. Which operator runs first?

_Speak, then check the video._

### B9. A config object `{ host, port, tls }` must become an array of `{ name, value }`. Which function, and why not `map`?

_Speak, then check the video._

### B10. What is wrong with `payload.first ++ payload.last` vs `payload.qty + payload.bonus`? When do you use `++` on objects?

_Speak, then check the video._

### B11. `payload.account.iban` is sometimes missing. How do you avoid a crash, and when is `default` the wrong tool?

_Speak, then check the video._

### B12. Classify `payload.score` as `"gold"` / `"silver"` / `"bronze"` with a DataWeave `if`. Why is `score > 90 ? "gold" : "silver"` wrong?

_Speak, then check the video._

### B13. When do you write `payload."item-code"`, `payload[2]`, `payload.*Line`, and `payload..gstin`?

_Speak, then check the video._

### B14. Turn a JSON array of plants into XML. What breaks if you forget a single root?

_Speak, then check the video._

### B15. You need to know if `payload.batches` has rows. Compare `sizeOf` and `isEmpty`. Which phrase do you use in an interview?

_Speak, then check the video._

### B16. Split a pipe-separated plant list, join SKUs with commas, and uppercase a material name. Which module?

_Speak, then check the video._

### B17. In Transform Message, where do you read a flow variable `plant`, a query param `page`, and a property `sap.host`?

_Speak, then check the video._

### B18. When is a Set Payload `#[payload.awb]` enough, and when must you open Transform Message?

_Speak, then check the video._

### B19. A CSV column holds a JSON **string**. How do you parse it without changing the script’s `output` MIME? How do you log a compact JSON snapshot?

_Speak, then check the video._

### B20. You do not want `null` IBAN fields in the JSON response. Which writer property, and name two others (CSV / compact JSON)?

_Speak, then check the video._


---

## Moderate (B21–B40)

### B21. Uppercase every **key** on `{ plant: "P001", qty: 2 }` and keep object shape. Why is `map` the wrong first choice?

_Speak, then check the video._

### B22. From a list of invoices, group by `plant`, sort by `docDate`, and unique by `vendorGstin`. What type does `groupBy` return?

_Speak, then check the video._

### B23. Sum `payload.lines.amount` with `reduce`, then also build `{ sku: qty }` with `reduce`. What if you omit the seed?

_Speak, then check the video._

### B24. `[["A"], ["B","C"]]` should become `["A","B","C"]`. Is `flatten` enough for a 3-level tree?

_Speak, then check the video._

### B25. `{ tax: { cgst: 9 } } ++ { tax: { sgst: 9 } }` — what is in `tax` after the merge? How do you deep-merge?

_Speak, then check the video._

### B26. Uppercase `payload.vendor.address.city` without rewriting the whole vendor object. Which operator and which Mule version?

_Speak, then check the video._

### B27. Inside `map` over invoices you need a local `var tds`. Why put it in a `do` block instead of the header?

_Speak, then check the video._

### B28. Map SAP status `A` / `B` / anything starting with `E` / a Number / else. Show a `match`.

_Speak, then check the video._

### B29. `payload.rate` is the string `"N/A"`. How do you coerce to Number without failing the whole script? Is this a Mule HTTP error handler?

_Speak, then check the video._

### B30. Format today as `dd-MMM-yyyy`, parse `20-08-2026`, add seven days. Why is `now()` risky inside a pricing module?

_Speak, then check the video._

### B31. Finance sends CSV with header `Vendor,Amount` and semicolon separators. How do you get JSON numbers?

_Speak, then check the video._

### B32. Export invoices to CSV with columns `Doc` and `Gross`. How do headers appear?

_Speak, then check the video._

### B33. XML `<Delivery id="D1"><Item>X</Item><Item>Y</Item></Delivery>`. How do you read `id` vs items vs write an attribute?

_Speak, then check the video._

### B34. Show three `import` styles (star from Strings, one function from your module, Arrays as a prefix).

_Speak, then check the video._

### B35. In `payload map { n: $$ + 1, v: $ }`, what are `$` and `$$`? When do you use `$$$`? What do you say if the interviewer hates dollars?

_Speak, then check the video._

### B36. Drop keys `iban`, `pan`, `password` from an unknown object of secrets. Which function?

_Speak, then check the video._

### B37. Join `payload.deliveries` to `payload.plants` on `plantCode` / `code` like SQL LEFT JOIN. What does each result row look like?

_Speak, then check the video._

### B38. You need a UUID. Show a Java call. When do you refuse to call Java from DataWeave?

_Speak, then check the video._

### B39. `"INV-4401"` — contrast `startsWith "INV"`, `contains "440"`, and `matches /INV-[0-9]+/`.

_Speak, then check the video._

### B40. Why is `lookup("get-plant", { id: $.plant })` inside `map` a red flag? What do you do instead?

_Speak, then check the video._


---

## Hard (B41–B60)

### B41. A 2 GB CSV must become JSON lines. Which DW operations destroy streaming?

_Speak, then check the video._

### B42. Write `fun leaves(x)` that returns every primitive in a mixed JSON tree (objects + arrays).

_Speak, then check the video._

### B43. Each delivery has `packages[]`. You need one output row per package with `awb` copied down. Name the operator.

_Speak, then check the video._

### B44. SOAP body uses `xmlns:del="http://logistics.example/del"`. How do you **write** `del:Shipment` with an `id` attribute?

_Speak, then check the video._

### B45. Webhook vs file checksum: when `hashWith` vs `HMACBinary`? What type is the payload?

_Speak, then check the video._

### B46. Sketch `modules/Money.dwl` with `fun rupees(n)` and how you import it. What must stay out of a pure module?

_Speak, then check the video._

### B47. For `{ gstin: "...", pan: "..." }`, contrast `keysOf`, `namesOf`, `valuesOf`, `entriesOf`.

_Speak, then check the video._

### B48. `payload.pairs` is `[{ code: "P1", qty: 2 }]`. Build `{ P1: 2 }` with a **dynamic** key. What happens without parentheses?

_Speak, then check the video._

### B49. `vars.before` and `payload` are two flat invoice objects. List fields that changed (`field`, `from`, `to`).

_Speak, then check the video._

### B50. Overload `fun label` for String, Number, Array, and Any. Who wins?

_Speak, then check the video._

### B51. Invoice dates arrive as `yyyy-MM-dd` **or** `dd/MM/yyyy`. Write a robust `fun parseInv`.

_Speak, then check the video._

### B52. You receive a Base64 PDF in `vars.pdfB64`. How do you get Binary, and how do you encode Binary to Base64? Multipart?

_Speak, then check the video._

### B53. Name two reader/writer knobs each for JSON, XML, and CSV.

_Speak, then check the video._

### B54. `vars.page` and `vars.size` paginate `payload`. Write `drop` / `take`. Name `divideBy`.

_Speak, then check the video._

### B55. CDC list has duplicate `gstin`; **last** row should win. Why is `distinctBy` alone wrong?

_Speak, then check the video._

### B56. After `filter`, you want `{ count, rows }` without a header `var`. Show `then`. What does `also` return?

_Speak, then check the video._

### B57. Mask any key named `pan`, `aadhaar`, or `iban` at unknown depth. Sketch `fun redact`.

_Speak, then check the video._

### B58. List six performance answers an interviewer wants, including money and I/O.

_Speak, then check the video._

### B59. Write `fun twice(x, f)` that applies `f` two times. Call it with `upper` and with a lambda. What is a higher-order function?

_Speak, then check the video._

### B60. Talk through SAP IDoc XML → canonical invoice JSON in eight beats (no long script).

_Speak, then check the video._


---

## Industry / Mule message (B61–B80)

### B61. Besides `map`/`filter`, name `maxBy`, `firstWith`, `some`, `every`, `countBy`. What does `maxBy` return?

_Speak, then check the video._

### B62. What is `payload[0 to 2]` vs `slice(payload, 1, 4)` vs `1 to 5`?

_Speak, then check the video._

### B63. `payload.cols` and `payload.cells` are same-length arrays. Zip them into `{ name, value }` objects, then into one object.

_Speak, then check the video._

### B64. How do you ask “is this an Array?” without Java `instanceof`?

_Speak, then check the video._

### B65. Name number helpers plus how you round INR to 2 decimals without `BigDecimal`.

_Speak, then check the video._

### B66. `payload.postedAt` is ISO-8601. Show UTC and IST display. What do you store in the canonical API?

_Speak, then check the video._

### B67. Invoice due date is start + 1 month. Days between two dates? Start of that day?

_Speak, then check the video._

### B68. Redact `INV-\d+` in notes, extract those ids, and take the SKU family before `-`.

_Speak, then check the video._

### B69. One Transform Message must set JSON payload **and** variable `docCount`. How?

_Speak, then check the video._

### B70. After a Salesforce connector the MIME is `application/java`. Do you `read` it as JSON? When do you **output** Java?

_Speak, then check the video._

### B71. Plant codes live in `classpath://modules/plants.json`. `read` or `readUrl`? When is File connector better?

_Speak, then check the video._

### B72. How do you log `payload.docId` inline, dump DW preview, and still not leak PAN?

_Speak, then check the video._

### B73. Dirty `qty` vs HTTP 504 from SAP — which is DataWeave `try`, which is On Error?

_Speak, then check the video._

### B74. Memorize five HTTP `attributes` fields and say Listener vs Request.

_Speak, then check the video._

### B75. Default `xmlns="http://sap.example/idoc"` with no prefix on the XML. How do you select the root in DW? CDATA? Mixed content?

_Speak, then check the video._

### B76. Can DW read YAML, Excel, and EDI flat file in the Playground?

_Speak, then check the video._

### B77. When is `Values::mask` enough, and when must you recurse like Lab 39?

_Speak, then check the video._

### B78. Rewrite Java `status.equals("OPEN") && qty > 0` in DataWeave. Precedence of `not` / `and` / `or`?

_Speak, then check the video._

### B79. Sort plants by `region` A–Z, then `amount` descending. Why is `orderBy` then `orderBy` a trap?

_Speak, then check the video._

### B80. A 50k-line invoice file needs mapping, and some rows call SAP. DW, For Each, Batch, or Java — pick and say why.

_Speak, then check the video._

