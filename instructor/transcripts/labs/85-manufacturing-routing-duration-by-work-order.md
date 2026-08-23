# LAB 85 — Manufacturing routing duration by work order

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/85-manufacturing-routing-duration-by-work-order/` |
| Solution | `instructor/solutions/05-mapping/85-manufacturing-routing-duration-by-work-order/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-85-manufacturing-routing-duration-by-work-order.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 85. Manufacturing routing duration by work order. Sum step minutes per wo, order steps by seq. Output wo, steps[], totalMinutes.

groupBy work order. orderBy seq. Sum minutes.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "wo": "WO1", "seq": 20, "step": "PAINT", "min": "15" },
  { "wo": "WO1", "seq": 10, "step": "CUT", "min": 30 },
  { "wo": "WO2", "seq": 10, "step": "PACK", "min": 5 }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 85 — Manufacturing routing duration by work order**
> Folder: `student/labs/05-mapping/85-manufacturing-routing-duration-by-work-order/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-85-manufacturing-routing-duration-by-work-order-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload groupBy $.wo
  pluck ((rows, wo) -> do {
    var ordered = rows orderBy $.seq map { seq: $.seq as Number, step: $.step, min: $.min as Number }
    ---
    { wo: wo, steps: ordered, totalMinutes: sum(ordered.min) }
  })
```

**SAY:** That should match Expected:

```
[
  {
    "wo": "WO1",
    "steps": [
      { "seq": 10, "step": "CUT", "min": 30 },
      { "seq": 20, "step": "PAINT", "min": 15 }
    ],
    "totalMinutes": 45
  },
  {
    "wo": "WO2",
    "steps": [
      { "seq": 10, "step": "PACK", "min": 5 }
    ],
    "totalMinutes": 5
  }
]
```

## Part 4 — Interview phrase and close

**SAY:**

groupBy work order. orderBy seq. Sum minutes.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 86 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 85

Manufacturing routing duration by work order

## Expected

```
[
  {
    "wo": "WO1",
    "steps": [
      { "seq": 10, "step": "CUT", "min": 30 },
      { "seq": 20, "step": "PAINT", "min": 15 }
    ],
    "totalMinutes": 45
  },
  {
    "wo": "WO2",
    "steps": [
      { "seq": 10, "step": "PACK", "min": 5 }
    ],
    "totalMinutes": 5
  }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
