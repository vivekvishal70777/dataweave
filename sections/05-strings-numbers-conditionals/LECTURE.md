# Section — Strings, numbers, and conditionals

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Concatenate with `++` vs add with `+`.
- Split, join, and change case.
- Write if/else expressions (no Java ternary).

## Suggested video breakdown

- Trap: `+` on strings. Demo the error, then fix with `++`.
- Lab 13 grades as the if/else pattern students will reuse.

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

`splitBy` returns an array; `joinBy` builds a string.

---

### Q19. How do you add comments in DataWeave?

**Answer:**

```dataweave
// single line
/* multi
   line */
```

Comments can appear in header and body.

---
