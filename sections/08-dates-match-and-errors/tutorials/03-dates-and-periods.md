# Dates and periods

*Section: Dates, pattern matching, and try · Interview Q30 · easy words*

## In one sentence

Parse with as Date {format:...}. Format with as String {format:...}. Add |P7D| for seven days.

## Like this in real life

A calendar stamp. The same instant can print as 20-Aug-2026. A period is “how long,” not a clock time.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  today: now(),
  formatted: now() as String {format: "dd-MMM-yyyy"},
  parsed: "2026-08-20" as Date {format: "yyyy-MM-dd"},
  nextWeek: (now() as Date) + |P7D|,
  ageDays: |P1Y2M| 
}
```

## Remember

Pipe literals: |2026-08-20|. Prefer injecting time over now() in modules.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
