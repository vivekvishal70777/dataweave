# Quiz 13 — DataWeave Mapping

1. Lookup tables for these labs live:
   - A) Inside `lookup()` per row
   - B) **On the payload** (then `groupBy` id)
   - C) Only in Object Store
   - D) In MEL

2. GST intra-state (same `fromState` / `toState`) usually means:
   - A) IGST only
   - B) CGST + SGST (split of the GST rate)
   - C) No tax
   - D) `lookup("gst")`

3. Debezium `op: "d"` should read fields from:
   - A) `after` only
   - B) `before`
   - C) HTTP attributes
   - D) `now()`

4. ERP `qty` and `amount` arrive as strings. First you:
   - A) `++` them
   - B) `as Number` (and `try` if dirty)
   - C) `write` to XML
   - D) `flatten`

5. Zero-qty lines in an invoice map:
   - A) Must be kept for GST
   - B) Are usually **filtered out** before totals
   - C) Require Java
   - D) Break `output application/json`
