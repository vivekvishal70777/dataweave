# DataWeave production interview questions and answers

**20 hard questions (61–80)** for Mule 4 / DataWeave 2.x **production** interviews: partial success, golden records, CDC, money, overlays, and operational envelopes.

Hands-on scripts: [DataWeave-Production-Transformations.md](DataWeave-Production-Transformations.md) (Labs 55–82).

---

## Production (Questions 61–80)

### 61. How do you design a transform that must not fail the whole batch when one row is bad?

**Answer:** Split **valid vs invalid** inside the script (`filter` + `try`), put good rows in the canonical shape, and collect `{ id, reason }` in `errors[]`. The Mule flow then Choice-routes: empty `errors` → happy path; mixed → 207-style downstream or a second publisher for the DLQ. Do **not** swallow errors with `default 0` unless the business explicitly wants silent zeros.

See Lab 55.

### 62. Why is `++` the wrong default for a customer-360 / MDM merge?

**Answer:** `++` is a **shallow** overwrite: a `null` from the “winning” system wipes a good value from ERP. Production merges use **per-field coalesce** (`mdm default (crm default erp)`), a documented precedence list, and **collection keys** (email union, address by `type`). Tag each source before `groupBy` so missing sources do not shift array indexes.

See Lab 56.

### 63. What is an idempotency key and what must never go in it?

**Answer:** A stable string the provider uses to recognize **retries of the same business document** (`customerId|externalOrderId|sorted skus`). Never include `now()`, random UUIDs, or unsorted arrays. Store it on the outbound HTTP header or in an object store keyed for upserts.

See Lab 62.

### 64. How do you map CDC (`c`/`u`/`d`) without dropping deletes?

**Answer:** `match` on `op`. Creates/updates take `after`; deletes (**tombstones**) take `before` and still emit a stable `id`. Unknown ops are skipped (`null` + `filter`), not thrown, so a poison `op` does not halt the batch. Downstream consumers must be idempotent.

See Lab 57.

### 65. Where should FX rates and other lookup tables live?

**Answer:** As an **object/table already in the payload or `vars`**, indexed once. `payload.rates[currency]` inside `map` is O(1). `lookup("get-rate-flow", …)` inside `map` is N+1 HTTP. Pin the rate timestamp in production; missing rate → `errors[]`, not a guessed `1.0`.

See Lab 58.

### 66. What is a trailer / control-total check?

**Answer:** File-based payments and EDI include a last record whose `total` must equal `sum(lines)`. Emit `{ balanced: true/false }`. If false, **do not post the ledger** — route to ops. Same idea as Lab 71 batch checksums.

See Lab 60.

### 67. When is pagination in DataWeave the wrong tool?

**Answer:** `drop` / `take` / `sizeOf(payload)` **materialize** the collection and break streaming. Page at the **connector** (DB `LIMIT/OFFSET`, Salesforce query locator, S3 list). Use Lab 61 only for small in-memory lists or for shaping an envelope the API already paginated.

### 68. How do you keep CloudEvents / audit timestamps testable?

**Answer:** Inject `payload.now` and `eventId` (or `vars`). Do not call `now()` or `UUID::randomUUID()` inside a reusable module if you need MUnit determinism. Duplicate `id`/`type` on the MQ/Kafka headers if the bus requires them.

See Lab 65.

### 69. What merge algebra should you quote for tenant config overlays?

**Answer:** Precedence **request > tenant > defaults**. Nested objects merge recursively; **feature-flag arrays replace** (do not concatenate). Document it; a blind `++` is shallow and `flatten` of flags duplicates entries.

See Lab 66.

### 70. How does JSON Merge Patch (RFC 7396) differ from PUT?

**Answer:** PUT replaces the resource. Merge Patch: `null` **deletes** a key; nested objects merge; non-objects replace. Pair the result with a **changelog** of paths (`from`/`to`) for audit. Do not `skipNullOn` the changelog or deletions vanish.

See Lab 70.

### 71. What is a “business date” vs `createdAt` UTC?

