# Quiz 1 — Fundamentals

1. In Mule 4, DataWeave scripts usually start with:
   - A) `%dw 1.0` and `%output application/json`
   - B) `%dw 2.0` and `output application/json`
   - C) `import mule from dw`
   - D) `SELECT * FROM payload`

2. The `---` line in a script:
   - A) Comments out the header
   - B) Separates header (imports, var, fun, output) from the body expression
   - C) Means “optional output”
   - D) Starts a CSV row

3. Variables declared with `var` are:
   - A) Mutable, like Java fields
   - B) Immutable in the script
   - C) Only allowed in Mule 3
   - D) Always global across flows without Transform Message

4. `payload.age as Number` is:
   - A) Pattern matching
   - B) Type coercion
   - C) A MEL expression
   - D) A writer property

5. Interviews for Mule 4 almost always expect:
   - A) DataWeave 1.0 only
   - B) DataWeave 2.0
   - C) XSLT
   - D) Groovy
