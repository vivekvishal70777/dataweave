# Section — Objects, nulls, and selectors

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/04-objects-nulls-and-selectors/README.md`](../../student/tutorials/04-objects-nulls-and-selectors/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Choose `.` vs `[]` vs `.*` vs `..`.
- Handle missing data with `default` and `?`.
- Transform objects with `mapObject` and `pluck`.

## Suggested video breakdown

- Whiteboard the selector table from Q13.
- Show `skipNullOn` from Q20 as a writer-property demo.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 04
- Lab 05
- Lab 16
- Lab 18

## Interview talking points for this section

Teach the **concept**, then demo, then lab. Use these Q&A as the phrases to say on camera —
not as a second lecture series. One 20–40s “if they ask this in an interview…” close per video is enough.

### Q9. What is `pluck`?

**Answer:** `pluck` turns an object into an array by iterating keys/values.

```dataweave
{ a: 1, b: 2 } pluck ((value, key, index) -> { k: key, v: value })
// [{k: "a", v: 1}, {k: "b", v: 2}]
```

Use it when you need an array from an object’s fields.

---

### Q11. How do you handle missing fields and nulls?

**Answer:**

```dataweave
payload.email default "unknown"
payload.address.city default ""
payload.address.?city          // null-safe selector; returns null if address is null
```

`default` replaces `null` (and missing values that evaluate to null). It does **not** catch errors—use `try` for that.

---

### Q13. What is the difference between `.` and `[]` selectors?

**Answer:**

- `payload.customer.name` — named key selector.
- `payload[0]` — array index.
- `payload["first-name"]` — key that is not a valid identifier.
- `payload.*item` — multi-value selector (all `item` children, useful in XML).
- `payload..id` — descendants selector (all `id` fields at any depth).

---

### Q20. What does `output application/json skipNullOn="everywhere"` do?

**Answer:** Writer properties control serialization. `skipNullOn="everywhere"` omits fields whose values are `null` from JSON/XML output. Other common properties:

- `indent=false` — compact JSON
- `duplicateKeyAsArray=true` — XML
- `header=true` / `separator=","` — CSV

```dataweave
%dw 2.0
output application/json skipNullOn="everywhere", indent=false
---
{ a: 1, b: null }   // { "a": 1 }
```

---

### Q21. Explain `mapObject`. When do you use it instead of `map`?

**Answer:** `map` iterates **arrays** and returns an **array**. `mapObject` iterates **objects** and returns an **object**.

```dataweave
payload mapObject ((value, key) -> {
  (upper(key as String)): value
})
```

Use `mapObject` to rename keys, drop/keep fields, or transform every value while keeping object shape.

---
