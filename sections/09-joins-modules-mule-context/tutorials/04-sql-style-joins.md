# SQL-style joins

*Section: Joins, modules, and Mule context · Interview Q37 · easy words*

## In one sentence

leftJoin (and friends) live in dw::core::Arrays. Result items look like { l: left, r: right }.

## Like this in real life

Orders on the left, customers on the right. Missing customer means r is null.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
leftJoin(payload.orders, payload.customers,
  (o) -> o.customerId,
  (c) -> c.id)
```

## Remember

Import leftJoin. Then map to a flat { orderId, customerName }.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q37). Then try the lab listed for this section.
