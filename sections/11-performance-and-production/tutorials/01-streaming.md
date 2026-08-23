# Streaming

*Section: Streaming, crypto, modules, and pitfalls · Interview Q41 · easy words*

## In one sentence

Streaming means DataWeave reads a huge file in pieces. It breaks if you need the whole file at once.

## Like this in real life

Watching a movie as it downloads vs downloading the whole movie to sort scenes. orderBy, groupBy, sizeOf(payload) need the whole movie.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Streaming-friendly: map / filter on the array.
// Streaming-hostile: orderBy, groupBy, sizeOf on the whole file, reduce to one object.
payload filter $.status == "PAID"
```

## Remember

One-pass map and filter can stream. Mention this in every senior interview.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q41). Then try the lab listed for this section.
