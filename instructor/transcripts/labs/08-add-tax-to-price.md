# LAB 08 — Add tax to price

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/08-add-tax-to-price/` |
| Solution | `instructor/solutions/01-fundamentals/08-add-tax-to-price/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-08-add-tax-to-price.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 08. Add tax to price. Add 18% tax. Return `{ price, tax, total }` with 2 decimal places as numbers.

Tax is price times rate. Coerce strings to Number before you multiply.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "price": 100 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 08 — Add tax to price**
> Folder: `student/labs/01-fundamentals/08-add-tax-to-price/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-08-add-tax-to-price-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var rate = 0.18
---
{
  price: payload.price,
  tax: payload.price * rate,
  total: payload.price * (1 + rate)
}
```

**SAY:** That should match Expected:

`{ "price": 100, "tax": 18, "total": 118 }`

## Part 4 — Interview phrase and close

**SAY:**

Tax is price times rate. Coerce strings to Number before you multiply.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 09 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 08

Add tax to price

## Expected (note)

`{ "price": 100, "tax": 18, "total": 118 }`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
