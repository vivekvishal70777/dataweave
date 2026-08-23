# LAB 54 — Production invoice: discounts, tax, skip zero qty

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/54-production-invoice-discounts-tax-skip-zero-qty/` |
| Solution | `instructor/solutions/03-advanced/54-production-invoice-discounts-tax-skip-zero-qty/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-54-production-invoice-discounts-tax-skip-zero-qty.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 54. Production invoice: discounts, tax, skip zero qty. Drop lines with `qty` ≤ 0. `lineTotal = qty * price * (1 - discountPct)` rounded to 2 decimals. `subtotal` = sum of line totals. `tax` = subtotal × `taxRate`. `grandTotal` = subtotal + tax. Header `var` / `fun money`.

Filter qty greater than zero. Discount then tax. fun money on every currency field.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "taxRate": 0.18,
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "price": 50, "discountPct": 0.10 },
    { "sku": "SKU-B", "qty": 1, "price": 100, "discountPct": 0 },
    { "sku": "SKU-Z", "qty": 0, "price": 999, "discountPct": 0 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 54 — Production invoice: discounts, tax, skip zero qty**
> Folder: `student/labs/03-advanced/54-production-invoice-discounts-tax-skip-zero-qty/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-54-production-invoice-discounts-tax-skip-zero-qty-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var lines = payload.lines
  filter ((l) -> (l.qty as Number) > 0)
  map (l) -> do {
    var qty = l.qty as Number
    var price = l.price as Number
    var disc = (l.discountPct default 0) as Number
    ---
    l ++ { lineTotal: money(qty * price * (1 - disc)) }
  }
var subtotal = money(sum(lines.lineTotal))
var tax = money(subtotal * payload.taxRate)
---
{
  currency: payload.currency,
  lines: lines,
  subtotal: subtotal,
  tax: tax,
  grandTotal: money(subtotal + tax)
}
```

**SAY:** That should match Expected:

SKU-Z omitted; SKU-A `lineTotal` 90.00; SKU-B 100.00; `subtotal` 190.00; `tax` 34.20; `grandTotal` 224.20.

## Part 4 — Interview phrase and close

**SAY:**

Filter qty greater than zero. Discount then tax. fun money on every currency field.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 55 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 54

Production invoice: discounts, tax, skip zero qty

## Expected (note)

SKU-Z omitted; SKU-A `lineTotal` 90.00; SKU-B 100.00; `subtotal` 190.00; `tax` 34.20; `grandTotal` 224.20.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
