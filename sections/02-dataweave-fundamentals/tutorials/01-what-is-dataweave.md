# What is DataWeave?

*Section: DataWeave 2.0 fundamentals · Interview Q1 · easy words*

## In one sentence

DataWeave is MuleSoft’s language for changing data from one shape to another.

## Like this in real life

Think of a translator. A Salesforce Contact comes in as JSON. Your API wants a smaller JSON. DataWeave does that translation.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  name: payload.Name,
  email: payload.Email
}
```

## Remember

In Mule 4 you write DataWeave in Transform Message, and also as #[...] in other steps. It is not Java.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q1). Then try the lab listed for this section.
