# Quiz 12 — Production-level transforms

1. A batch mapper should usually:
   - A) Fail the whole message if one line has a bad `qty`
   - B) Put good lines in the canonical body and bad lines in `errors[]`
   - C) Replace bad money with `default 0` without telling anyone
   - D) Call `lookup` for every line

2. MDM vs CRM vs ERP golden record:
   - A) Always `erp ++ crm ++ mdm` (nulls from MDM wipe ERP)
   - B) Per-field coalesce with documented precedence; tag collection sources
   - C) Keep only ERP
   - D) Use MEL

3. Idempotency keys must not include:
   - A) Sorted unique SKUs
   - B) `customerId` and `externalOrderId`
   - C) `now()` or random UUIDs
   - D) A pipe separator

4. CDC delete (`op = d`) should:
   - A) Be dropped because `after` is null
   - B) Emit a tombstone using `before` and a stable `id`
   - C) Call Java UUID
   - D) Use `flatten`

5. FX rates in a `map` over lines:
   - A) Must `lookup` a flow per line
   - B) Should come from a table already in payload/`vars`
   - C) Should assume 1.0 when missing
   - D) Belong in CSV headers

6. Recursive BOM explode without a visited path:
   - A) Is always safe
   - B) Can infinite-loop when the graph has cycles
   - C) Is required by RFC 7396
   - D) Replaces `groupBy`

7. Scatter-Gather with one HTTP 500 and two HTTP 200s:
   - A) Must throw in DataWeave
   - B) Can return `ok` for the 200s and `errors[]` for the 500
   - C) Must retry inside `map`
   - D) Must use XML namespaces

8. JSON Merge Patch `null` on a field means:
   - A) Keep the old value
   - B) Delete that key
   - C) Set it to `0`
   - D) Skip the document
