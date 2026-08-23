# Functions (fun)

*Section: DataWeave 2.0 fundamentals · Interview Q5 · easy words*

## In one sentence

fun is a named recipe: give inputs, get an output. No side effects if you keep it pure.

## Like this in real life

Like a kitchen function fullName(first, last) that always returns the same plate for the same ingredients.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
fun fullName(first: String, last: String) = first ++ " " ++ last
---
fullName(payload.firstName, payload.lastName)
```

## Remember

You can overload by types. Prefer type annotations in modules.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
