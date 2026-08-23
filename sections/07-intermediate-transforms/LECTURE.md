# Section — Group, reduce, merge, and update

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/07-intermediate-transforms/README.md`](../../student/tutorials/07-intermediate-transforms/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Use `groupBy`, `orderBy`, `distinctBy`, `reduce`, and `flatMap`.
- Merge objects and update nested fields.
- Scope locals with `do`.

## Suggested video breakdown

- Hero demo: Lab 20 totals per customer (coerce string amounts), then Lab 23 flatMap lines.
- Show `update` and mention Mule 4.3+ (Q26).

## Labs in this section

Student starters live under `student/labs/`.

- Lab 19
- Lab 20
- Lab 21
- Lab 22
- Lab 23
- Lab 24
- Lab 25
- Lab 26
- Lab 35
- Lab 36

## Teach these interview questions

### Q22. How do `groupBy`, `orderBy`, and `distinctBy` work?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  byCity: payload groupBy ((c) -> c.city),
  sorted: payload orderBy ((c) -> c.name),
  unique: payload distinctBy ((c) -> c.email)
}
```

`groupBy` returns an **object** whose keys are group names and values are arrays.

---

### Q23. Explain `reduce`. Give an example of a sum and of building an object.

**Answer:** `reduce` folds an array into a single value.

```dataweave
[1, 2, 3] reduce ((item, acc = 0) -> acc + item)   // 6

payload reduce ((item, acc = {}) -> acc ++ {
  (item.id): item.name
})
```

If you omit the accumulator initializer, the first element is the seed and iteration starts at the second element.

---

### Q24. How do you flatten nested arrays?

**Answer:**

```dataweave
flatten([[1, 2], [3], [4, 5]])     // [1, 2, 3, 4, 5]
```

`flatten` is only one level. For deeper trees, write a recursive function or flatten in steps.

---

### Q25. How do you merge two objects? What happens with duplicate keys?

**Answer:** `++` and `dw::core::Objects::mergeWith`:

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

`++` is a **shallow** merge (right key overwrites the whole nested object). `mergeWith` is the interview follow-up for **deep** merge of nested objects. Minus on objects (`payload - "password"`) drops keys. For arrays of objects, merge by `id` is Lab 49, not `++`.

---

### Q26. How do you update a nested field without rebuilding the whole object?

**Answer:** Use the `update` operator (DataWeave 2.3+ / Mule 4.3+):

```dataweave
%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
  case .items[0].qty -> $ + 1
}
```

This is preferred in interviews over copying every field by hand.

---

### Q27. What is a `do` block and why is it useful?

**Answer:** `do` creates a local scope for `var` / `fun` so the header stays clean.

```dataweave
payload.orders map (order) -> do {
  var tax = order.amount * 0.18
  ---
  { id: order.id, total: order.amount + tax }
}
```

Use it for intermediate values inside `map`/`filter`.

---

### Q36. How do you filter object keys dynamically?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Objects
output application/json
---
payload filterObject ((value, key) -> !(["password", "ssn"] contains (key as String)))
```

`filterObject` keeps entries where the predicate is true. `dw::util::Values::mask` is another option for hiding fields.

---
