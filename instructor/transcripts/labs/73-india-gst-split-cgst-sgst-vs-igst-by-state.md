# LAB 73 — India GST split CGST SGST vs IGST by state

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/73-india-gst-split-cgst-sgst-vs-igst-by-state/` |
| Solution | `instructor/solutions/05-mapping/73-india-gst-split-cgst-sgst-vs-igst-by-state/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-73-india-gst-split-cgst-sgst-vs-igst-by-state.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 73. India GST split CGST SGST vs IGST by state. Same state: half of 18% each CGST and SGST. Different: full IGST 18%. fun money on taxable amount.

Same state: CGST and SGST 9 each. Else IGST 18. fun money.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "fromState": "KA",
  "toState": "MH",
  "taxable": "1000.00"
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 73 — India GST split CGST SGST vs IGST by state**
> Folder: `student/labs/05-mapping/73-india-gst-split-cgst-sgst-vs-igst-by-state/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-73-india-gst-split-cgst-sgst-vs-igst-by-state-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var t = payload.taxable as Number
var intra = payload.fromState == payload.toState
---
{
  taxable: money(t),
  cgst: if (intra) money(t * 0.09) else 0.00,
  sgst: if (intra) money(t * 0.09) else 0.00,
  igst: if (intra) 0.00 else money(t * 0.18)
}
```

**SAY:** That should match Expected:

```
{
  "taxable": 1000.00,
  "cgst": 0.00,
  "sgst": 0.00,
  "igst": 180.00
}
```

## Part 4 — Interview phrase and close

**SAY:**

Same state: CGST and SGST 9 each. Else IGST 18. fun money.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 74 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 73

India GST split CGST SGST vs IGST by state

## Expected

```
{
  "taxable": 1000.00,
  "cgst": 0.00,
  "sgst": 0.00,
  "igst": 180.00
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
