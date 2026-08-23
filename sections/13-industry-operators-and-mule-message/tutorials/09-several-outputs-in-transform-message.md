# Several outputs in Transform Message

*Section: Industry operators, message, and MIME · Interview Q69 · easy words*

## In one sentence

One component can set payload and variables. Each target is its own script.

## Like this in real life

Stamp the parcel (payload) and write the tracking number in your notebook (vars) in the same desk visit.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Target 1 — Payload:
payload
// Target 2 — Variable correlationId (separate script):
// attributes.headers['x-correlation-id'] default uuid()
```

## Remember

Playground cannot set Mule vars. Lab 58 simulates both in one JSON.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
