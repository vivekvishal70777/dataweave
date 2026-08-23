# Timezones

*Section: Industry operators, message, and MIME · Interview Q66 · easy words*

## In one sentence

DateTime has an offset. Shift with >> "Asia/Kolkata". Store UTC. Convert at the edge.

## Like this in real life

A meeting at 14:05 UTC is 19:35 in India. Same moment, different wall clock.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
var ts = payload.occurredAt as DateTime
---
{
  utc: ts >> "UTC",
  ist: ts >> "Asia/Kolkata",
  display: (ts >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"}
}
```

## Remember

Do not use now() in a pricing module. Inject asOf.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
