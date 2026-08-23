# Selectors (dot, brackets, star, dots)

*Section: Objects, nulls, and selectors · Interview Q13 · easy words*

## In one sentence

Dot is a field. Brackets are index or odd names. Star is repeating children. Two dots means “search descendants.”

## Like this in real life

A filing cabinet. customer.name is a labelled drawer. [0] is the first folder. .*item is every “item” tab. ..id is “find every id sticker in the whole cabinet.”

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  name: payload.customer.name,
  first: payload[0],
  hyphen: payload["first-name"],
  items: payload.*item,
  anyId: payload..id
}
```

## Remember

XML attributes use at-sign: order.@id.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q13). Then try the lab listed for this section.
