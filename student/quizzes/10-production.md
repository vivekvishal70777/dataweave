# Quiz 10 — Production and performance

1. Which is most likely to **break streaming** on a huge JSON array?
   - A) `payload map { id: $.id }`
   - B) `payload orderBy $.name`
   - C) `output application/json`
   - D) A comment in the header

2. HMAC vs hash:
   - A) They are the same
   - B) Hash is a checksum; HMAC signs with a secret
   - C) HMAC is only for XML
   - D) Hash requires `leftJoin`

3. Reusable functions belong in:
   - A) Random Java classes only
   - B) `.dwl` modules under resources, imported with `import … from modules::Name`
   - C) MEL files
   - D) CSV headers

4. Nested `filter` of the right-hand list for every left item is often:
   - A) O(n²); index with `groupBy` first
   - B) Faster than `groupBy` always
   - C) Required for streaming
   - D) How `++` works

5. Reader properties for CSV (header, separator) are often set:
   - A) Only in Java
   - B) On the **incoming MIME type**, not only in the script
   - C) In `match` cases
   - D) In `distinctBy`
