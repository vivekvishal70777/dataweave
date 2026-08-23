# Section — Strings, numbers, and conditionals

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Concatenate with `++` vs add with `+`.
- Split, join, and change case.
- Write if/else expressions (no Java ternary).

## Suggested video breakdown

- Trap: `+` on strings. Demo the error, then fix with `++`.
- Lab 13 HTTP retry class is the if/else pattern. Mention `write`/`read` (Q19) as a production follow-up.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 06
- Lab 07
- Lab 08
- Lab 13
- Lab 17

## Teach these interview questions

### Q10. How do you concatenate strings and arrays?

**Answer:**

- Strings: `++` (`"Hello" ++ " " ++ "World"`)
- Arrays: `++` (`[1, 2] ++ [3]`)
- Objects: `++` merges keys (right side wins on conflict)

`+` is numeric addition, not concatenation.

---

### Q12. How do you write if/else in DataWeave?

**Answer:** DataWeave uses expressions, not statements:

```dataweave
if (payload.age >= 18) "adult"
else if (payload.age >= 13) "teen"
else "child"
```

There is no ternary `? :` operator like Java.

---

### Q16. How do you split, join, and change case of strings?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  parts: payload.csvLine splitBy ",",
  csv: ["a", "b"] joinBy ",",
  upper: upper(payload.name),
  lower: lower(payload.name),
  cap: capitalize(payload.name)
}
```

`splitBy` returns an array; `joinBy` builds a string. Industry follow-ups from `dw::core::Strings`: `trim`, `replace`, `substringAfter` / `substringBefore`, `pad`, `repeat`, and regex `find` / `scan` (see Q68).

---

### Q19. How do you `write` and `read` data inside a script?

**Answer:** Use `write(value, mimeType, properties)` to serialize a value to String/Binary without changing the Transform **output** MIME, and `read(binaryOrString, mimeType)` to parse. Typical interview case: log a JSON snapshot, or parse a JSON **string field** inside XML/CSV.

```dataweave
%dw 2.0
output application/json
---
{
  asText: write(payload.order, "application/json", { indent: false }),
  nested: read(payload.jsonBlob, "application/json")
}
```

This is **not** the same as `output application/json` on the script (that sets the Mule payload writer). Follow-up: huge `write(payload)` can break streaming.

---
