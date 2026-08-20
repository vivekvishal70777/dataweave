# Quiz 8 — Joins, modules, Mule context

1. Customer id already stored in a Mule variable is typically:
   - A) `flowVars.customerId` (Mule 3 style only in DW 2)
   - B) `vars.customerId`
   - C) `p.customerId`
   - D) `java.customerId`

2. `leftJoin(orders, customers, (o) -> o.customerId, (c) -> c.id)` result items look like:
   - A) `{ l: order, r: customer }`
   - B) SQL ResultSet
   - C) A single string
   - D) XML attributes

3. A DataWeave-only lookup instead of nested loops:
   - A) `groupBy` the right side, then `map` the left
   - B) `lookup` inside every `map` iteration as best practice
   - C) Convert to Java `HashMap` always
   - D) Use MEL

4. `lookup("get-customer-flow", …)` inside `map` is risky because:
   - A) It is asynchronous always
   - B) It can become N+1 synchronous flow calls
   - C) It cannot return JSON
   - D) It disables XML

5. Calling Java from DataWeave is:
   - A) The default for every mapping
   - B) Possible, but prefer pure DataWeave; Java adds coupling
   - C) Impossible in Mule 4
   - D) Required for `upper()`
