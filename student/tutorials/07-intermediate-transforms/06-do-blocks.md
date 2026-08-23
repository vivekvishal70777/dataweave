# do blocks

*Section: Group, reduce, merge, and update · Interview Q27 · easy words*

## In one sentence

do makes a tiny local header (var/fun) so the main header stays clean.

## Like this in real life

Scratch paper inside one map step: compute tax, then output the line. Throw the scratch paper away.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.orders map (order) -> do {
  var tax = order.amount * 0.18
  ---
  { id: order.id, total: order.amount + tax }
}
```

## Remember

Use do when a map body would be messy.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q27). Then try the lab listed for this section.
