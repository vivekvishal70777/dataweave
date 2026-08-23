# maxBy, firstWith, and friends

*Section: Industry operators, message, and MIME · Interview Q61 · easy words*

## In one sentence

maxBy returns the whole item with the biggest field, not just the number. firstWith returns the first match.

## Like this in real life

richest order is the whole order record. firstPaid is the first PAID in line, even if a later one is bigger.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy $.amount,
  cheapest: payload minBy $.amount,
  firstPaid: payload firstWith ((o) -> o.status == "PAID"),
  anyOver: payload some ((o) -> (o.amount as Number) > 1000),
  allPositive: payload every ((o) -> (o.amount as Number) > 0),
  idx: indexOf(payload, ((o) -> o.id == "O1")),
  countPaid: payload countBy ((o) -> o.status == "PAID")
}
```

## Remember

import dw::core::Arrays. Guard empty lists.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q61). Then try the lab listed for this section.
