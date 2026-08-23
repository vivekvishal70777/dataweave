# Missing fields and null

*Section: Objects, nulls, and selectors · Interview Q11 · easy words*

## In one sentence

default replaces null. The safe selector ? stops you crashing if a parent is missing.

## Like this in real life

If the guest left the email blank, print noreply. If they have no address at all, do not look for city inside nothing.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.email default "unknown"
payload.address.city default ""
payload.address.?city          // null-safe selector; returns null if address is null
```

## Remember

default does not catch as Number failures. That is try.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q11). Then try the lab listed for this section.
