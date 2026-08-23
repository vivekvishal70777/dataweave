# LAB 66 — Product variants color times size SKUs

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/66-product-variants-color-times-size-skus/` |
| Solution | `instructor/solutions/05-mapping/66-product-variants-color-times-size-skus/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-66-product-variants-color-times-size-skus.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 66. Product variants color times size SKUs. Cartesian colors x sizes. Skip discontinued colors. SKU base-color-size.

flatMap colors times sizes. Skip discontinued. SKU base-color-size.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "base": "TEE",
  "colors": [
    { "code": "BLK", "discontinued": false },
    { "code": "RED", "discontinued": true },
    { "code": "WHT", "discontinued": false }
  ],
  "sizes": ["S", "M"]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 66 — Product variants color times size SKUs**
> Folder: `student/labs/05-mapping/66-product-variants-color-times-size-skus/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-66-product-variants-color-times-size-skus-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.colors
  filter ((c) -> c.discontinued == false)
  flatMap ((c) ->
    payload.sizes map (sz) -> {
      sku: payload.base ++ "-" ++ c.code ++ "-" ++ sz
    }
  )
```

**SAY:** That should match Expected:

```
[
  { "sku": "TEE-BLK-S" },
  { "sku": "TEE-BLK-M" },
  { "sku": "TEE-WHT-S" },
  { "sku": "TEE-WHT-M" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

flatMap colors times sizes. Skip discontinued. SKU base-color-size.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 67 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 66

Product variants color times size SKUs

## Expected

```
[
  { "sku": "TEE-BLK-S" },
  { "sku": "TEE-BLK-M" },
  { "sku": "TEE-WHT-S" },
  { "sku": "TEE-WHT-M" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
