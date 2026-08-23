# lookup vs doing it in DataWeave

*Section: Joins, modules, and Mule context · Interview Q40 · easy words*

## In one sentence

lookup calls another Mule flow and waits. Inside map it becomes N+1 slow calls.

## Like this in real life

Phoning the warehouse once per line on a 5,000-line order. Fetch the catalog first, then join in DataWeave.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
lookup("get-customer-flow", { id: payload.customerId })
```

## Remember

Index with groupBy, or enrich before Transform Message.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q40). Then try the lab listed for this section.
