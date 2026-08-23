# zip

*Section: Industry operators, message, and MIME · Interview Q63 · easy words*

## In one sentence

zip pairs two arrays: headers with values. Then you can build an object.

## Like this in real life

A blank form (headers) and a handwritten row (values). zip staples them cell by cell.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  map { name: $[0], value: $[1] }
```

## Remember

Length follows the shorter array.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q63). Then try the lab listed for this section.
