# LAB 47 — Error-code frequency from log lines

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/47-error-code-frequency-from-log-lines/` |
| Solution | `instructor/solutions/03-advanced/47-error-code-frequency-from-log-lines/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-47-error-code-frequency-from-log-lines.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 47. Error-code frequency from log lines. Count case-insensitive tokens in an ops log string (same skill as word frequency). Ignore empty pieces.

Ops log histogram. lower, split, groupBy, sizeOf.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```text
TIMEOUT timeout 429 TIMEOUT mule
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 47 — Error-code frequency from log lines**
> Folder: `student/labs/03-advanced/47-error-code-frequency-from-log-lines/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-47-error-code-frequency-from-log-lines-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var words = lower(payload) splitBy /[^a-z0-9]+/
---
(words filter !isEmpty($))
  groupBy $
  mapObject ((v, k) -> { (k): sizeOf(v) })
```

**SAY:** That should match Expected:

`{ "timeout": 3, "429": 1, "mule": 1 }` (key order may vary)

## Part 4 — Interview phrase and close

**SAY:**

Ops log histogram. lower, split, groupBy, sizeOf.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 48 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 47

Error-code frequency from log lines

## Expected (note)

`{ "timeout": 3, "429": 1, "mule": 1 }` (key order may vary)

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
