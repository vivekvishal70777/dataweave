# filterObject

*Section: Group, reduce, merge, and update · Interview Q36 · easy words*

## In one sentence

filterObject keeps object keys where a test is true. Use it to drop password and ssn.

## Like this in real life

Redacting a form before you photocopy it for the log file.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Objects
output application/json
---
payload filterObject ((value, key) -> !(["password", "ssn"] contains (key as String)))
```

## Remember

Compare lower(k as String). Keys are not always plain strings.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
