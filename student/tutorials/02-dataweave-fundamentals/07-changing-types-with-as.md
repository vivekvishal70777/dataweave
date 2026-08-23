# Changing types with as

*Section: DataWeave 2.0 fundamentals · Interview Q7 · easy words*

## In one sentence

as tries to convert a value, like "10" as Number → 10.

## Like this in real life

Like pouring juice into a measuring cup. If the cup is for millilitres and you pour sand, it fails.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.age as Number
payload.createdAt as Date {format: "yyyy-MM-dd"}
payload as String {encoding: "UTF-8"}
```

## Remember

Failed as is an error. Use try, not default, when conversion can fail. Dates need a format.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q7). Then try the lab listed for this section.
