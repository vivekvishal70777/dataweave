# DataWeave 2.0 cheat sheet

Keep this open during labs. Full explanations live in `sections/*/LECTURE.md`.

## Script skeleton

```dataweave
%dw 2.0
output application/json
var taxRate = 0.18
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{ total: payload.amount * (1 + taxRate) }
```

## Arrays

| Need | Function |
| --- | --- |
| Transform each item | `map` |
| Keep some items | `filter` |
| 1-to-many rows | `flatMap` |
| Fold to one value | `reduce` |
| Unique / sort / group | `distinctBy` / `orderBy` / `groupBy` |
| One-level flatten | `flatten` |
| Length / empty | `sizeOf` / `isEmpty` |
| Page | `drop` / `take` (import Arrays) |
| Chunk | `divideBy` |

`$` = item, `$$` = index. Prefer `(item, index) ->`.

## Objects

| Need | Function |
| --- | --- |
| Transform keys/values | `mapObject` |
| Object → array | `pluck` |
| Keep keys | `filterObject` |
| Merge (right wins) | `++` |
| Nested field | `update { case .a.b -> ... }` (Mule 4.3+) |
| Dynamic key | `{ (expr): value }` |
| Names / values | `namesOf` / `valuesOf` / `entriesOf` |

## Nulls and errors

- Missing/null value: `payload.email default "n/a"`
- Null-safe path: `payload.address.?city`
- Coercion/runtime inside script: `try(() -> x as Number) orElse 0`
- Drop nulls on write: `output application/json skipNullOn="everywhere"`

`default` does **not** catch errors.

## Selectors

- `payload.customer.name` — field
- `payload[0]` — index
- `payload["first-name"]` — odd key
- `payload.*item` — repeating children (XML)
- `payload..id` — descendants
- `payload.order.@id` — XML attribute

## Strings and concat

- Concat string/array/object: `++` (object: right key wins)
- Add numbers: `+`
- `splitBy` / `joinBy` / `upper` / `lower` / `capitalize`
- `startsWith` / `contains` / `matches` (full regex)

## Conditionals

```dataweave
if (score >= 90) "A"
else if (score >= 75) "B"
else "F"

status match {
  case "PAID" -> "ok"
  case n if n >= 400 -> "client"
  else -> "other"
}
```

No Java `? :` ternary.

## Formats

- JSON → XML: `output application/xml` and **one root**.
- XML attr write: `order @(id: payload.id): { ... }`
- Namespace: `ns ns0 http://acme.com/order` then `ns0#order`
- CSV in: array of objects from header row; coerce `as Number`.
- CSV out: `output application/csv header=true`

## Dates

```dataweave
now() as String {format: "dd-MMM-yyyy"}
"2026-08-20" as Date {format: "yyyy-MM-dd"}
(now() as Date) + |P7D|
```

## Joins and Mule

```dataweave
vars.customerId
attributes.queryParams.page
p("http.host")
import leftJoin from dw::core::Arrays
```

Interview default: index once with `groupBy`, then `map`. Avoid `lookup` inside `map`.

## Streaming breaks when you…

`sizeOf(payload)`, `orderBy`, `groupBy`, `distinctBy`, full `reduce`, touching payload twice, `payload as String`.
