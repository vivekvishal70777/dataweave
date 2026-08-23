# Section — DataWeave 2.0 fundamentals

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Describe DataWeave and the Mule 4 script header.
- Declare `var` and `fun`, and coerce types with `as`.
- Contrast DataWeave 1.0 and 2.0 at interview level.

## Suggested video breakdown

- Record one short video per question cluster: what DW is, 1 vs 2, script shape, vars, functions, types, `as`.
- Live-type the hello-world script from Q3.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 03
- Lab 05
- Lab 08
- Lab 13

## Teach these interview questions

### Q1. What is DataWeave?

**Answer:** DataWeave is MuleSoft’s functional data transformation language. In Mule 4 it is the primary way to map, filter, enrich, and convert payloads between formats such as JSON, XML, CSV, Java objects, and strings. Scripts run inside the Transform Message component and also as DataWeave expressions (`#[...]`) in other processors.

---

### Q2. What is the difference between DataWeave 1.0 and DataWeave 2.0?

**Answer:**

| Area | DataWeave 1.0 (Mule 3) | DataWeave 2.0 (Mule 4) |
| --- | --- | --- |
| Header | `%dw 1.0` | `%dw 2.0` |
| Language | MEL + DW 1.0 | DataWeave everywhere (`#[...]`) |
| Operators | `map` / `mapObject` syntax differences | Unified functions, modules (`dw::core::*`) |
| Null handling | More implicit | Explicit (`default`, `?`, `try`) |
| Output | `%output application/json` | `output application/json` |

Interviews almost always expect **DataWeave 2.0**.

---

### Q3. What is the basic structure of a DataWeave script?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  greeting: "Hello " ++ payload.name
}
```

- Header: version, output MIME type, imports, functions, variables.
- `---` separates header from body.
- Body: the expression that becomes the output payload.

---

### Q4. How do you declare a variable in DataWeave?

**Answer:** Use `var` in the header (script-scoped) or inside a `do` block.

```dataweave
%dw 2.0
output application/json
var taxRate = 0.18
---
{
  total: payload.amount * (1 + taxRate)
}
```

Variables are immutable. Comments: `//` and `/* */` in header or body.

---

### Q5. How do you define a custom function?

**Answer:**

```dataweave
%dw 2.0
output application/json
fun fullName(first: String, last: String) = first ++ " " ++ last
---
fullName(payload.firstName, payload.lastName)
```

Functions can be overloaded by argument types and arity.

---

### Q6. What are the main DataWeave data types?

**Answer:** `String`, `Boolean`, `Number`, `Date`, `DateTime`, `LocalDateTime`, `Time`, `Period`, `Regex`, `Array`, `Object`, `Null`, `Binary`, `Type`, and `Any`. Type annotations are optional but useful in interviews and modules:

```dataweave
fun add(a: Number, b: Number): Number = a + b
```

---

### Q7. How do you convert types (`as`)?

**Answer:** Use `as` for coercion:

```dataweave
payload.age as Number
payload.createdAt as Date {format: "yyyy-MM-dd"}
payload as String {encoding: "UTF-8"}
```

If coercion fails, the script errors unless you use `try` / `default`.

---
