# Mixed date formats

*Section: Advanced: recursion, namespaces, diffs · Interview Q51 · easy words*

## In one sentence

try the first format, orElseTry the next, orElse null.

## Like this in real life

Customers type 2026-08-20 or 20/08/2026. You accept both. Garbage becomes null, not a crash.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import try, orElseTry, orElse from dw::Runtime
output application/json
fun parseDate(s: String) =
  try(() -> s as Date {format: "yyyy-MM-dd"})
    orElseTry (() -> s as Date {format: "dd/MM/yyyy"})
    orElseTry (() -> s as Date {format: "dd-MMM-yyyy"})
    orElse null
---
payload map { id: $.id, date: parseDate($.date) }
```

## Remember

default will not save a failed as Date.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q51). Then try the lab listed for this section.
