# DataWeave 1.0 vs 2.0

*Section: DataWeave 2.0 fundamentals · Interview Q2 · easy words*

## In one sentence

Interviews want DataWeave 2.0 (Mule 4). Version 1.0 is the old Mule 3 style.

## Like this in real life

Like switching from an old phone OS to a new one. Same idea, different buttons. Header is %dw 2.0, output is output application/json, not %output.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Mule 4 header: version 2.0, then output, then ---
payload
```

## Remember

If they say MEL, that is Mule 3. Mule 4 is DataWeave everywhere.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
