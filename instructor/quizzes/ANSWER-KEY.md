# Quiz answer key (instructor only)

Do not ship this file in the student zip.

## Quiz 1 — Fundamentals

1. B  
2. B  
3. B  
4. B  
5. B  

## Quiz 2 — Arrays

1. B  
2. C  
3. C  
4. B  
5. B  

## Quiz 3 — Objects

1. B  
2. A  
3. B  
4. B  
5. C  

## Quiz 4 — Strings

1. B  
2. B  
3. A  
4. B  
5. B  

## Quiz 5 — Formats

1. B  
2. B  
3. B  
4. B  
5. B  

## Quiz 6 — Intermediate

1. B  
2. B  
3. B  
4. B  
5. A  

## Quiz 7 — Dates / match / try

1. B  
2. B  
3. B  
4. B  
5. A  

## Quiz 8 — Joins / Mule

1. B  
2. A  
3. A  
4. B  
5. B  

## Quiz 9 — Advanced

1. B  
2. B  
3. B  
4. B  
5. B  
6. B

1. B  
2. B  
3. B  
4. A  
5. B  

## Quiz 12 — Industry operators / MIME

1. B  
2. A  
3. B  
4. B  
5. B  

## Final practice test

Score the spoken/written answers against `sections/12-interview-bootcamp/LECTURE.md` and labs 20, 23, 32, 39, 53, 54.

1. Header (`%dw 2.0`, `output`, imports/var/fun), `---`, body expression.  
2. `map` = arrays → arrays; `mapObject` = objects → objects.  
3. Attribute `payload.order.@id`; element `payload.order.customer`.  
4. Synchronous N+1 flow calls; fetch/enrich outside the per-item map.  
5. Any of: `sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, full `reduce`, double payload access, `as String` on whole doc.  
6. Parentheses: `{ (expr): value }`.  
7. First. Last-wins: `reduce` into object keyed by id, then `valuesOf`.  
8. `default` for null/missing; `try` for errors inside the script.  
9. `orders flatMap (o) -> o.items map (i) -> { orderId: o.id, sku: i.sku }`.  
10. `ns`, `.*line`, `@attr`, `as Number`, `fun`/`do` for money, join customer from `vars` not `lookup` per line, `skipNullOn`, one-pass map.
