# XML attributes vs elements

*Section: JSON, XML, and CSV mappings · Interview Q33 · easy words*

## In one sentence

@id is an attribute on the tag. A child tag is an element. *item is repeating children.

## Like this in real life

<order id="O-1"> — id is written on the sticker. <amount>50</amount> is a box inside.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  id: payload.order.@id,           // attribute
  name: payload.order.customer,    // element text / child
  items: payload.order.*item       // repeating child elements
}
```

## Remember

To write attributes: order @(id: payload.id): { ... }

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
