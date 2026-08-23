# Variables (var)

*Section: DataWeave 2.0 fundamentals · Interview Q4 · easy words*

## In one sentence

var stores a value you can reuse. You cannot change it later. It is immutable.

## Like this in real life

Like writing a GST rate of 0.18 on a sticky note. You read it many times. You do not scribble a new number on the same note.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
var taxRate = 0.18
---
{
  total: payload.amount * (1 + taxRate)
}
```

## Remember

Put var in the header, or inside a do block for a local value.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
