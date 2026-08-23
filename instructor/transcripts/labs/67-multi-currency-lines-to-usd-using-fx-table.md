# LAB 67 — Multi-currency lines to USD using FX table

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/67-multi-currency-lines-to-usd-using-fx-table/` |
| Solution | `instructor/solutions/05-mapping/67-multi-currency-lines-to-usd-using-fx-table/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-67-multi-currency-lines-to-usd-using-fx-table.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 67. Multi-currency lines to USD using FX table. usd = amount / perUsd. Skip unknown currency. fun money.

FX: amount divided by perUsd. Skip unknown currency. Sum USD.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "fx": [
    { "ccy": "USD", "perUsd": 1 },
    { "ccy": "INR", "perUsd": 83 },
    { "ccy": "EUR", "perUsd": 0.92 }
  ],
  "lines": [
    { "id": "L1", "amount": "8300", "currency": "INR" },
    { "id": "L2", "amount": "10", "currency": "USD" },
    { "id": "L3", "amount": "9.2", "currency": "EUR" },
    { "id": "L4", "amount": "1", "currency": "JPY" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 67 — Multi-currency lines to USD using FX table**
> Folder: `student/labs/05-mapping/67-multi-currency-lines-to-usd-using-fx-table/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-67-multi-currency-lines-to-usd-using-fx-table-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var rates = payload.fx groupBy $.ccy
var converted = payload.lines
  filter ((l) -> rates[l.currency] != null)
  map (l) -> {
    id: l.id,
    usd: money((l.amount as Number) / (rates[l.currency][0].perUsd as Number))
  }
---
{
  lines: converted,
  totalUsd: money(sum(converted.usd))
}
```

**SAY:** That should match Expected:

```
{
  "lines": [
    { "id": "L1", "usd": 100.00 },
    { "id": "L2", "usd": 10.00 },
    { "id": "L3", "usd": 10.00 }
  ],
  "totalUsd": 120.00
}
```

## Part 4 — Interview phrase and close

**SAY:**

FX: amount divided by perUsd. Skip unknown currency. Sum USD.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 68 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 67

Multi-currency lines to USD using FX table

## Expected

```
{
  "lines": [
    { "id": "L1", "usd": 100.00 },
    { "id": "L2", "usd": 10.00 },
    { "id": "L3", "usd": 10.00 }
  ],
  "totalUsd": 120.00
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
