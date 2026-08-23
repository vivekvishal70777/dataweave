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

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
