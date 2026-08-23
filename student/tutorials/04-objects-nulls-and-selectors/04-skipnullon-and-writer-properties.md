# skipNullOn and writer properties

*Section: Objects, nulls, and selectors · Interview Q20 · easy words*

## In one sentence

Writer properties sit on the output line. skipNullOn="everywhere" hides null fields in JSON or XML.

## Like this in real life

If a field is empty, do not print a blank line on the invoice.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json skipNullOn="everywhere", indent=false
---
{ a: 1, b: null }   // { "a": 1 }
```

## Remember

indent=false makes compact JSON. CSV uses header=true and separator.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
