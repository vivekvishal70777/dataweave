# JSON to XML and back

*Section: JSON, XML, and CSV mappings · Interview Q14 · easy words*

## In one sentence

Change the output MIME type and shape a tree. XML must have exactly one root.

## Like this in real life

JSON is Lego bricks in a bag. XML is the same bricks snapped under one lid. No lid, or two lids, and XML is invalid.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/xml
---
orders: {
  order: payload map {
    id: $.id,
    amount: $.amount
  }
}
```

## Remember

JSON → XML = output application/xml plus a root key. XML → JSON = output application/json and pick elements.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q14). Then try the lab listed for this section.
