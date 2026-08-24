# Recording transcripts

Spoken scripts for Vivek. **One video per concept lecture** and **one video per lab (01–88)**.

How to use: open the matching **PowerPoint** in [`../slides/pptx/`](../slides/pptx/README.md), press **F5**, share the window. Read **SAY** from this transcript (also in PPT notes). Follow **PAUSE CARD**, type the **TYPE** blocks. Target 6–10 minutes; cap 12. Split Lab 23, 39, 53, 54, and the whiteboard set if needed.

Quizzes on Udemy are practice tests — no transcript, no video.

Regenerate after lab or Q&A edits:

```bash
python3 scripts/generate_transcripts.py
python3 scripts/generate_slides.py
python3 scripts/generate_pptx.py
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
| L70 | Arrays helpers: maxBy, firstWith, zip, ranges | 8–12 min | [lectures/L70.md](lectures/L70.md) |
| L71 | Types, money, timezones, Dates module | 8–12 min | [lectures/L71.md](lectures/L71.md) |
| L72 | TM targets, Java MIME, readUrl, log, HTTP attributes | 8–12 min | [lectures/L72.md](lectures/L72.md) |
| L73 | XML ns extras, Excel/YAML, DW vs Batch | 8–12 min | [lectures/L73.md](lectures/L73.md) |
| L54a | How to run the 80-question bank | 4–6 min | [lectures/L54a.md](lectures/L54a.md) |
| L55 | Whiteboard mock interview (set of 6) | split into 6×~10 min or one section | [lectures/L55.md](lectures/L55.md) |
| L56 | Nested XML to canonical JSON (Q60) | 8–12 min | [lectures/L56.md](lectures/L56.md) |
| L58 | Next steps and solutions pack | 2–3 min | [lectures/L58.md](lectures/L58.md) |

## Lab videos (88)

All files: [`labs/`](labs/).

| Lab | Transcript |
| --- | --- |
| 01 Map Salesforce Contact to a shorter API shape | [labs/01-map-salesforce-contact-to-a-shorter-api-shape.md](labs/01-map-salesforce-contact-to-a-shorter-api-shape.md) |
| 02 Filter settled commerce orders | [labs/02-filter-settled-commerce-orders.md](labs/02-filter-settled-commerce-orders.md) |
| 03 Sum invoice line amounts (string money) | [labs/03-sum-invoice-line-amounts-string-money.md](labs/03-sum-invoice-line-amounts-string-money.md) |
| 04 Uppercase string fields on an address object | [labs/04-uppercase-string-fields-on-an-address-object.md](labs/04-uppercase-string-fields-on-an-address-object.md) |
| 05 Default missing email on an Account | [labs/05-default-missing-email-on-an-account.md](labs/05-default-missing-email-on-an-account.md) |
| 06 Split a CSV line into fields | [labs/06-split-a-csv-line-into-fields.md](labs/06-split-a-csv-line-into-fields.md) |
| 07 Join SKUs into a comma-separated string | [labs/07-join-skus-into-a-comma-separated-string.md](labs/07-join-skus-into-a-comma-separated-string.md) |
| 08 Add GST to a unit price (2 decimal money) | [labs/08-add-gst-to-a-unit-price-2-decimal-money.md](labs/08-add-gst-to-a-unit-price-2-decimal-money.md) |
| 09 Extract unique billing cities, sorted | [labs/09-extract-unique-billing-cities-sorted.md](labs/09-extract-unique-billing-cities-sorted.md) |
| 10 Count line items in a composite payload | [labs/10-count-line-items-in-a-composite-payload.md](labs/10-count-line-items-in-a-composite-payload.md) |
| 11 Convert JSON array to XML with a single root | [labs/11-convert-json-array-to-xml-with-a-single-root.md](labs/11-convert-json-array-to-xml-with-a-single-root.md) |
| 12 Read XML attributes vs element text | [labs/12-read-xml-attributes-vs-element-text.md](labs/12-read-xml-attributes-vs-element-text.md) |
| 13 Classify an HTTP/integration status | [labs/13-classify-an-http-integration-status.md](labs/13-classify-an-http-integration-status.md) |
| 14 Index each batch row (1-based) | [labs/14-index-each-batch-row-1-based.md](labs/14-index-each-batch-row-1-based.md) |
| 15 Flatten one level of nested arrays | [labs/15-flatten-one-level-of-nested-arrays.md](labs/15-flatten-one-level-of-nested-arrays.md) |
| 16 Object keys to array of `{ key, value }` | [labs/16-object-keys-to-array-of-key-value.md](labs/16-object-keys-to-array-of-key-value.md) |
| 17 Boolean flag from dirty string | [labs/17-boolean-flag-from-dirty-string.md](labs/17-boolean-flag-from-dirty-string.md) |
| 18 SKU prefix before hyphen | [labs/18-sku-prefix-before-hyphen.md](labs/18-sku-prefix-before-hyphen.md) |
| 19 Group orders by customerId | [labs/19-group-orders-by-customerid.md](labs/19-group-orders-by-customerid.md) |
| 20 Total amount per customer (groupBy + sum) | [labs/20-total-amount-per-customer-groupby-sum.md](labs/20-total-amount-per-customer-groupby-sum.md) |
| 21 Sort products by unitPrice descending | [labs/21-sort-products-by-unitprice-descending.md](labs/21-sort-products-by-unitprice-descending.md) |
| 22 Pivot array to object keyed by Id | [labs/22-pivot-array-to-object-keyed-by-id.md](labs/22-pivot-array-to-object-keyed-by-id.md) |
| 23 Expand order lines (flatMap) | [labs/23-expand-order-lines-flatmap.md](labs/23-expand-order-lines-flatmap.md) |
| 24 Strip password, ssn, and accessToken keys | [labs/24-strip-password-ssn-and-accesstoken-keys.md](labs/24-strip-password-ssn-and-accesstoken-keys.md) |
| 25 Merge config overlay (right wins) | [labs/25-merge-config-overlay-right-wins.md](labs/25-merge-config-overlay-right-wins.md) |
| 26 Update nested city to uppercase (Mule 4.3+) | [labs/26-update-nested-city-to-uppercase-mule-4-3.md](labs/26-update-nested-city-to-uppercase-mule-4-3.md) |
| 27 Parse mixed date formats (ISO or dd/MM/yyyy) | [labs/27-parse-mixed-date-formats-iso-or-dd-mm-yyyy.md](labs/27-parse-mixed-date-formats-iso-or-dd-mm-yyyy.md) |
| 28 Format an event timestamp as `dd-MMM-yyyy` | [labs/28-format-an-event-timestamp-as-dd-mmm-yyyy.md](labs/28-format-an-event-timestamp-as-dd-mmm-yyyy.md) |
| 29 CSV to JSON with number coercion | [labs/29-csv-to-json-with-number-coercion.md](labs/29-csv-to-json-with-number-coercion.md) |
| 30 JSON to CSV for finance export | [labs/30-json-to-csv-for-finance-export.md](labs/30-json-to-csv-for-finance-export.md) |
| 31 Left join orders to customers | [labs/31-left-join-orders-to-customers.md](labs/31-left-join-orders-to-customers.md) |
| 32 Join without leftJoin (groupBy lookup) | [labs/32-join-without-leftjoin-groupby-lookup.md](labs/32-join-without-leftjoin-groupby-lookup.md) |
| 33 Pattern match HTTP status class | [labs/33-pattern-match-http-status-class.md](labs/33-pattern-match-http-status-class.md) |
| 34 Window / paginate a bulk array | [labs/34-window-paginate-a-bulk-array.md](labs/34-window-paginate-a-bulk-array.md) |
| 35 Deduplicate by email, keep last record (CDC) | [labs/35-deduplicate-by-email-keep-last-record-cdc.md](labs/35-deduplicate-by-email-keep-last-record-cdc.md) |
| 36 Dynamic object keys from header pairs | [labs/36-dynamic-object-keys-from-header-pairs.md](labs/36-dynamic-object-keys-from-header-pairs.md) |
| 37 Recursively flatten nested arrays | [labs/37-recursively-flatten-nested-arrays.md](labs/37-recursively-flatten-nested-arrays.md) |
| 38 Collect all `id` fields at any depth | [labs/38-collect-all-id-fields-at-any-depth.md](labs/38-collect-all-id-fields-at-any-depth.md) |
| 39 Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`) | [labs/39-deep-mask-pii-keys-ssn-password-email-accesstoken.md](labs/39-deep-mask-pii-keys-ssn-password-email-accesstoken.md) |
| 40 Recursively sum all numbers in a mixed tree | [labs/40-recursively-sum-all-numbers-in-a-mixed-tree.md](labs/40-recursively-sum-all-numbers-in-a-mixed-tree.md) |
| 41 SOAP namespaced purchase order to canonical JSON | [labs/41-soap-namespaced-purchase-order-to-canonical-json.md](labs/41-soap-namespaced-purchase-order-to-canonical-json.md) |
| 42 Write namespaced XML from canonical JSON | [labs/42-write-namespaced-xml-from-canonical-json.md](labs/42-write-namespaced-xml-from-canonical-json.md) |
| 43 CDC flat diff (before vs after) | [labs/43-cdc-flat-diff-before-vs-after.md](labs/43-cdc-flat-diff-before-vs-after.md) |
| 44 Recursive nested diff | [labs/44-recursive-nested-diff.md](labs/44-recursive-nested-diff.md) |
| 45 Chunk array into batches of N (Salesforce Composite / bulk) | [labs/45-chunk-array-into-batches-of-n-salesforce-composite-bulk.md](labs/45-chunk-array-into-batches-of-n-salesforce-composite-bulk.md) |
| 46 Running totals (ledger) | [labs/46-running-totals-ledger.md](labs/46-running-totals-ledger.md) |
| 47 Error-code frequency from log lines | [labs/47-error-code-frequency-from-log-lines.md](labs/47-error-code-frequency-from-log-lines.md) |
| 48 Validate and partition good vs bad rows | [labs/48-validate-and-partition-good-vs-bad-rows.md](labs/48-validate-and-partition-good-vs-bad-rows.md) |
| 49 Outer-join style merge of two lists by `id` | [labs/49-outer-join-style-merge-of-two-lists-by-id.md](labs/49-outer-join-style-merge-of-two-lists-by-id.md) |
| 50 Tree map: apply `f` to every leaf string | [labs/50-tree-map-apply-f-to-every-leaf-string.md](labs/50-tree-map-apply-f-to-every-leaf-string.md) |
| 51 Cartesian product of SKU options | [labs/51-cartesian-product-of-sku-options.md](labs/51-cartesian-product-of-sku-options.md) |
| 52 Safe unit price with `try` | [labs/52-safe-unit-price-with-try.md](labs/52-safe-unit-price-with-try.md) |
| 53 Build a nested org chart from a flat HR list | [labs/53-build-a-nested-org-chart-from-a-flat-hr-list.md](labs/53-build-a-nested-org-chart-from-a-flat-hr-list.md) |
| 54 Production invoice: discounts, tax, skip zero qty | [labs/54-production-invoice-discounts-tax-skip-zero-qty.md](labs/54-production-invoice-discounts-tax-skip-zero-qty.md) |
| 55 maxBy and firstWith on a work queue | [labs/55-maxby-and-firstwith-on-a-work-queue.md](labs/55-maxby-and-firstwith-on-a-work-queue.md) |
| 56 Shift DateTime to IST for display | [labs/56-shift-datetime-to-ist-for-display.md](labs/56-shift-datetime-to-ist-for-display.md) |
| 57 Zip headers with values into an object | [labs/57-zip-headers-with-values-into-an-object.md](labs/57-zip-headers-with-values-into-an-object.md) |
| 58 Simulate Transform Message payload + vars | [labs/58-simulate-transform-message-payload-vars.md](labs/58-simulate-transform-message-payload-vars.md) |
| 59 Salesforce Account composite to nested customer API | [labs/59-salesforce-account-composite-to-nested-customer-api.md](labs/59-salesforce-account-composite-to-nested-customer-api.md) |
| 60 SAP-style order JSON to canonical invoice with GST | [labs/60-sap-style-order-json-to-canonical-invoice-with-gst.md](labs/60-sap-style-order-json-to-canonical-invoice-with-gst.md) |
| 61 Workday workers to HR API (active only) | [labs/61-workday-workers-to-hr-api-active-only.md](labs/61-workday-workers-to-hr-api-active-only.md) |
| 62 Shopify order to ERP sales order | [labs/62-shopify-order-to-erp-sales-order.md](labs/62-shopify-order-to-erp-sales-order.md) |
| 63 Stripe charges enriched with customer | [labs/63-stripe-charges-enriched-with-customer.md](labs/63-stripe-charges-enriched-with-customer.md) |
| 64 ServiceNow incident plus CMDB lookup | [labs/64-servicenow-incident-plus-cmdb-lookup.md](labs/64-servicenow-incident-plus-cmdb-lookup.md) |
| 65 Debezium CDC envelope to flat upsert rows | [labs/65-debezium-cdc-envelope-to-flat-upsert-rows.md](labs/65-debezium-cdc-envelope-to-flat-upsert-rows.md) |
| 66 Product variants color times size SKUs | [labs/66-product-variants-color-times-size-skus.md](labs/66-product-variants-color-times-size-skus.md) |
| 67 Multi-currency lines to USD using FX table | [labs/67-multi-currency-lines-to-usd-using-fx-table.md](labs/67-multi-currency-lines-to-usd-using-fx-table.md) |
| 68 Normalize IN vs US postal addresses | [labs/68-normalize-in-vs-us-postal-addresses.md](labs/68-normalize-in-vs-us-postal-addresses.md) |
| 69 EDI-like PO JSON to procurement canonical | [labs/69-edi-like-po-json-to-procurement-canonical.md](labs/69-edi-like-po-json-to-procurement-canonical.md) |
| 70 Bank statement lines to signed running ledger | [labs/70-bank-statement-lines-to-signed-running-ledger.md](labs/70-bank-statement-lines-to-signed-running-ledger.md) |
| 71 IdP userinfo plus groups to application roles | [labs/71-idp-userinfo-plus-groups-to-application-roles.md](labs/71-idp-userinfo-plus-groups-to-application-roles.md) |
| 72 Allocate warehouse stock to order lines FIFO | [labs/72-allocate-warehouse-stock-to-order-lines-fifo.md](labs/72-allocate-warehouse-stock-to-order-lines-fifo.md) |
| 73 India GST split CGST SGST vs IGST by state | [labs/73-india-gst-split-cgst-sgst-vs-igst-by-state.md](labs/73-india-gst-split-cgst-sgst-vs-igst-by-state.md) |
| 74 Loyalty points from paid orders | [labs/74-loyalty-points-from-paid-orders.md](labs/74-loyalty-points-from-paid-orders.md) |
| 75 Appointment slots to IST display with duration | [labs/75-appointment-slots-to-ist-display-with-duration.md](labs/75-appointment-slots-to-ist-display-with-duration.md) |
| 76 BOM explode one level to pick list | [labs/76-bom-explode-one-level-to-pick-list.md](labs/76-bom-explode-one-level-to-pick-list.md) |
| 77 RMA restock vs refund split | [labs/77-rma-restock-vs-refund-split.md](labs/77-rma-restock-vs-refund-split.md) |
| 78 Catalog pick locale with English fallback | [labs/78-catalog-pick-locale-with-english-fallback.md](labs/78-catalog-pick-locale-with-english-fallback.md) |
| 79 Partner catalog XML to JSON products | [labs/79-partner-catalog-xml-to-json-products.md](labs/79-partner-catalog-xml-to-json-products.md) |
| 80 Health claims flatten ICD diagnosis codes | [labs/80-health-claims-flatten-icd-diagnosis-codes.md](labs/80-health-claims-flatten-icd-diagnosis-codes.md) |
| 81 Telecom CDR aggregate minutes by MSISDN | [labs/81-telecom-cdr-aggregate-minutes-by-msisdn.md](labs/81-telecom-cdr-aggregate-minutes-by-msisdn.md) |
| 82 Listings filter amenities and map geo | [labs/82-listings-filter-amenities-and-map-geo.md](labs/82-listings-filter-amenities-and-map-geo.md) |
| 83 SCIM-style patch merge on user | [labs/83-scim-style-patch-merge-on-user.md](labs/83-scim-style-patch-merge-on-user.md) |
| 84 Payment recon: bank UTR vs gateway charges | [labs/84-payment-recon-bank-utr-vs-gateway-charges.md](labs/84-payment-recon-bank-utr-vs-gateway-charges.md) |
| 85 Manufacturing routing duration by work order | [labs/85-manufacturing-routing-duration-by-work-order.md](labs/85-manufacturing-routing-duration-by-work-order.md) |
| 86 Event-sourced account balance | [labs/86-event-sourced-account-balance.md](labs/86-event-sourced-account-balance.md) |
| 87 Multi-tenant config overlay (deep-ish merge) | [labs/87-multi-tenant-config-overlay-deep-ish-merge.md](labs/87-multi-tenant-config-overlay-deep-ish-merge.md) |
| 88 Canonical product GTIN and UoM conversion | [labs/88-canonical-product-gtin-and-uom-conversion.md](labs/88-canonical-product-gtin-and-uom-conversion.md) |

## Udemy mapping

Old bundled lectures such as “Labs 03, 05, 08, 13” are replaced by individual lab videos. Keep the concept videos. Attach the matching `student/labs/...` folder on each lab lecture.
