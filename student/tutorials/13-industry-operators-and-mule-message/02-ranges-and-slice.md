# Ranges and slice

*Section: Industry operators, message, and MIME · Interview Q62 · easy words*

## In one sentence

[0 to 2] is the first three items (inclusive). 1 to 5 is numbers 1,2,3,4,5. slice is a clear window.

## Like this in real life

Taking pages 1–3 of a report.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import slice from dw::core::Arrays
output application/json
---
{
  firstThree: payload[0 to 2],
  nums: 1 to 5,
  mid: slice(payload, 1, 4)
}
```

## Remember

Prefer slice / take / drop in production code.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q62). Then try the lab listed for this section.
