# Section — Dates, pattern matching, and try

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Parse and format dates; use period literals.
- Pattern-match with `match`.
- Catch coercion errors with `try` / `orElse` (not Mule error handlers).

## Suggested video breakdown

- Lab 27 mixed dates is the interview favorite — type it slowly.
- Contrast `default` (nulls) vs `try` (errors).

## Labs in this section

Student starters live under `student/labs/`.

- Lab 27
- Lab 28
- Lab 33
- Lab 52

## Teach these interview questions

### Q28. How does pattern matching (`match`) work?

**Answer:**

```dataweave
payload.status match {
  case "NEW" -> "created"
  case "PAID" -> "completed"
  case s if s startsWith "ERR" -> "failed"
  case n is Number -> "numeric-status"
  else -> "unknown"
}
```

`match` is exhaustive-style pattern matching: literals, types (`is`), conditions, and `else`.

---

### Q29. How do you handle errors in DataWeave (`try`)?

**Answer:**

```dataweave
%dw 2.0
import try, orElse, orElseTry from dw::Runtime
output application/json
---
{
  n: try(() -> payload.age as Number) orElse 0,
  safe: try(() -> 1 / payload.divisor)
}
```

`try` returns `{ success: true, result: ... }` or `{ success: false, error: ... }`. Combine with `orElse` for fallbacks. This is **not** a Mule error handler; it only catches failures **inside** the script.

---

### Q30. How do you work with dates and periods?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  today: now(),
  formatted: now() as String {format: "dd-MMM-yyyy"},
  parsed: "2026-08-20" as Date {format: "yyyy-MM-dd"},
  nextWeek: (now() as Date) + |P7D|,
  ageDays: |P1Y2M| 
}
```

Date literals use pipes: `|2026-08-20|`, `|P7D|` (ISO-8601 periods). Rounding and timezone functions live in `dw::core::Dates`.

---
