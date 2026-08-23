# mapObject

*Section: Objects, nulls, and selectors · Interview Q21 · easy words*

## In one sentence

mapObject walks an object and returns an object. Use it to rename keys or change every value.

## Like this in real life

A form where you uppercase every label but keep the same boxes.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload mapObject ((value, key) -> {
  (upper(key as String)): value
})
```

## Remember

map = lists. mapObject = objects. Mixing them is a common interview fail.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
