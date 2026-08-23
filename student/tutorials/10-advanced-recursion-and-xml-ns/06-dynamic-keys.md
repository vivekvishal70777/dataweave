# Dynamic keys

*Section: Advanced: recursion, namespaces, diffs · Interview Q48 · easy words*

## In one sentence

Wrap the key expression in parentheses: { (item.id): item.name }.

## Like this in real life

The label on the box is printed from the barcode, not handwritten as the word “item.id”.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload.fields reduce ((f, acc = {}) -> acc ++ {
  (f.name): f.value
})
```

## Remember

Without ( ), the key is the literal text. This is a top interview trap.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
