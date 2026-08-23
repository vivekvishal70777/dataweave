# Section — Joins, modules, and Mule context

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Read `vars`, `attributes`, and properties.
- Import modules and join arrays (or index with `groupBy`).
- Know when not to call Java or `lookup` inside `map`.

## Suggested video breakdown

- Lab 32 (join via groupBy) after Lab 31 (leftJoin) — same result, better interview story.
- Warn about N+1 `lookup` (Q40).

## Labs in this section

Student starters live under `student/labs/`.

- Lab 31
- Lab 32
- Lab 34
- Lab 45

## Teach these interview questions

### Q17. How do you read Mule variables, attributes, and properties in DataWeave?

**Answer:**

```dataweave
vars.customerId
attributes.headers["content-type"]
attributes.queryParams.page
p("http.host")               // from configuration properties
Mule::p("api.version")       // same idea in some contexts
```

In Transform Message you can also map from the **input graph** (`payload`, `vars`, `attributes`). HTTP Listener extras interviewers want: `attributes.method`, `attributes.requestPath` / `rawRequestUri`, `attributes.uriParams.orderId`, `attributes.queryParams.page`, `attributes.headers['authorization']` (often lower-cased). `error.errorType` / `error.errorMessage.payload` belong in **On Error** scopes, not in a happy-path script (see Q73).

---

### Q18. What is the difference between Transform Message and a DataWeave expression in a Set Payload?

**Answer:**

- **Transform Message**: full script with header, preview, metadata, multiple outputs (`payload`, `variables`).
- **`#[...]` expression**: a DataWeave expression (often without a full header) used inline, e.g. `#[payload.orderId]`.

Both use DataWeave 2 in Mule 4.

---

### Q34. What are DataWeave modules? How do you import them?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
import someFun from modules::MyModule
import dw::core::Arrays
output application/json
---
Arrays.drop(payload, 2)
```

Built-in modules include `dw::Core`, `dw::core::Strings`, `Arrays`, `Objects`, `Dates`, `Periods`, `Binaries`, `URL`, `Crypto`, `Runtime`, `dw::util::Values`. Custom modules are `.dwl` files under `src/main/resources/modules`.

---

### Q37. How do you join two arrays like a SQL join?

**Answer:** `dw::core::Array` join functions:

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
leftJoin(payload.orders, payload.customers,
  (o) -> o.customerId,
  (c) -> c.id)
```

Also: `join` (inner), `outerJoin`, `leftJoin`. Result items look like `{ l: leftItem, r: rightItem }`. For simple lookups, `groupBy` plus indexing is common.

---

### Q38. How do you call Java from DataWeave? When should you not?

**Answer:**

```dataweave
%dw 2.0
import java!java::util::UUID
output application/json
---
{
  id: UUID::randomUUID() as String
}
```

You can invoke static methods and, with care, instance methods. Prefer pure DataWeave for transformations. Use Java for libraries you cannot reproduce (special crypto, proprietary parsers). Java calls add coupling and can hurt streaming/performance.

---

### Q39. What is the difference between `startsWith`, `contains`, and `matches`?

**Answer:**

```dataweave
"MuleSoft" startsWith "Mule"     // true
["a", "b"] contains "a"          // true
"abc123" matches /[a-z]+[0-9]+/  // true (full match vs regex)
```

`matches` uses a regular expression against the whole string. For partial regex, use `payload find /pattern/` or `contains` for substrings.

---

### Q40. How do you use `lookup` (Mule 4) vs DataWeave-only alternatives?

**Answer:** Flow `lookup` (from `dw::Runtime` / Mule functions) invokes **another flow** and returns its payload—useful for enrichment, but it is synchronous and expensive.

```dataweave
lookup("get-customer-flow", { id: payload.customerId })
```

Prefer **lookup tables as objects**, `groupBy`, database/HTTP connectors **outside** Transform Message, or `Mule::p()` for config. Mention in interviews: do not hide heavy I/O inside every `map` iteration if you can batch it.

---
