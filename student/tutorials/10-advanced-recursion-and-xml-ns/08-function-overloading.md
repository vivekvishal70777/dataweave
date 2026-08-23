# Function overloading

*Section: Advanced: recursion, namespaces, diffs · Interview Q50 · easy words*

## In one sentence

Same fun name, different argument types. The most specific match wins.

## Like this in real life

describe("hi") vs describe(3) print different labels, like two stamps in one drawer.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
fun describe(x: String) = "string: " ++ x
fun describe(x: Number) = "number: " ++ (x as String)
fun describe(x: Array) = "array size " ++ sizeOf(x)
fun describe(x: Any) = "other"
```

## Remember

Pair with match { case x is Date -> } for trees.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q50). Then try the lab listed for this section.
