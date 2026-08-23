# Section — Industry operators, message, and MIME

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/13-industry-operators-and-mule-message/README.md`](../../student/tutorials/13-industry-operators-and-mule-message/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Use Arrays helpers: maxBy, firstWith, zip, ranges.
- Shift timezones; replace/find; Transform Message multiple targets.
- Distinguish try vs Mule On Error, Java MIME, and DW vs Batch vs For Each.

## Suggested video breakdown

- These are the production topics the first 60 questions only hinted at.
- Demo Lab 55 (maxBy) and Lab 56 (IST). Assign zip and TM dual-target as homework.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 55
- Lab 56
- Lab 57
- Lab 58

## Interview talking points for this section

Teach the **concept**, then demo, then lab. Use these Q&A as the phrases to say on camera —
not as a second lecture series. One 20–40s “if they ask this in an interview…” close per video is enough.

### Q61. What `dw::core::Arrays` helpers do interviewers expect besides map/filter?

**Answer:** Import `dw::core::Arrays` (Mule 4.3+ / current core):

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy $.amount,
  cheapest: payload minBy $.amount,
  firstPaid: payload firstWith ((o) -> o.status == "PAID"),
  anyOver: payload some ((o) -> (o.amount as Number) > 1000),
  allPositive: payload every ((o) -> (o.amount as Number) > 0),
  idx: indexOf(payload, ((o) -> o.id == "O1")),
  countPaid: payload countBy ((o) -> o.status == "PAID")
}
```

`maxBy` / `minBy` return the **item**, not the number. Empty arrays: guard with `isEmpty` or `default`.

---

### Q62. How do ranges and `slice` work?

**Answer:**

```dataweave
%dw 2.0
import slice from dw::core::Arrays
output application/json
---
{
  firstThree: payload[0 to 2],
  nums: 1 to 5,
  mid: slice(payload, 1, 4)
}
```

`[0 to 2]` is inclusive. Out-of-range indexes are safer than Java (often empty, not an exception) — still do not assume that in every runtime; prefer `slice` / `take` / `drop` in production.

---

### Q63. How do you `zip` two arrays?

**Answer:** Pair headers with values (dynamic CSV / Excel columns):

```dataweave
%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  map { name: $[0], value: $[1] }
```

Length is the shorter array. Interview follow-up: building an object with `(pair[0]): pair[1]` (dynamic keys).

---

### Q64. How do you test types (`is`, `typeOf`)?

**Answer:** There is no Java `===`. Use `is` and `typeOf`:

```dataweave
payload is Object
payload.amount is Number
typeOf(payload)     // "Object" | "Array" | "String" | ...
```

`match { case x is Array -> ... }` is the same idea for trees (Q42, Q57).

---

### Q65. Which number helpers should you name?

**Answer:** `sum`, `avg`, `min`, `max`, `mod`, `abs`, `ceil`, `floor`, `round`, plus **money** via `as String {format: "0.00"} as Number`. Coerce ERP strings **before** arithmetic. `sum([])` is a common trap — skip empty or `default 0`. Do not use Java `BigDecimal` unless the interviewer asks; `fun money` is the DW answer.

---

### Q66. How do you handle timezones?

**Answer:** `DateTime` includes an offset; `LocalDateTime` / `Date` do not. Parse ISO-8601, then shift:

```dataweave
%dw 2.0
output application/json
var ts = payload.occurredAt as DateTime
---
{
  utc: ts >> "UTC",
  ist: ts >> "Asia/Kolkata",
  display: (ts >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"}
}
```

Store UTC in canonical APIs; convert only at the edge. Do not call `now()` inside a pricing module (inject `asOf`).

---

### Q67. What is in `dw::core::Dates` / `Periods`?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Dates
output application/json
---
{
  days: daysBetween(payload.start as Date, payload.end as Date),
  startOfDay: atBeginningOfDay(payload.occurredAt as DateTime),
  nextMonth: (payload.start as Date) + |P1M|
}
```

Period literals: `|P7D|`, `|PT2H|`. Interview: SLA clocks and invoice due dates, not “print today”.

---

### Q68. How do you `replace`, `find`, and split SKUs with Strings helpers?

**Answer:**

```dataweave
%dw 2.0
import * from dw::core::Strings
output application/json
---
{
  redacted: replace(payload.notes, /INV-\d+/, "REDACTED"),
  ids: payload.notes find /INV-\d+/,
  family: substringBefore(payload.sku, "-"),
  trimmed: trim(payload.name)
}
```

`matches` is a **full-string** regex (Q39). `find` / `scan` extract parts. `replace` can take a regex or a literal.

---

### Q69. How does Transform Message set payload **and** variables?

**Answer:** One Transform Message can have **multiple output targets**: Payload, Variable, Attributes (metadata). Each target is its own DataWeave script (own header). Typical pattern: payload = canonical JSON; variable `correlationId` = `attributes.headers['x-correlation-id'] default uuid()`; variable `recordCount` = `sizeOf(payload)`.

Do not cram side effects into `also` just to avoid a second target. Preview each target in Studio.

---

### Q70. When is `application/java` the payload type?

**Answer:** After Java/Salesforce/JMS connectors, payload is often `Map` / `List` (`application/java`), not a JSON string. DataWeave still selects `.field` the same way. Traps: Java `null` vs DW `null`, calendar types vs `DateTime`, and **don’t** `payload as String` then `read` unless you must. Output `application/java` only when the next processor needs a Java object (e.g. some connectors). Canonical APIs should still **write JSON**.

---

### Q71. What is `readUrl` vs `read`?

**Answer:** `read(binaryOrString, mime)` parses a value already in memory (Q19). `readUrl` loads from a URL or classpath:

```dataweave
readUrl("classpath://modules/iso-countries.json", "application/json")
```

Use for small lookup tables shipped in the app. Do not `readUrl` a huge file inside `map` (I/O per item). File connector + one Transform is cleaner for large blobs.

---

### Q72. How do you debug DataWeave (`log`, `application/dw`)?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  seen: log("DEBUG", payload.id),
  body: payload
}
```

