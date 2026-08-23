# try

*Section: Dates, pattern matching, and try · Interview Q29 · easy words*

## In one sentence

try runs a risky expression and lets you orElse a fallback if it fails.

## Like this in real life

Tasting soup. If it burns (bad as Number), serve water (0 or null) instead of throwing the pot.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import try, orElse, orElseTry from dw::Runtime
output application/json
---
{
  n: try(() -> payload.age as Number) orElse 0,
  safe: try(() -> 1 / payload.divisor)
}
```

## Remember

try is not Mule On Error. HTTP timeouts still need On Error.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
