# is and typeOf

*Section: Industry operators, message, and MIME · Interview Q64 · easy words*

## In one sentence

is checks a type. typeOf names it. DataWeave has no Java ===.

## Like this in real life

“Is this a box of apples or a single apple?” Arrays and objects need different walks.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload is Object
payload.amount is Number
typeOf(payload)     // "Object" | "Array" | "String" | ...
```

## Remember

payload is Object. match { case x is Array -> }.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q64). Then try the lab listed for this section.
