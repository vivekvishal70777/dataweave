# keysOf, namesOf, valuesOf, entriesOf

*Section: Advanced: recursion, namespaces, diffs · Interview Q47 · easy words*

## In one sentence

keysOf is XML-aware keys. namesOf is string names (usual JSON). valuesOf is values. entriesOf is {key, value} list.

## Like this in real life

A coat check: names of coats, the coats themselves, or tickets paired with coats.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
var obj = { a: 1, b: 2 }
---
{
  keys: keysOf(obj),       // ["a", "b"] as Keys
  names: namesOf(obj),     // ["a", "b"] as Strings
  values: valuesOf(obj),   // [1, 2]
  entries: entriesOf(obj)  // [{key: "a", value: 1}, ...]
}
```

## Remember

For JSON dynamic keys, namesOf is what you usually want.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q47). Then try the lab listed for this section.
