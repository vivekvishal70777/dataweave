# Quiz 12 — Industry operators, message, and MIME

1. `payload maxBy $.amount` returns:
   - A) The max number only
   - B) The **item** whose amount is largest
   - C) An error always
   - D) A CSV row

2. Timezone shift in DataWeave:
   - A) `payload as DateTime >> "Asia/Kolkata"`
   - B) Java `TimeZone.getDefault()` only
   - C) `lookup("timezone")`
   - D) `++ "IST"`

3. `try` inside a script vs Mule On Error:
   - A) They are identical
   - B) `try` catches expression failures; On Error catches connector/flow failures
   - C) On Error only works in DataWeave 1.0
   - D) `try` retries HTTP 500

4. `zip(headers, values)` is for:
   - A) Compressing files
   - B) Pairing two arrays (then often dynamic keys)
   - C) XML namespaces
   - D) HMAC

5. Hide HTTP inside `payload map` via `lookup`:
   - A) Best practice for streaming
   - B) N+1 anti-pattern; fetch first, then DataWeave
   - C) Required for `groupBy`
   - D) How `zip` works
