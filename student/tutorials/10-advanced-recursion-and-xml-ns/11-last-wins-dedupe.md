# Last-wins dedupe

*Section: Advanced: recursion, namespaces, diffs · Interview Q55 · easy words*

## In one sentence

distinctBy keeps the first. For last-wins, reduce into an object keyed by id, then valuesOf.

## Like this in real life

Two profile updates with the same email. You want the latest row, not the first.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload
  reduce ((item, acc = {}) -> acc ++ { (item.id): item })
  then valuesOf($)
```

## Remember

This is the CDC upsert story.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
