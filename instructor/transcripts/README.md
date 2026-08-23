# Recording transcripts

Spoken scripts for Vivek. **One video per concept lecture** and **one video per lab (01–54)**.

How to use: open the markdown, read **SAY**, follow **PAUSE CARD**, type the **TYPE** blocks. Target 6–10 minutes; cap 12. Split Lab 23, 39, 53, 54, and the whiteboard set if needed.

Quizzes on Udemy are practice tests — no transcript, no video.

Regenerate after lab or Q&A edits:

```bash
python3 scripts/generate_transcripts.py
```

## Suggested recording order

For each Udemy section: record the concept videos, then every lab video listed in `instructor/CURRICULUM.md` for that section. Optional “section bridge” transcripts (L09, L13, …) are skippable if the lab videos already sit in the curriculum.

## Concept and section lectures

| Code | Title | Length | Transcript |
| --- | --- | --- | --- |
| L01 | Welcome and what you will build | 3–4 min | [lectures/L01.md](lectures/L01.md) |
| L02 | How this course works (concept, pause, lab, quiz) | 3–4 min | [lectures/L02.md](lectures/L02.md) |
| L03 | Getting started: Playground vs Transform Message | 4–6 min | [lectures/L03.md](lectures/L03.md) |
| L04 | Tour of the student lab folder | 3–5 min | [lectures/L04.md](lectures/L04.md) |
| L05 | What is DataWeave in Mule 4? | 4–6 min | [lectures/L05.md](lectures/L05.md) |
| L06 | DataWeave 1.0 vs 2.0 | 5–7 min | [lectures/L06.md](lectures/L06.md) |
| L07 | Script structure: header, output, body | 5–8 min | [lectures/L07.md](lectures/L07.md) |
| L08 | Variables, functions, types, and as | 7–10 min | [lectures/L08.md](lectures/L08.md) |
| L09 | Section bridge: fundamentals labs | 1–2 min | [lectures/L09.md](lectures/L09.md) |
| L11 | map, filter, dollar and dollar-dollar | 7–10 min | [lectures/L11.md](lectures/L11.md) |
| L12 | sizeOf, isEmpty, flatten | 5–7 min | [lectures/L12.md](lectures/L12.md) |
| L13 | Section bridge: array labs | 1–2 min | [lectures/L13.md](lectures/L13.md) |
| L15 | Selectors: dot, brackets, star, descendant | 6–9 min | [lectures/L15.md](lectures/L15.md) |
| L16 | default, safe selector, skipNullOn | 6–9 min | [lectures/L16.md](lectures/L16.md) |
| L17 | mapObject and pluck | 6–9 min | [lectures/L17.md](lectures/L17.md) |
| L18 | Section bridge: object labs | 1–2 min | [lectures/L18.md](lectures/L18.md) |
| L20 | plus-plus vs plus; split, join, case | 6–9 min | [lectures/L20.md](lectures/L20.md) |
| L21 | if/else expressions (no Java ternary) | 5–8 min | [lectures/L21.md](lectures/L21.md) |
| L22 | Section bridge: string labs | 1–2 min | [lectures/L22.md](lectures/L22.md) |
| L24 | JSON to XML (single root) | 6–9 min | [lectures/L24.md](lectures/L24.md) |
| L25 | XML attributes and repeating elements | 6–9 min | [lectures/L25.md](lectures/L25.md) |
| L26 | CSV to JSON and JSON to CSV | 6–9 min | [lectures/L26.md](lectures/L26.md) |
| L27 | Section bridge: format labs | 1–2 min | [lectures/L27.md](lectures/L27.md) |
| L29 | groupBy, orderBy, distinctBy | 7–10 min | [lectures/L29.md](lectures/L29.md) |
| L30 | reduce and flatten | 7–10 min | [lectures/L30.md](lectures/L30.md) |
| L31 | flatMap line items (concept) | 5–8 min | [lectures/L31.md](lectures/L31.md) |
| L32 | Merge, update, and do | 7–10 min | [lectures/L32.md](lectures/L32.md) |
| L33 | Homework recap pointer (Lab 20) | 3–5 min | [lectures/L33.md](lectures/L33.md) |
| L35 | Dates, formats, and periods | 6–9 min | [lectures/L35.md](lectures/L35.md) |
| L36 | match and try / orElse | 7–10 min | [lectures/L36.md](lectures/L36.md) |
| L37 | Section bridge: date labs | 1–2 min | [lectures/L37.md](lectures/L37.md) |
| L39 | vars, attributes, and properties | 6–9 min | [lectures/L39.md](lectures/L39.md) |
| L40 | Modules and Transform Message vs hash-bracket | 6–9 min | [lectures/L40.md](lectures/L40.md) |
| L41 | Section bridge: join labs 31–32 | 1–2 min | [lectures/L41.md](lectures/L41.md) |
| L42 | Why not lookup or Java inside every map | 6–9 min | [lectures/L42.md](lectures/L42.md) |
| L44 | Recursion and match on types | 8–12 min | [lectures/L44.md](lectures/L44.md) |
| L45 | Deep PII mask (concept) | 3–6 min | [lectures/L45.md](lectures/L45.md) |
| L46 | XML namespaces read and write | 8–12 min | [lectures/L46.md](lectures/L46.md) |
| L47 | Dynamic keys, diffs, last-wins, pagination | 8–12 min | [lectures/L47.md](lectures/L47.md) |
| L48 | Section bridge: capstone labs 53–54 | 1–2 min | [lectures/L48.md](lectures/L48.md) |
| L50 | Streaming: what breaks it | 6–9 min | [lectures/L50.md](lectures/L50.md) |
| L51 | Crypto, binary, reader/writer properties | 8–12 min | [lectures/L51.md](lectures/L51.md) |
| L52 | Reusable modules and performance pitfalls | 8–12 min | [lectures/L52.md](lectures/L52.md) |
| L54a | How to run the 60-question bank | 4–6 min | [lectures/L54a.md](lectures/L54a.md) |
| L55 | Whiteboard mock interview (set of 6) | split into 6×~10 min or one section | [lectures/L55.md](lectures/L55.md) |
| L56 | Nested XML to canonical JSON (Q60) | 8–12 min | [lectures/L56.md](lectures/L56.md) |
| L58 | Next steps and solutions pack | 2–3 min | [lectures/L58.md](lectures/L58.md) |

