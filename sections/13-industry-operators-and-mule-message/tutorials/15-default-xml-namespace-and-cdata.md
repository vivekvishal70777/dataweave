# Default XML namespace and CDATA

*Section: Industry operators, message, and MIME · Interview Q75 · easy words*

## In one sentence

Default xmlns still needs ns and prefix#Element. The URI must match. CDATA is usually just text.

## Like this in real life

A nameless family still has an address (URI). You give them a nickname (prefix) in DataWeave.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
ns ord http://acme.com/order
output application/xml
---
{
  ord#PurchaseOrder @(id: payload.id): {
    ord#Note: payload.note
  }
}
```

## Remember

Mixed content is messy. Push back on the contract if you can.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q75). Then try the lab listed for this section.
