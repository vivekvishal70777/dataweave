# try vs On Error

*Section: Industry operators, message, and MIME · Interview Q73 · easy words*

## In one sentence

try is inside the script (bad coerce). On Error is the flow (HTTP 500, timeout).

## Like this in real life

Burnt toast = try, serve jam. House fire = fire alarm (On Error), not more jam.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload map (row) -> {
  sku: row.sku,
  qty: try(() -> row.qty as Number) orElse 0
}
```

## Remember

error.errorType and error.errorMessage.payload live in On Error scopes.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q73). Then try the lab listed for this section.