## Lab videos (54)

All files: [`labs/`](labs/).

| Lab | Transcript |
| --- | --- |
| 01 Map employee JSON to a shorter shape | [labs/01-map-employee-json-to-a-shorter-shape.md](labs/01-map-employee-json-to-a-shorter-shape.md) |
| 02 Filter paid orders | [labs/02-filter-paid-orders.md](labs/02-filter-paid-orders.md) |
| 03 Sum array of numbers | [labs/03-sum-array-of-numbers.md](labs/03-sum-array-of-numbers.md) |
| 04 Uppercase all string values in an object | [labs/04-uppercase-all-string-values-in-an-object.md](labs/04-uppercase-all-string-values-in-an-object.md) |
| 05 Default missing email | [labs/05-default-missing-email.md](labs/05-default-missing-email.md) |
| 06 Split a CSV line into fields | [labs/06-split-a-csv-line-into-fields.md](labs/06-split-a-csv-line-into-fields.md) |
| 07 Join array into a comma-separated string | [labs/07-join-array-into-a-comma-separated-string.md](labs/07-join-array-into-a-comma-separated-string.md) |
| 08 Add tax to price | [labs/08-add-tax-to-price.md](labs/08-add-tax-to-price.md) |
| 09 Extract unique cities | [labs/09-extract-unique-cities.md](labs/09-extract-unique-cities.md) |
| 10 Count items in an array | [labs/10-count-items-in-an-array.md](labs/10-count-items-in-an-array.md) |
| 11 Convert JSON array to XML with a root | [labs/11-convert-json-array-to-xml-with-a-root.md](labs/11-convert-json-array-to-xml-with-a-root.md) |
| 12 Read XML attributes | [labs/12-read-xml-attributes.md](labs/12-read-xml-attributes.md) |
| 13 If/else grade from score | [labs/13-if-else-grade-from-score.md](labs/13-if-else-grade-from-score.md) |
| 14 Index each element | [labs/14-index-each-element.md](labs/14-index-each-element.md) |
| 15 Flatten one level | [labs/15-flatten-one-level.md](labs/15-flatten-one-level.md) |
| 16 Object keys to array of `{ key, value }` | [labs/16-object-keys-to-array-of-key-value.md](labs/16-object-keys-to-array-of-key-value.md) |
| 17 Boolean flag from string | [labs/17-boolean-flag-from-string.md](labs/17-boolean-flag-from-string.md) |
| 18 First three characters of a code | [labs/18-first-three-characters-of-a-code.md](labs/18-first-three-characters-of-a-code.md) |
| 19 Group orders by customer | [labs/19-group-orders-by-customer.md](labs/19-group-orders-by-customer.md) |
| 20 Total amount per customer | [labs/20-total-amount-per-customer.md](labs/20-total-amount-per-customer.md) |
| 21 Sort products by price descending | [labs/21-sort-products-by-price-descending.md](labs/21-sort-products-by-price-descending.md) |
| 22 Pivot array to object keyed by id | [labs/22-pivot-array-to-object-keyed-by-id.md](labs/22-pivot-array-to-object-keyed-by-id.md) |
| 23 Expand order lines (flatMap) | [labs/23-expand-order-lines-flatmap.md](labs/23-expand-order-lines-flatmap.md) |
| 24 Remove password and ssn keys | [labs/24-remove-password-and-ssn-keys.md](labs/24-remove-password-and-ssn-keys.md) |
| 25 Merge two objects (right wins) | [labs/25-merge-two-objects-right-wins.md](labs/25-merge-two-objects-right-wins.md) |
| 26 Update nested city to uppercase | [labs/26-update-nested-city-to-uppercase.md](labs/26-update-nested-city-to-uppercase.md) |
| 27 Parse mixed date formats | [labs/27-parse-mixed-date-formats.md](labs/27-parse-mixed-date-formats.md) |
| 28 Format `now()` as `dd-MMM-yyyy` | [labs/28-format-now-as-dd-mmm-yyyy.md](labs/28-format-now-as-dd-mmm-yyyy.md) |
| 29 CSV to JSON with number coercion | [labs/29-csv-to-json-with-number-coercion.md](labs/29-csv-to-json-with-number-coercion.md) |
| 30 JSON to CSV | [labs/30-json-to-csv.md](labs/30-json-to-csv.md) |
| 31 Left join orders to customers | [labs/31-left-join-orders-to-customers.md](labs/31-left-join-orders-to-customers.md) |
| 32 Join without `leftJoin` (groupBy lookup) | [labs/32-join-without-leftjoin-groupby-lookup.md](labs/32-join-without-leftjoin-groupby-lookup.md) |
| 33 Pattern match status codes | [labs/33-pattern-match-status-codes.md](labs/33-pattern-match-status-codes.md) |
| 34 Window / paginate an array | [labs/34-window-paginate-an-array.md](labs/34-window-paginate-an-array.md) |
| 35 Deduplicate by email, keep last record | [labs/35-deduplicate-by-email-keep-last-record.md](labs/35-deduplicate-by-email-keep-last-record.md) |
| 36 Dynamic object keys from an array of pairs | [labs/36-dynamic-object-keys-from-an-array-of-pairs.md](labs/36-dynamic-object-keys-from-an-array-of-pairs.md) |
| 37 Recursively flatten nested arrays | [labs/37-recursively-flatten-nested-arrays.md](labs/37-recursively-flatten-nested-arrays.md) |
| 38 Collect all `id` fields at any depth | [labs/38-collect-all-id-fields-at-any-depth.md](labs/38-collect-all-id-fields-at-any-depth.md) |
| 39 Deep mask PII keys (`ssn`, `password`, `email`) | [labs/39-deep-mask-pii-keys-ssn-password-email.md](labs/39-deep-mask-pii-keys-ssn-password-email.md) |
| 40 Recursively sum all numbers in a mixed tree | [labs/40-recursively-sum-all-numbers-in-a-mixed-tree.md](labs/40-recursively-sum-all-numbers-in-a-mixed-tree.md) |
| 41 XML namespaced order to canonical JSON | [labs/41-xml-namespaced-order-to-canonical-json.md](labs/41-xml-namespaced-order-to-canonical-json.md) |
| 42 Write XML with attributes and namespace | [labs/42-write-xml-with-attributes-and-namespace.md](labs/42-write-xml-with-attributes-and-namespace.md) |
| 43 Diff two flat objects (changed keys) | [labs/43-diff-two-flat-objects-changed-keys.md](labs/43-diff-two-flat-objects-changed-keys.md) |
| 44 Recursive nested diff | [labs/44-recursive-nested-diff.md](labs/44-recursive-nested-diff.md) |
| 45 Chunk array into batches of N (for bulk APIs) | [labs/45-chunk-array-into-batches-of-n-for-bulk-apis.md](labs/45-chunk-array-into-batches-of-n-for-bulk-apis.md) |
| 46 Running totals | [labs/46-running-totals.md](labs/46-running-totals.md) |
| 47 Word frequency (case-insensitive) | [labs/47-word-frequency-case-insensitive.md](labs/47-word-frequency-case-insensitive.md) |
| 48 Validate and partition good vs bad rows | [labs/48-validate-and-partition-good-vs-bad-rows.md](labs/48-validate-and-partition-good-vs-bad-rows.md) |
| 49 Outer-join style merge of two lists by `id` | [labs/49-outer-join-style-merge-of-two-lists-by-id.md](labs/49-outer-join-style-merge-of-two-lists-by-id.md) |
| 50 Tree map: apply `f` to every leaf string | [labs/50-tree-map-apply-f-to-every-leaf-string.md](labs/50-tree-map-apply-f-to-every-leaf-string.md) |
| 51 Combinations: cartesian product of two arrays | [labs/51-combinations-cartesian-product-of-two-arrays.md](labs/51-combinations-cartesian-product-of-two-arrays.md) |
| 52 Safe divide with `try` | [labs/52-safe-divide-with-try.md](labs/52-safe-divide-with-try.md) |
| 53 Build a nested org chart from a flat list | [labs/53-build-a-nested-org-chart-from-a-flat-list.md](labs/53-build-a-nested-org-chart-from-a-flat-list.md) |
| 54 Invoice: compute line totals, tax, and grand total | [labs/54-invoice-compute-line-totals-tax-and-grand-total.md](labs/54-invoice-compute-line-totals-tax-and-grand-total.md) |

## Udemy mapping

Old bundled lectures such as “Labs 03, 05, 08, 13” are replaced by individual lab videos. Keep the concept videos. Attach the matching `student/labs/...` folder on each lab lecture.
