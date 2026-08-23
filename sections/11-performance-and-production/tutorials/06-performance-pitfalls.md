# Performance pitfalls

*Section: Streaming, crypto, modules, and pitfalls · Interview Q58 · easy words*

## In one sentence

Name: groupBy on huge data, O(n²) nested filter, lookup in map, payload as String, XML .. on big docs, breaking streaming.

## Like this in real life

Index the customer list once (groupBy id), then map orders. Do not search the whole list for every order.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Pitfalls: lookup/Java inside map, orderBy on a huge file,
// ++ in a hot loop, nested map+filter that rescans the same array.
payload map (r) -> r - "internalNotes"
```

## Remember

Coerce money once. No I/O inside map.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
