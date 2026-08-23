# application/java

*Section: Industry operators, message, and MIME · Interview Q70 · easy words*

## In one sentence

After many connectors, payload is a Java Map/List, not a JSON string. Selectors still use dot.

## Like this in real life

The same shopping list, written in pencil (Java) not printed as JSON. You still read “milk.”

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// After a Java connector, payload is often application/java.
// You still write: payload.Account.Name
{
  name: payload.Name
}
```

## Remember

Do not payload as String then parse unless you must.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q70). Then try the lab listed for this section.
