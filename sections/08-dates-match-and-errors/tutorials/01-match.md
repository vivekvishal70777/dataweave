# match

*Section: Dates, pattern matching, and try · Interview Q28 · easy words*

## In one sentence

match picks a branch by value, type, or a condition. Always have else.

## Like this in real life

A sorting hat: 2xx → ok, 4xx → client, else → other.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload.status match {
  case "NEW" -> "created"
  case "PAID" -> "completed"
  case s if s startsWith "ERR" -> "failed"
  case n is Number -> "numeric-status"
  else -> "unknown"
}
```

## Remember

This is not Java switch with break. It is an expression.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q28). Then try the lab listed for this section.
