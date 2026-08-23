# replace, find, substring

*Section: Industry operators, message, and MIME · Interview Q68 · easy words*

## In one sentence

replace can use regex. find extracts matches. substringBefore("-") takes the SKU family.

## Like this in real life

Black out invoice numbers in a comment. Pull INV-123 out of a sentence.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  redacted: replace(payload.notes, /INV-\d+/, "REDACTED"),
  ids: payload.notes find /INV-\d+/,
  family: substringBefore(payload.sku, "-"),
  trimmed: trim(payload.name)
}
```

## Remember

matches = whole string. find = pieces inside.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
