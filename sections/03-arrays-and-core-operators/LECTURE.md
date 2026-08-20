# Section — Arrays: map, filter, and indexes

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Use `map`, `filter`, `$` / `$$`, `sizeOf`, `isEmpty`, and `flatten`.
- Explain when named lambda parameters are clearer than `$`.

## Suggested video breakdown

- Demo Lab 01 (map shape) and Lab 02 (filter) on camera.
- Assign Labs 09–10, 14–15 as homework.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 01
- Lab 02
- Lab 09
- Lab 10
- Lab 14
- Lab 15

## Teach these interview questions

### Q8. How do `map` and `filter` work on arrays?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
payload.orders
  filter ((order) -> order.status == "PAID")
  map ((order) -> {
    id: order.id,
    total: order.amount
  })
```

- `$` is the current item, `$$` is the index: `payload map { index: $$, value: $ }`.
- `filter` keeps elements where the predicate is `true`.

---

### Q15. What does `sizeOf` and `isEmpty` do?

**Answer:**

```dataweave
sizeOf(payload.items)     // array length, object key count, or string length
isEmpty(payload.items)    // true for [], {}, "", or null in many cases
```

Prefer `isEmpty` over `sizeOf(x) == 0` in interviews.

---

### Q35. Explain `$`, `$$`, and `$$$` in lambdas.

**Answer:** Implicit parameters in function literals:

- `$` — first argument (item / value)
- `$$` — second (index / key depending on function)
- `$$$` — third (index in `mapObject` / `pluck`)

```dataweave
["a", "b"] map upper($)
{ a: 1 } mapObject ((v, k) -> { (k): v }) 
```

Interview tip: named parameters (`(item, index) ->`) are clearer than `$`/`$$`.

---
