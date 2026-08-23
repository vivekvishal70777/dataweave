# flatMap

*Section: Advanced: recursion, namespaces, diffs · Interview Q43 · easy words*

## In one sentence

flatMap is map, then flatten one level. Perfect for one order → many line rows.

## Like this in real life

Each pizza order opens into several slices on a single serving tray, not a tray of trays.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.orders flatMap ((order) ->
  order.items map (item) -> {
    orderId: order.id,
    sku: item.sku
  }
)
```

## Remember

flatten(payload map ...) is the same idea.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q43). Then try the lab listed for this section.
