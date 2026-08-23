# Mask PII in an unknown tree

*Section: Advanced: recursion, namespaces, diffs · Interview Q57 · easy words*

## In one sentence

Walk objects and arrays. If the key is email/ssn/password, output stars. Else keep walking.

## Like this in real life

A marker over secrets on every page of a mixed folder, not only the cover sheet.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
var secretKeys = ["ssn", "password", "email"]
fun mask(x) =
  x match {
    case o is Object -> o mapObject ((v, k) -> {
      (k): if (secretKeys contains lower(k as String)) "****" else mask(v)
    })
    case a is Array -> a map mask($)
    else -> x
  }
---
mask(payload)
```

## Remember

Mask before log. Known paths can use update instead.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q57). Then try the lab listed for this section.
