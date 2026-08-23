# plus-plus vs plus

*Section: Strings, numbers, and conditionals · Interview Q10 · easy words*

## In one sentence

++ joins strings, arrays, or objects. + adds numbers. Do not mix them up.

## Like this in real life

"Hello" ++ " " ++ "World" is gluing paper. 1 + 2 is maths. Glue on numbers, or maths on words, and Mule shouts.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  hello: "Hi " ++ payload.firstName,
  ids: [1, 2] ++ [3],
  sum: 10 + 5
}
```

## Remember

Object ++ is a shallow merge. The right-hand key wins.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q10). Then try the lab listed for this section.
