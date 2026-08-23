# Calling Java

*Section: Joins, modules, and Mule context · Interview Q38 · easy words*

## In one sentence

You can import java!... and call static methods. Prefer pure DataWeave for mapping.

## Like this in real life

Asking a neighbour (Java) to lend a special tool. Do not ask them to butter every slice in a map of 10,000 rows.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import java!java::util::UUID
output application/json
---
{
  id: UUID::randomUUID() as String
}
```

## Remember

Java can hurt streaming and tests. Use it for libraries DW cannot replace.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q38). Then try the lab listed for this section.
