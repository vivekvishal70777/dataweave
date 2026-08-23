# reduce

*Section: Group, reduce, merge, and update · Interview Q23 · easy words*

## In one sentence

reduce folds a list into one value: a sum, or a growing object.

## Like this in real life

A running total on a till. Each item updates the drawer. The drawer is the accumulator.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
[1, 2, 3] reduce ((item, acc = 0) -> acc + item)   // 6

payload reduce ((item, acc = {}) -> acc ++ {
  (item.id): item.name
})
```

## Remember

Give the accumulator a starting value (acc = 0 or acc = {}) or the first item becomes the seed.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
