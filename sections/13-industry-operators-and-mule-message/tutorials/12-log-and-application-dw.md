# log and application/dw

*Section: Industry operators, message, and MIME · Interview Q72 · easy words*

## In one sentence

log prints and returns the value. application/dw is a debug view. Never log PII.

## Like this in real life

A sticky “DEBUG: order O-1” on the belt. Not a photocopy of passports.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  seen: log("DEBUG", payload.id),
  body: payload
}
```

## Remember

log is not try and not On Error.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q72). Then try the lab listed for this section.
