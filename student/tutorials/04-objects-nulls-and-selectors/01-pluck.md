# pluck

*Section: Objects, nulls, and selectors · Interview Q9 · easy words*

## In one sentence

pluck walks an object and returns an array of whatever you build from each key and value.

## Like this in real life

A form with fields Name, Age, City. pluck turns it into a list of rows for a spreadsheet.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
{ a: 1, b: 2 } pluck ((value, key, index) -> { k: key, v: value })
// [{k: "a", v: 1}, {k: "b", v: 2}]
```

## Remember

map is for arrays. mapObject is for objects that stay objects. pluck is object → array.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
