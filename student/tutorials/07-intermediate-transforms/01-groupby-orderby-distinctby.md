# groupBy, orderBy, distinctBy

*Section: Group, reduce, merge, and update · Interview Q22 · easy words*

## In one sentence

groupBy buckets items by a key (returns an object of arrays). orderBy sorts. distinctBy unique by a key (keeps first).

## Like this in real life

groupBy customerId is sorting mail into pigeonholes. distinctBy email throws duplicate letters, keeping the first.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  byCity: payload groupBy ((c) -> c.city),
  sorted: payload orderBy ((c) -> c.name),
  unique: payload distinctBy ((c) -> c.email)
}
```

## Remember

groupBy is not an array. You pluck or namesOf to walk groups.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q22). Then try the lab listed for this section.
