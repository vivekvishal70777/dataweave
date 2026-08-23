# LAB 18 — SKU prefix before hyphen

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/18-sku-prefix-before-hyphen/` |
| Solution | `instructor/solutions/01-fundamentals/18-sku-prefix-before-hyphen/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-18-sku-prefix-before-hyphen.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 18. SKU prefix before hyphen. From `"MULE-12345"` take the product family `"MULE"` (split on `-`, first segment).

Split SKU on hyphen and take the family prefix.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```text
MULE-12345
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 18 — SKU prefix before hyphen**
> Folder: `student/labs/01-fundamentals/18-sku-prefix-before-hyphen/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-18-sku-prefix-before-hyphen-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
(payload splitBy "-")[0]
```

**SAY:** That should match Expected:

`"MULE"`

## Part 4 — Interview phrase and close

**SAY:**

Split SKU on hyphen and take the family prefix.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 19 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 18

SKU prefix before hyphen

## Expected (note)

`"MULE"`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
