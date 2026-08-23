# LAB 76 — BOM explode one level to pick list

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/76-bom-explode-one-level-to-pick-list/` |
| Solution | `instructor/solutions/05-mapping/76-bom-explode-one-level-to-pick-list/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-76-bom-explode-one-level-to-pick-list.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 76. BOM explode one level to pick list. Each finished SKU has components. Explode order lines to component qty = parent qty * per. Skip unknown BOM.

BOM groupBy parent. flatMap order times per. Skip unknown parent.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "bom": [
    { "parent": "BIKE", "component": "FRAME", "per": 1 },
    { "parent": "BIKE", "component": "WHEEL", "per": 2 }
  ],
  "orders": [
    { "sku": "BIKE", "qty": 3 },
    { "sku": "UNK", "qty": 1 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 76 — BOM explode one level to pick list**
> Folder: `student/labs/05-mapping/76-bom-explode-one-level-to-pick-list/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-76-bom-explode-one-level-to-pick-list-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var byP = payload.bom groupBy $.parent
---
payload.orders
  flatMap ((o) ->
    (byP[o.sku] default []) map (b) -> {
      component: b.component,
      qty: (o.qty as Number) * (b.per as Number)
    }
  )
```

**SAY:** That should match Expected:

```
[
  { "component": "FRAME", "qty": 3 },
  { "component": "WHEEL", "qty": 6 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

BOM groupBy parent. flatMap order times per. Skip unknown parent.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 77 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 76

BOM explode one level to pick list

## Expected

```
[
  { "component": "FRAME", "qty": 3 },
  { "component": "WHEEL", "qty": 6 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
