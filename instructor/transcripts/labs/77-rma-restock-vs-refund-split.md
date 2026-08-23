# LAB 77 — RMA restock vs refund split

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/77-rma-restock-vs-refund-split/` |
| Solution | `instructor/solutions/05-mapping/77-rma-restock-vs-refund-split/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-77-rma-restock-vs-refund-split.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 77. RMA restock vs refund split. reason DAMAGED → refund only (restock false). Else restock true. Amount = qty * unit. fun money.

DAMAGED means restock false. Refund qty times unit.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "rma": "R1", "reason": "DAMAGED", "qty": "2", "unit": "10.00" },
  { "rma": "R2", "reason": "SIZE", "qty": 1, "unit": "15.5" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 77 — RMA restock vs refund split**
> Folder: `student/labs/05-mapping/77-rma-restock-vs-refund-split/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-77-rma-restock-vs-refund-split-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload map {
  rma: $.rma,
  restock: upper($.reason) != "DAMAGED",
  refund: money(($.qty as Number) * ($.unit as Number))
}
```

**SAY:** That should match Expected:

```
[
  { "rma": "R1", "restock": false, "refund": 20.00 },
  { "rma": "R2", "restock": true, "refund": 15.50 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

DAMAGED means restock false. Refund qty times unit.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 78 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 77

RMA restock vs refund split

## Expected

```
[
  { "rma": "R1", "restock": false, "refund": 20.00 },
  { "rma": "R2", "restock": true, "refund": 15.50 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
