# write and read

*Section: Strings, numbers, and conditionals · Interview Q19 · easy words*

## In one sentence

write turns a value into text or bytes. read parses text or bytes back into data. They do not change the script’s output MIME by themselves.

## Like this in real life

write is photocopying a form to PDF in your hand. output application/json is the stamp on the envelope you actually mail.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  asText: write(payload.order, "application/json", { indent: false }),
  nested: read(payload.jsonBlob, "application/json")
}
```

## Remember

write(payload) on a huge file can break streaming.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q19). Then try the lab listed for this section.
