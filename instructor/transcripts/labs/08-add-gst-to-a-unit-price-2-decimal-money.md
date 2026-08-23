# LAB 08 — Add GST to a unit price (2 decimal money)

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/08-add-gst-to-a-unit-price-2-decimal-money/` |
| Solution | `instructor/solutions/01-fundamentals/08-add-gst-to-a-unit-price-2-decimal-money/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-08-add-gst-to-a-unit-price-2-decimal-money.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 08. Add GST to a unit price (2 decimal money). GST 18%. Return `{ price, tax, total }` as numbers with

Round tax with fun money: format 0.00 then as Number.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "price": 99.99 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 08 — Add GST to a unit price (2 decimal money)**
> Folder: `student/labs/01-fundamentals/08-add-gst-to-a-unit-price-2-decimal-money/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-08-add-gst-to-a-unit-price-2-decimal-money-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var rate = 0.18
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  price: money(payload.price),
  tax: money(payload.price * rate),
  total: money(payload.price * (1 + rate))
}
```

**SAY:** That should match Expected:

```
{ "price": 99.99, "tax": 18.00, "total": 117.99 }
```

## Part 4 — Interview phrase and close

**SAY:**

Round tax with fun money: format 0.00 then as Number.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 09 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 08

Add GST to a unit price (2 decimal money)

## Expected

```
{ "price": 99.99, "tax": 18.00, "total": 117.99 }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
