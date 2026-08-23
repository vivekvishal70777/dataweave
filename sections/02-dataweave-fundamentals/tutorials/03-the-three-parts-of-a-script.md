# The three parts of a script

*Section: DataWeave 2.0 fundamentals · Interview Q3 · easy words*

## In one sentence

Every script has a header, a line of dashes, then a body that becomes the output.

## Like this in real life

Like a letter: address at the top (version and output type), a line, then the message.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  greeting: "Hello " ++ payload.name
}
```

## Remember

Say it out loud: percent dw two point oh, output, dash dash dash, then the expression.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q3). Then try the lab listed for this section.
