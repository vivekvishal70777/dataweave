# LAB 56 — Shift DateTime to IST for display

| Field | Value |
| --- | --- |
| Level | industry |
| Student folder | `student/labs/04-industry/56-shift-datetime-to-ist-for-display/` |
| Solution | `instructor/solutions/04-industry/56-shift-datetime-to-ist-for-display/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-56-shift-datetime-to-ist-for-display.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 56. Shift DateTime to IST for display. Canonical APIs store UTC. Output `occurredAtIst` as `dd-MMM-yyyy HH:mm` in `Asia/Kolkata`. Do not use `now()`.

Shift UTC DateTime with >> Asia/Kolkata. Inject occurredAt. Do not call now.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "occurredAt": "2026-08-20T14:05:00Z" }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 56 — Shift DateTime to IST for display**
> Folder: `student/labs/04-industry/56-shift-datetime-to-ist-for-display/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-56-shift-datetime-to-ist-for-display-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
{
  occurredAtIst: ((payload.occurredAt as DateTime) >> "Asia/Kolkata")
    as String {format: "dd-MMM-yyyy HH:mm"}
}
```

**SAY:** That should match Expected:

IST is UTC+5:30 → `20-Aug-2026 19:35`

## Part 4 — Interview phrase and close

**SAY:**

Shift UTC DateTime with >> Asia/Kolkata. Inject occurredAt. Do not call now.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 57 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 56

Shift DateTime to IST for display

## Expected (note)

IST is UTC+5:30 → `20-Aug-2026 19:35`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
