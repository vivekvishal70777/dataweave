# CSV to JSON

*Section: JSON, XML, and CSV mappings · Interview Q31 · easy words*

## In one sentence

With header=true, each CSV row becomes an object. Keys come from the header line. Coerce numbers.

## Like this in real life

Excel export → list of records. Amount is text until as Number.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number
}
```

## Remember

Set MIME application/csv on the incoming message.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q31). Then try the lab listed for this section.