`log` returns the value (so it can sit inline). `output application/dw` dumps the DW view of the data (Studio/debug). **Never** log raw payloads with PII (Lab 39). `log` is not a substitute for `try` or Mule On Error.

---

### Q73. DataWeave `try` vs Mule On Error?

**Answer:** `try` / `orElse` catch **expression** failures (bad `as Number`, divide by zero) and keep the script running. They do **not** catch HTTP 500 from a connector. Connector and flow failures use **On Error Continue / Propagate**, `error.errorType` (`HTTP:TIMEOUT`, `VALIDATION:INVALID_BOOLEAN`), `error.description`, `error.errorMessage.payload`. Interview: validation of dirty rows → `try` inside `map`; Salesforce timeout → On Error + retry.

---

### Q74. Which HTTP `attributes` should you memorize?

**Answer:**

| Field | Use |
| --- | --- |
| `attributes.method` | GET/POST routing in DW (rare; prefer Choice) |
| `attributes.uriParams.id` | `/orders/{id}` |
| `attributes.queryParams.page` | pagination (Lab 34) |
| `attributes.headers['x-correlation-id']` | tracing |
| `attributes.statusCode` | HTTP Request **response** attributes |

Listener vs Request: know which processor produced `attributes`. Query params are often **strings** — coerce `as Number`.

---

### Q75. Default XML namespaces, CDATA, mixed content?

**Answer:** Default `xmlns="http://acme.com/order"` still needs `ns ord http://acme.com/order` and `ord#PurchaseOrder` in DW — the prefix is yours, the URI must match. CDATA usually becomes element text. Mixed content (`<note>Pay <b>now</b></note>`) is messy; normalize with `trim` + `.*` children or refuse it in the contract. SOAP: always walk `Envelope/Body` (Lab 41).

---

### Q76. YAML, Excel, and flat file — does DataWeave do them?

**Answer:** DataWeave is MIME-driven. `application/yaml` is supported on current runtimes. Excel (`application/xlsx`) usually needs the **Excel module** / File connector, then DW on the sheet rows. EDI / fixed-width uses **flat file** schemas (`application/flatfile`), not ad-hoc `splitBy`. Playground may not offer every MIME — say that, then: set the reader MIME and map to canonical JSON. Do not parse XLSX by splitting strings.

---

### Q77. `dw::util::Values::mask` vs recursive mask?

**Answer:** `mask` / `update` with known **paths** is best when the schema is stable (`case .customer.ssn -> "****"`). Recursive `match` on types (Lab 39) is required when **key names** appear at unknown depth (`email`, `ssn`, `accessToken`). Interview both. Never log before masking.

---

### Q78. Boolean operators and precedence?

**Answer:** `and`, `or`, `not` — not Java `&&` / `||` / `!`. `not` binds tightest, then `and`, then `or`. Always parenthesize mixed conditions:

```dataweave
(lower(o.status) == "paid") and ((o.amount as Number) > 0)
```

`if` without `else` is illegal — every `if` is an expression (Q12).

---

### Q79. How do you sort by two fields (region, then amount desc)?

**Answer:** `orderBy` is one key. Descending numbers: `-o.amount`. Multi-field: a **composite key** (or sort by the less-significant key first, then the primary — only if the runtime’s `orderBy` is stable, which you should not bet on in interviews). Safer:

```dataweave
payload orderBy ((o) -> o.region ++ "|" ++ leftPad((100000000 - (o.amount as Number)) as String, 12, "0"))
```

Cleaner production: `orderBy ((o) -> o.region)` then group and sort each bucket. Name the trap: two sequential `orderBy` calls do **not** automatically mean SQL `ORDER BY a, b`.

---

### Q80. DataWeave vs For Each vs Batch Job vs Java?

**Answer:**

| Tool | Use |
| --- | --- |
| **DataWeave** | CPU-bound mapping, no I/O, streaming-friendly `map`/`filter` |
| **For Each** | Per-item **connector** calls (accept N+1 or collection-in) |
| **Batch Job** | Large files, aggregators, per-record retries, until-successful |
| **Java** | Libraries DW cannot express (special crypto, vendor SDK) |

Anti-pattern: `lookup` or HTTP inside `map` (Q40). Anti-pattern: Batch when a single Transform + streaming would do.

---
