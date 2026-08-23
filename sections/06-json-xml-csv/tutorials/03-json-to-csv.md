# JSON to CSV

*Section: JSON, XML, and CSV mappings · Interview Q32 · easy words*

## In one sentence

output application/csv header=true. Object keys become column names.

## Like this in real life

Your API list becomes a finance spreadsheet.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/csv header=true, separator=","
---
payload map {
  OrderId: $.id,
  Total: $.amount
}
```

## Remember

Every row object should use the same keys.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q32). Then try the lab listed for this section.
