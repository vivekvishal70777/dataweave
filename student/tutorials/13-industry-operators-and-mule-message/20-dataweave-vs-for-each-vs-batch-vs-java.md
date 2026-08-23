# DataWeave vs For Each vs Batch vs Java

*Section: Industry operators, message, and MIME · Interview Q80 · easy words*

## In one sentence

DataWeave maps CPU-only. For Each calls connectors per item. Batch is huge files and retries. Java is special libraries.

## Like this in real life

DW = folding letters. For Each = posting each letter. Batch = the industrial mail warehouse. Java = a custom stamp machine.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// DataWeave = CPU mapping (this script).
// For Each = connector per item.
// Batch = huge file + retries.
payload map {
  id: $.Id
}
```

## Remember

No lookup/HTTP inside map.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q80). Then try the lab listed for this section.
