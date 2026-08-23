# Diff two payloads

*Section: Advanced: recursion, namespaces, diffs · Interview Q49 · easy words*

## In one sentence

Compare old and new. List fields that changed, with from and to.

## Like this in real life

Change-data-capture: status NEW → PAID. Amount unchanged? Skip it.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
var old = vars.oldPayload
var newp = payload
---
namesOf(newp) filter ((k) -> old[k] != newp[k]) map (k) -> {
  field: k,
  from: old[k],
  to: newp[k]
}
```

## Remember

Nested diffs need recursion. Flat CDC is namesOf plus !=.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q49). Then try the lab listed for this section.
