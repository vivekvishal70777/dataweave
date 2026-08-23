# Dollar signs in lambdas

*Section: Arrays: map, filter, and indexes · Interview Q35 · easy words*

## In one sentence

$ is the item. $$ is usually the index or key. $$$ is rare (third argument).

## Like this in real life

In a queue, $ is the person, $$ is their number in line (starting at 0).

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
["a", "b"] map upper($)
{ a: 1 } mapObject ((v, k) -> { (k): v })
```

## Remember

Named arguments (item, index) -> are clearer in interviews.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
