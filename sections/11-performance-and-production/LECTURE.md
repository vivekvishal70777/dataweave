# Section — Streaming, crypto, modules, and pitfalls

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Name what breaks DataWeave streaming.
- Hash vs HMAC; binary/Base64 care.
- Extract a reusable `.dwl` module.

## Suggested video breakdown

- Whiteboard the performance list from Q58 — this is a closing-section video.
- Optional: show a tiny Pricing.dwl module (Q46).

## Labs in this section

Student starters live under `student/labs/`.

- Lab 45

## Teach these interview questions

### Q41. How does DataWeave streaming work? When does it break?

**Answer:** For large JSON/XML/CSV, DataWeave can stream if the script is **incremental** (e.g. `payload map ...` without needing the whole document). Streaming **breaks** when you:

- Use `sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, `reduce` on the whole payload
- Access the same payload twice
- Use random index access on the full array
- Convert the entire payload to String

Interview talking point: design maps as **one-pass** `map`/`filter` when files are large; set streaming in the MIME type / reader config.

---

### Q45. Explain `dw::Crypto` hashing vs HMAC. When is each used?

**Answer:**

```dataweave
%dw 2.0
import dw::Crypto
output application/json
---
{
  sha: Crypto::hashWith(payload as Binary, "SHA-256"),
  hmac: Crypto::HMACBinary(payload as Binary, "secret" as Binary, "HmacSHA256")
}
```

Hashing is one-way checksums (file integrity). HMAC signs with a secret (webhook verification). Never roll your own encoding; watch Binary vs String and Base64 wrapping (`dw::core::Binaries::toBase64`).

---

### Q46. How do you write a reusable `.dwl` module and unit-test it?

**Answer:**

`src/main/resources/modules/Pricing.dwl`:

```dataweave
%dw 2.0
fun withTax(amount: Number, rate: Number = 0.18) = amount * (1 + rate)
```

Import: `import withTax from modules::Pricing`.

Tests: MUnit with DataWeave assertions, or a `src/test/resources` script. Interview plus: default argument values, type signatures, and keeping modules **pure** (no `lookup`, no `now()` if you want determinism—inject time as a parameter).

---

### Q52. How do you process multipart / binary / Base64 in DataWeave?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Binaries
output application/json
---
{
  b64: toBase64(payload as Binary),
  bytes: fromBase64(vars.fileBase64),
  asText: (payload as Binary) as String {encoding: "UTF-8"}
}
```

For multipart, Mule gives `parts` (e.g. `payload.parts.file.content`). Avoid loading huge binaries as String. Set `output application/octet-stream` when the result must stay binary.

---

### Q53. What are reader/writer properties you should mention for XML, JSON, and CSV?

**Answer:**

**JSON:** `streaming`, `indexed`, `duplicateKeyAsArray`

**XML:** `ignoreRootElement`, `nullValueOn`, `writeDeclaration`, `encoding`, `indent`, `escapeCR`

**CSV:** `header`, `separator`, `quote`, `escape`, `bodyStartLineNumber`, `ignoreEmptyLine`

Example:

```dataweave
%dw 2.0
output application/xml writeDeclaration=true, encoding="UTF-8"
---
root: payload
```

Reader properties are often set on the **MIME type of the incoming message**, not only in the script header.

---

### Q58. What performance pitfalls do interviewers expect you to name?

**Answer:**

1. `groupBy` / `orderBy` on huge in-memory arrays  
2. Nested `filter`/`map` causing O(n²) (use `groupBy` to index first)  
3. `lookup` inside `map` (N+1 flow calls)  
4. Repeated `payload as String` then parse  
5. XML `..` descendant selector on large documents  
6. Breaking streaming (see Q41)  
7. Recursive functions without considering depth  
8. Converting entire files to Java `HashMap` unnecessarily  

Fix pattern: index the right-hand collection once (`groupBy` id), then `map` the left side with O(1)/O(k) lookups.

---
