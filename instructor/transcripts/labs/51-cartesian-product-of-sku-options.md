# LAB 51 — Cartesian product of SKU options

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/51-cartesian-product-of-sku-options/` |
| Solution | `instructor/solutions/03-advanced/51-cartesian-product-of-sku-options/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-51-cartesian-product-of-sku-options.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 51. Cartesian product of SKU options. Product configurator: every color × every size.

Cartesian SKU options: colors flatMap sizes.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "colors": ["R", "G"], "sizes": ["S", "M"] }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 51 — Cartesian product of SKU options**
> Folder: `student/labs/03-advanced/51-cartesian-product-of-sku-options/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-51-cartesian-product-of-sku-options-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.colors flatMap ((c) ->
  payload.sizes map (s) -> { color: c, size: s }
)
```

**SAY:** That should match Expected:

four objects `{ color, size }`.

## Part 4 — Interview phrase and close

**SAY:**

Cartesian SKU options: colors flatMap sizes.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 52 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 51

Cartesian product of SKU options

## Expected (note)

four objects `{ color, size }`.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
