# LAB 33 — Pattern match HTTP status class

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/33-pattern-match-http-status-class/` |
| Solution | `instructor/solutions/02-intermediate/33-pattern-match-http-status-class/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-33-pattern-match-http-status-class.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 33. Pattern match HTTP status class. Map `code`: 2xx → `ok`, 4xx → `client`, 5xx → `server`, else `other`. Prefer `match` over a pile of ifs in interviews.

match on HTTP ranges, not only string literals.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "code": 404 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 33 — Pattern match HTTP status class**
> Folder: `student/labs/02-intermediate/33-pattern-match-http-status-class/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-33-pattern-match-http-status-class-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.code match {
  case n if n >= 200 and n < 300 -> "ok"
  case n if n >= 400 and n < 500 -> "client"
  case n if n >= 500 and n < 600 -> "server"
  else -> "other"
}
```

**SAY:** That should match Expected:

`"client"`

## Part 4 — Interview phrase and close

**SAY:**

match on HTTP ranges, not only string literals.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 34 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 33

Pattern match HTTP status class

## Expected (note)

`"client"`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
