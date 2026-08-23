# Split, join, and case

*Section: Strings, numbers, and conditionals · Interview Q16 · easy words*

## In one sentence

splitBy cuts a string into an array. joinBy glues an array into a string. upper / lower / capitalize change case.

## Like this in real life

CSV line "Asha,IT,Pune" splitBy comma is three boxes. joinBy comma packs them again.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  parts: payload.csvLine splitBy ",",
  csv: ["a", "b"] joinBy ",",
  upper: upper(payload.name),
  lower: lower(payload.name),
  cap: capitalize(payload.name)
}
```

## Remember

Import dw::core::Strings for trim, replace, substringAfter.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q16). Then try the lab listed for this section.
