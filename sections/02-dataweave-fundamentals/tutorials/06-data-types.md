# Data types

*Section: DataWeave 2.0 fundamentals · Interview Q6 · easy words*

## In one sentence

Values have types: String, Number, Boolean, Array, Object, Date, Null, Binary, and more.

## Like this in real life

A price should be a Number, not the text "99.99", until you coerce it. Mixing them is how scripts explode.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
fun add(a: Number, b: Number): Number = a + b
```

## Remember

Type names start with a capital. Any means “I did not specify.”

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q6). Then try the lab listed for this section.
