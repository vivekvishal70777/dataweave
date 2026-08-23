# sizeOf and isEmpty

*Section: Arrays: map, filter, and indexes · Interview Q15 · easy words*

## In one sentence

sizeOf counts. isEmpty asks “is there nothing?” Prefer isEmpty when you only care about empty vs not.

## Like this in real life

Do not count every grain of rice to see if the bowl is empty. Just look.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
sizeOf(payload.items)     // array length, object key count, or string length
isEmpty(payload.items)    // true for [], {}, "", or null in many cases
```

## Remember

sizeOf works on arrays, objects (keys), and strings.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q15). Then try the lab listed for this section.
