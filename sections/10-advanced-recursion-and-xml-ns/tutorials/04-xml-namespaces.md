# XML namespaces

*Section: Advanced: recursion, namespaces, diffs · Interview Q44 · easy words*

## In one sentence

ns prefix URI then prefix#Element. The prefix is yours. The URI must match the XML.

## Like this in real life

Two families both named “Order.” The URI is the family address so you do not mix them.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
ns ns0 http://example.com/order
output application/xml
---
ns0#Orders: {
  ns0#Order @(id: payload.id): {
    ns0#Amount: payload.amount
  }
}
```

## Remember

SOAP: Envelope, Body, then your element. Repeating lines use *prefix#Line.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