**Answer:** Business date is a **policy** (store timezone, cut-off hour), not the raw ISO timestamp. Convert with an explicit offset or IANA zone, inject the clock in tests. Mixing UTC `createdAt` with IST “booking date” without a written rule causes settlement bugs.

See Labs 67 and 72.

### 72. How do you aggregate Scatter-Gather (or parallel HTTP) results?

**Answer:** Map **each leg**: 2xx → `ok[name] = body`; else `errors[]`. Partial success is allowed unless the product requires all-or-nothing (then fail the flow in Choice, not by throwing inside DW). Same pattern as Salesforce `allOrNone: false`.

See Labs 75 and 76.

### 73. How do you explode a bill of materials without infinite recursion?

**Answer:** One-level explode is `groupBy` sku + `map` components (Lab 59). Multi-level explode passes a **visited path**; if `sku` is already on the path, emit `cycle: true` and stop. Production item graphs have cycles.

See Lab 73.

### 74. When do you flatten JSON to dotted keys?

**Answer:** Analytics, CSV, and some search indexes want **one object, dotted paths** (`lines.0.sku`). Walk with `match` on Object/Array. This materializes the tree — not for multi-GB payloads.

See Lab 74.

### 75. How do you redact logs without breaking tracing?

**Answer:** `mapObject` on headers: `authorization`, `cookie`, `x-api-key` → `"****"`; **keep** `x-correlation-id`. Apply Lab 39-style recursion to bodies. Logging raw inbound HTTP is a production incident.

See Lab 79.

### 76. How do you project “latest version wins” from an event list?

**Answer:** `reduce` into an object keyed by `id`; replace when `version >= current`. `distinctBy` keeps the **first**, which is wrong for event logs. Tie-break with array order (`>=`).

See Lab 77.

### 77. How do you map SOAP Fault vs Body?

**Answer:** If `Envelope.Body.Fault` is present, return `{ ok: false, code, message }` and stop. Else unwrap the Body. Do this **before** the happy-path canonical map; in Mule a tiny DW + Choice is clearer than one 200-line script.

See Lab 68.

### 78. FIFO allocation / warehouse draw — what does DataWeave own?

**Answer:** A **plan**: `reduce` a running remainder over warehouses sorted by priority. Inventory locks and writes stay in the backend. Shortfall is an explicit field, not a thrown error, unless the SLA says hard-fail.

See Lab 63.

### 79. Heterogeneous webhooks (`card` vs `upi` vs `wallet`) — which operator?

**Answer:** `match` on `method`/`type` with an `else` that maps to `other` (or `errors[]`). Nested `if` without `else` drops unknown PSPs silently or crashes the batch.

See Lab 82.

### 80. Talk through an end-to-end production order mapper (design, not trivia).

**Answer:** A strong answer covers:

1. **In:** JSON/XML/EDI → normalize types with `try`; bad lines → `errors[]` (Lab 55).  
2. **Money:** one `fun money` (2 dp); tax on successful subtotal only.  
3. **Join:** customer from `vars` or a table already fetched — never `lookup` per line.  
4. **FX:** table in payload (Lab 58).  
5. **Idempotency key** from natural keys (Lab 62).  
6. **Out:** canonical JSON `skipNullOn` only on the API body, not on the error array.  
7. **Ops:** correlation id; on connector failure wrap DLQ (Lab 81).  
8. **Scale:** one-pass `map`; index catalogs with `groupBy`; do not `orderBy` the whole file unless required.

Sketch (happy path + errors): Lab 55. Envelope: Lab 65. Replay: Lab 81.

---

## Quick production checklist

- Partial success: `errors[]`, do not `default 0` away money  
- Precedence + nulls, not raw `++`  
- Index once (`groupBy`); no N+1 `lookup`  
- Inject `now` / ids for tests  
- Cycle guards on recursive graphs  
- Redact headers before log  
- Control totals / checksums before posting  
- `match` + `else` on union types  

---

*Pair with Labs 55–82. Mule 4.3+ for `update`, `divideBy`, `drop` / `take`.*
