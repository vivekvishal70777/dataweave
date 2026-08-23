# Reader and writer properties

*Section: Streaming, crypto, modules, and pitfalls · Interview Q53 · easy words*

## In one sentence

Readers parse input (CSV header, XML encoding). Writers shape output (indent, skipNullOn).

## Like this in real life

Incoming stamp vs outgoing stamp. CSV separator is often on the MIME type of the message, not only in the script.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/xml writeDeclaration=true, encoding="UTF-8"
---
root: payload
```

## Remember

JSON streaming, XML writeDeclaration, CSV header=true.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q53). Then try the lab listed for this section.
