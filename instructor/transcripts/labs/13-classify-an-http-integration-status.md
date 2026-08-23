# LAB 13 — Classify an HTTP/integration status

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/13-classify-an-http-integration-status/` |
| Solution | `instructor/solutions/01-fundamentals/13-classify-an-http-integration-status/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-13-classify-an-http-integration-status.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 13. Classify an HTTP/integration status. From `{ "httpStatus": 503 }`, return `"retry"` for 408/429/5xx, `"client"` for 4xx, `"ok"` for 2xx, else `"other"`. No Java ternary.

Retry on 408, 429, and 5xx. if/else is an expression, not a school grade.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "httpStatus": 503 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 13 — Classify an HTTP/integration status**
> Folder: `student/labs/01-fundamentals/13-classify-an-http-integration-status/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-13-classify-an-http-integration-status-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var s = payload.httpStatus as Number
---
if ([408, 429] contains s) "retry"
else if (s >= 500 and s < 600) "retry"
else if (s >= 200 and s < 300) "ok"
else if (s >= 400 and s < 500) "client"
else "other"
```

**SAY:** That should match Expected:

`"retry"`

## Part 4 — Interview phrase and close

**SAY:**

Retry on 408, 429, and 5xx. if/else is an expression, not a school grade.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 14 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 13

Classify an HTTP/integration status

## Expected (note)

`"retry"`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
