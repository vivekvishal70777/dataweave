# LAB 54 — Invoice: compute line totals, tax, and grand total

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/54-invoice-compute-line-totals-tax-and-grand-total/` |
| Solution | `instructor/solutions/03-advanced/54-invoice-compute-line-totals-tax-and-grand-total/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-54-invoice-compute-line-totals-tax-and-grand-total.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 54. Invoice: compute line totals, tax, and grand total. Invoice: compute line totals, tax, and grand total

var lines with lineTotal, subtotal, tax, grandTotal. Header vars keep the body clean.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "taxRate": 0.18,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50 },
    { "sku": "B", "qty": 1, "price": 100 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 54 — Invoice: compute line totals, tax, and grand total**
> Folder: `student/labs/03-advanced/54-invoice-compute-line-totals-tax-and-grand-total/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-54-invoice-compute-line-totals-tax-and-grand-total-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var lines = payload.lines map (l) -> l ++ { lineTotal: l.qty * l.price }
var subtotal = sum(lines.lineTotal)
var tax = subtotal * payload.taxRate
---
{
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: subtotal + tax
}
```

**SAY:** That should match Expected:

each line has `lineTotal`; document has `subtotal` `200`, `tax` `36`, `grandTotal` `236`.

## Part 4 — Interview phrase and close

**SAY:**

var lines with lineTotal, subtotal, tax, grandTotal. Header vars keep the body clean.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 55 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 54

Invoice: compute line totals, tax, and grand total

## Expected (note)

each line has `lineTotal`; document has `subtotal` `200`, `tax` `36`, `grandTotal` `236`.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
