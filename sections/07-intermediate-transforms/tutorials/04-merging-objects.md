# Merging objects

*Section: Group, reduce, merge, and update · Interview Q25 · easy words*

## In one sentence

++ copies keys. If both sides have the same key, the right side wins. That merge is shallow.

## Like this in real life

Overlaying a new config file on an old one. retries: 5 replaces retries: 2. Nested objects are replaced whole, not mixed, unless you use mergeWith.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import mergeWith from dw::core::Objects
output application/json
---
{
  concat: { a: 1, b: 2 } ++ { b: 9, c: 3 },     // {a:1, b:9, c:3} — right wins
  merged: { a: {x: 1} } mergeWith { a: {y: 2} } // deep merge depending on values
}
```

## Remember

mergeWith is the deep-merge follow-up.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
