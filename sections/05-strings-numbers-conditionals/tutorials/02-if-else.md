# if / else

*Section: Strings, numbers, and conditionals · Interview Q12 · easy words*

## In one sentence

if/else is an expression. It must produce a value. There is no Java question-mark colon.

## Like this in real life

Like a vending machine: if code is 503, spit out "retry". Every path must spit something.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
if (payload.age >= 18) "adult"
else if (payload.age >= 13) "teen"
else "child"
```

## Remember

You need else. A lonely if is illegal.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q12). Then try the lab listed for this section.
