# Transform Message vs #[...]

*Section: Joins, modules, and Mule context · Interview Q18 · easy words*

## In one sentence

Transform Message is a full script with preview. #[...] is a tiny DataWeave expression inside another processor.

## Like this in real life

Transform Message is a full kitchen. #[payload.orderId] is grabbing one spice while the soup is already cooking.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Transform Message: whole script.
// Set Payload expression: #[payload.orderId]  (one expression, not a full mapping)
```

## Remember

Both are DataWeave 2 in Mule 4. Big mappings belong in Transform Message.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
