# Quiz 4 — Strings, numbers, conditionals

1. `"Hello" ++ " " ++ "World"` concatenates strings. `"Hello" + "World"`:
   - A) Also concatenates
   - B) Is numeric addition and typically fails on strings
   - C) Joins with commas
   - D) Lowercases both

2. `{ a: 1 } ++ { a: 9, b: 2 }` yields:
   - A) `{ a: 1 }`
   - B) `{ a: 9, b: 2 }` with right-hand `a` winning
   - C) An array
   - D) An error always

3. DataWeave if/else is:
   - A) An expression (must produce a value)
   - B) A statement with no value
   - C) The same as Java ternary `? :`
   - D) Only allowed in Mule 3

4. `splitBy ","` returns:
   - A) A string
   - B) An array
   - C) An object
   - D) XML

5. `write(payload, "application/json")` inside a script:
   - A) Changes the Transform Message output MIME type
   - B) Serializes a value to String/Binary **without** changing the script `output` MIME
   - C) Is the same as `output application/xml`
   - D) Only works in DataWeave 1.0
