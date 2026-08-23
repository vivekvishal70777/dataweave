# Join tables that arrived together

*Section: DataWeave Mapping · easy words*

## In one sentence

`groupBy` the small table by id, then `map` the big table. That is a hash join.

## Like this in real life

Index the customer list once. For each order, pick the card from the index. Do not phone HQ per order.

## Tiny example

```dataweave
var byId = payload.customers groupBy $.id
---
payload.orders map (o) -> o ++ { email: (byId[o.customerId][0].email) default "unknown" }
```

## Remember

Missing match → `default`. Outer merge is Lab 84 / Lab 49.

Lab 59, 63, 64.
