# Values::mask vs recursive mask

*Section: Industry operators, message, and MIME · Interview Q77 · easy words*

## In one sentence

Known paths → update or mask. Unknown depth → recursive match on types (Lab 39).

## Like this in real life

If secrets always sit in customer.ssn, use a precise marker. If secrets hide anywhere, search the whole house.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// Known path: mask / update.
// Unknown depth: recursive match (Lab 39).
payload update {
  case .ssn -> "****"
}
```

## Remember

Mask before logging.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q77). Then try the lab listed for this section.
