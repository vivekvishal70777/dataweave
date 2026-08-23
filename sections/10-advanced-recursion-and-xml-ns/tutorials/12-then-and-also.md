# then and also

*Section: Advanced: recursion, namespaces, diffs · Interview Q56 · easy words*

## In one sentence

then passes the left value into the next expression as $. also is rare. Prefer a clear do block if chaining gets clever.

## Like this in real life

then is “take this tray and make a box { count, items }.”

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.orders
  filter ($.active)
  then (orders) -> { count: sizeOf(orders), orders: orders }
```

## Remember

Readable beats clever in interviews.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q56). Then try the lab listed for this section.
