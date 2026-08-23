# Section — Interview bootcamp

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/12-interview-bootcamp/README.md`](../../student/tutorials/12-interview-bootcamp/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Answer the 80-question bank out loud.
- Whiteboard the six signature programs.
- Talk through the nested XML → JSON design (Q60).

## Suggested video breakdown

- Do not re-teach Q1–80. Those answers were already taught in sections 2–12.
- Record timed drills: verbal flashcards, then whiteboard labs, then Q60 as a design talk.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 20
- Lab 23
- Lab 32
- Lab 39
- Lab 41
- Lab 53
- Lab 54

## This is not a second teaching pass

Q1–80 already appear in **topic sections** (easy tutorial → concept video → demo → lab → quiz).
Do **not** record another 80 videos here. Students drill from **prompts only** (no answer key in the zip).

Students drill **Set B**: `student/resources/bootcamp-prompts.md` (questions only).
Your answers while recording: `instructor/bootcamp/BOOTCAMP-QA.md`. Never zip that file.

The course bank (`reference/MuleSoft-DataWeave-Interview-Questions.md`) was already taught in sections 2–12.

### What to publish in this section

1. **Article** — how to drill. Attach **`student/resources/bootcamp-prompts.md` only** (Set B, no answers).
2. **Video: verbal mock** — you ask 8 mixed questions (easy + hard). Pause card after each prompt. Then you give a model 60-second answer. Do not open Studio.
3. **Video: whiteboard** — timebox 8 minutes each on Labs 23, 20, 32, 39, 41, 53/54 (pick 3 on camera; assign the rest).
4. **Video: Q60 design talk** — eight beats only (reader, types, money, join, shape, writer, try, scale). They already coded Lab 41 + 54.
5. **Practice test** — final quiz, not a lecture.

### Set B checklist (titles only — answers in instructor/bootcamp/BOOTCAMP-QA.md)

- B1. In one sentence, what problem does DataWeave solve in a Mule 4 API?
- B2. A teammate still writes `%dw 1.0` and `%output`. What do you change for Mule 4, and why would an interviewer care?
- B3. Walk me through a hello-world script that greets `payload.customerName`. Name the three parts.
- B4. You need a GST rate of 18% used in several fields. How do you store it, and can you change it later in the same script?
- B5. Write a small `fun` that builds `sku + "-" + plant` with types on the arguments.
- B6. Name at least eight DataWeave types you would list on a whiteboard.
- B7. The ERP sends `"qty": "12"`. How do you make it a number, and what if the text is garbage?
- B8. You have a list of shipments. Keep only `IN_TRANSIT`, then output `{ awb, dest }`. Which operator runs first?
- B9. A config object `{ host, port, tls }` must become an array of `{ name, value }`. Which function, and why not `map`?
- B10. What is wrong with `payload.first ++ payload.last` vs `payload.qty + payload.bonus`? When do you use `++` on objects?
- B11. `payload.account.iban` is sometimes missing. How do you avoid a crash, and when is `default` the wrong tool?
- B12. Classify `payload.score` as `"gold"` / `"silver"` / `"bronze"` with a DataWeave `if`. Why is `score > 90 ? "gold" : "silver"` wrong?
- B13. When do you write `payload."item-code"`, `payload[2]`, `payload.*Line`, and `payload..gstin`?
- B14. Turn a JSON array of plants into XML. What breaks if you forget a single root?
- B15. You need to know if `payload.batches` has rows. Compare `sizeOf` and `isEmpty`. Which phrase do you use in an interview?
- B16. Split a pipe-separated plant list, join SKUs with commas, and uppercase a material name. Which module?
- B17. In Transform Message, where do you read a flow variable `plant`, a query param `page`, and a property `sap.host`?
- B18. When is a Set Payload `#[payload.awb]` enough, and when must you open Transform Message?
- B19. A CSV column holds a JSON **string**. How do you parse it without changing the script’s `output` MIME? How do you log a compact JSON snapshot?
- B20. You do not want `null` IBAN fields in the JSON response. Which writer property, and name two others (CSV / compact JSON)?
- B21. Uppercase every **key** on `{ plant: "P001", qty: 2 }` and keep object shape. Why is `map` the wrong first choice?
- B22. From a list of invoices, group by `plant`, sort by `docDate`, and unique by `vendorGstin`. What type does `groupBy` return?
- B23. Sum `payload.lines.amount` with `reduce`, then also build `{ sku: qty }` with `reduce`. What if you omit the seed?
- B24. `[["A"], ["B","C"]]` should become `["A","B","C"]`. Is `flatten` enough for a 3-level tree?
- B25. `{ tax: { cgst: 9 } } ++ { tax: { sgst: 9 } }` — what is in `tax` after the merge? How do you deep-merge?
- B26. Uppercase `payload.vendor.address.city` without rewriting the whole vendor object. Which operator and which Mule version?
- B27. Inside `map` over invoices you need a local `var tds`. Why put it in a `do` block instead of the header?
- B28. Map SAP status `A` / `B` / anything starting with `E` / a Number / else. Show a `match`.
- B29. `payload.rate` is the string `"N/A"`. How do you coerce to Number without failing the whole script? Is this a Mule HTTP error handler?
- B30. Format today as `dd-MMM-yyyy`, parse `20-08-2026`, add seven days. Why is `now()` risky inside a pricing module?
- B31. Finance sends CSV with header `Vendor,Amount` and semicolon separators. How do you get JSON numbers?
- B32. Export invoices to CSV with columns `Doc` and `Gross`. How do headers appear?
- B33. XML `<Delivery id="D1"><Item>X</Item><Item>Y</Item></Delivery>`. How do you read `id` vs items vs write an attribute?
- B34. Show three `import` styles (star from Strings, one function from your module, Arrays as a prefix).
- B35. In `payload map { n: $$ + 1, v: $ }`, what are `$` and `$$`? When do you use `$$$`? What do you say if the interviewer hates dollars?
- B36. Drop keys `iban`, `pan`, `password` from an unknown object of secrets. Which function?
- B37. Join `payload.deliveries` to `payload.plants` on `plantCode` / `code` like SQL LEFT JOIN. What does each result row look like?
- B38. You need a UUID. Show a Java call. When do you refuse to call Java from DataWeave?
- B39. `"INV-4401"` — contrast `startsWith "INV"`, `contains "440"`, and `matches /INV-[0-9]+/`.
- B40. Why is `lookup("get-plant", { id: $.plant })` inside `map` a red flag? What do you do instead?
- B41. A 2 GB CSV must become JSON lines. Which DW operations destroy streaming?
- B42. Write `fun leaves(x)` that returns every primitive in a mixed JSON tree (objects + arrays).
- B43. Each delivery has `packages[]`. You need one output row per package with `awb` copied down. Name the operator.
- B44. SOAP body uses `xmlns:del="http://logistics.example/del"`. How do you **write** `del:Shipment` with an `id` attribute?
- B45. Webhook vs file checksum: when `hashWith` vs `HMACBinary`? What type is the payload?
- B46. Sketch `modules/Money.dwl` with `fun rupees(n)` and how you import it. What must stay out of a pure module?
- B47. For `{ gstin: "...", pan: "..." }`, contrast `keysOf`, `namesOf`, `valuesOf`, `entriesOf`.
- B48. `payload.pairs` is `[{ code: "P1", qty: 2 }]`. Build `{ P1: 2 }` with a **dynamic** key. What happens without parentheses?
- B49. `vars.before` and `payload` are two flat invoice objects. List fields that changed (`field`, `from`, `to`).
- B50. Overload `fun label` for String, Number, Array, and Any. Who wins?
- B51. Invoice dates arrive as `yyyy-MM-dd` **or** `dd/MM/yyyy`. Write a robust `fun parseInv`.
- B52. You receive a Base64 PDF in `vars.pdfB64`. How do you get Binary, and how do you encode Binary to Base64? Multipart?
- B53. Name two reader/writer knobs each for JSON, XML, and CSV.
- B54. `vars.page` and `vars.size` paginate `payload`. Write `drop` / `take`. Name `divideBy`.
- B55. CDC list has duplicate `gstin`; **last** row should win. Why is `distinctBy` alone wrong?
- B56. After `filter`, you want `{ count, rows }` without a header `var`. Show `then`. What does `also` return?
- B57. Mask any key named `pan`, `aadhaar`, or `iban` at unknown depth. Sketch `fun redact`.
- B58. List six performance answers an interviewer wants, including money and I/O.
- B59. Write `fun twice(x, f)` that applies `f` two times. Call it with `upper` and with a lambda. What is a higher-order function?
- B60. Talk through SAP IDoc XML → canonical invoice JSON in eight beats (no long script).
- B61. Besides `map`/`filter`, name `maxBy`, `firstWith`, `some`, `every`, `countBy`. What does `maxBy` return?
- B62. What is `payload[0 to 2]` vs `slice(payload, 1, 4)` vs `1 to 5`?
- B63. `payload.cols` and `payload.cells` are same-length arrays. Zip them into `{ name, value }` objects, then into one object.
- B64. How do you ask “is this an Array?” without Java `instanceof`?
- B65. Name number helpers plus how you round INR to 2 decimals without `BigDecimal`.
- B66. `payload.postedAt` is ISO-8601. Show UTC and IST display. What do you store in the canonical API?
- B67. Invoice due date is start + 1 month. Days between two dates? Start of that day?
- B68. Redact `INV-\d+` in notes, extract those ids, and take the SKU family before `-`.
- B69. One Transform Message must set JSON payload **and** variable `docCount`. How?
- B70. After a Salesforce connector the MIME is `application/java`. Do you `read` it as JSON? When do you **output** Java?
- B71. Plant codes live in `classpath://modules/plants.json`. `read` or `readUrl`? When is File connector better?
- B72. How do you log `payload.docId` inline, dump DW preview, and still not leak PAN?
- B73. Dirty `qty` vs HTTP 504 from SAP — which is DataWeave `try`, which is On Error?
- B74. Memorize five HTTP `attributes` fields and say Listener vs Request.
- B75. Default `xmlns="http://sap.example/idoc"` with no prefix on the XML. How do you select the root in DW? CDATA? Mixed content?
- B76. Can DW read YAML, Excel, and EDI flat file in the Playground?
- B77. When is `Values::mask` enough, and when must you recurse like Lab 39?
- B78. Rewrite Java `status.equals("OPEN") && qty > 0` in DataWeave. Precedence of `not` / `and` / `or`?
- B79. Sort plants by `region` A–Z, then `amount` descending. Why is `orderBy` then `orderBy` a trap?
- B80. A 50k-line invoice file needs mapping, and some rows call SAP. DW, For Each, Batch, or Java — pick and say why.
