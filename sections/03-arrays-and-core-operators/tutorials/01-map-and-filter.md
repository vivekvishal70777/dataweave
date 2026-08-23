# map and filter

*Section: Arrays: map, filter, and indexes · Interview Q8 · easy words*

## In one sentence

filter keeps some items. map changes each item. You often filter first, then map.

## Like this in real life

A conveyor belt of orders. Filter = throw away unpaid. Map = stick a shipping label on each remaining box.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload.orders
  filter ((order) -> order.status == "PAID")
  map ((order) -> {
    id: order.id,
    total: order.amount
  })
```

## Remember

Name the item (order) -> in interviews. $ is shorter but harder to read.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q8). Then try the lab listed for this section.
