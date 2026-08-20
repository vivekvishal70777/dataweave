# Quiz 7 — Dates, match, try

1. `now() as String {format: "dd-MMM-yyyy"}` is:
   - A) A reader property on XML
   - B) Date formatting via coercion
   - C) HMAC
   - D) A join

2. `|P7D|` is:
   - A) A regex
   - B) An ISO-8601 **period** literal
   - C) A MIME type
   - D) A Mule error type

3. `try` / `orElse` in DataWeave:
   - A) Replaces the Mule error handler for the whole app
   - B) Catches failures **inside the script** (e.g. bad `as Number`)
   - C) Retries HTTP connectors
   - D) Starts a transaction

4. `default` vs `try`:
   - A) They are identical
   - B) `default` handles nulls; `try` handles errors
   - C) `try` only works on XML
   - D) `default` catches divide-by-zero

5. `match` can branch on:
   - A) Literals, types (`is`), conditions, and `else`
   - B) Only Booleans
   - C) Only HTTP methods
   - D) Only CSV columns
