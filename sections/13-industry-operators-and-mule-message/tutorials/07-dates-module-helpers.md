# Dates module helpers

*Section: Industry operators, message, and MIME · Interview Q67 · easy words*

## In one sentence

daysBetween, atBeginningOfDay, plus |P1M|. Periods are durations.

## Like this in real life

Invoice due in 30 days. SLA clock in hours (|PT2H|).

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Dates
output application/json
---
{
  days: daysBetween(payload.start as Date, payload.end as Date),
  startOfDay: atBeginningOfDay(payload.occurredAt as DateTime),
  nextMonth: (payload.start as Date) + |P1M|
}
```

## Remember

import dw::core::Dates.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q67). Then try the lab listed for this section.
