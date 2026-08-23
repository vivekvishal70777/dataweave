# LAB 52 — Safe divide with `try`

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/52-safe-divide-with-try/` |
| Solution | `instructor/solutions/03-advanced/52-safe-divide-with-try/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-52-safe-divide-with-try.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 52. Safe divide with `try`. `amount / qty`; if `qty` is 0 or not numeric, return `null`.

try divide, orElse null or zero. Contrast with default which only helps null.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "id": 1, "amount": 10, "qty": 2 }, { "id": 2, "amount": 10, "qty": 0 }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 52 — Safe divide with `try`**
> Folder: `student/labs/03-advanced/52-safe-divide-with-try/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-52-safe-divide-with-try-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import try, orElse from dw::Runtime
output application/json
---
payload map {
  id: $.id,
  unit: try(() -> ($.amount as Number) / ($.qty as Number)) orElse null
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

try divide, orElse null or zero. Contrast with default which only helps null.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 53 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 52

Safe divide with `try`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
