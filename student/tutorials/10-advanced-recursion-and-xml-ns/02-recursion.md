# Recursion

*Section: Advanced: recursion, namespaces, diffs · Interview Q42 · easy words*

## In one sentence

A function that calls itself to walk trees: arrays, objects, then leaves.

## Like this in real life

Opening every nested gift box until you find the toy. Same motion at every layer.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
fun flattenTree(x) =
  x match {
    case a is Array -> a flatMap flattenTree($)
    case o is Object -> flattenTree(valuesOf(o))
    else -> [x]
  }
---
flattenTree(payload)
```

## Remember

match { case a is Array -> ... case o is Object -> ... else -> ... }

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q42). Then try the lab listed for this section.
