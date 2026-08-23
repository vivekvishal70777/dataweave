# LAB 75 — Appointment slots to IST display with duration

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/75-appointment-slots-to-ist-display-with-duration/` |
| Solution | `instructor/solutions/05-mapping/75-appointment-slots-to-ist-display-with-duration/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-75-appointment-slots-to-ist-display-with-duration.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 75. Appointment slots to IST display with duration. Parse start/end ISO. Shift both to Asia/Kolkata. durationMinutes from period. Inject times — no now().

Shift both instants to IST. Duration is epoch millis difference over 60000.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "id": "APT-1",
  "start": "2026-08-20T03:30:00Z",
  "end": "2026-08-20T04:00:00Z"
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 75 — Appointment slots to IST display with duration**
> Folder: `student/labs/05-mapping/75-appointment-slots-to-ist-display-with-duration/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-75-appointment-slots-to-ist-display-with-duration-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var s = payload.start as DateTime
var e = payload.end as DateTime
---
{
  id: payload.id,
  startIst: (s >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  endIst: (e >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  durationMinutes: ((e as Number) - (s as Number)) / 60000
}
```

**SAY:** That should match Expected:

```
{
  "id": "APT-1",
  "startIst": "20-Aug-2026 09:00",
  "endIst": "20-Aug-2026 09:30",
  "durationMinutes": 30
}
```

## Part 4 — Interview phrase and close

**SAY:**

Shift both instants to IST. Duration is epoch millis difference over 60000.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 76 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 75

Appointment slots to IST display with duration

## Expected

```
{
  "id": "APT-1",
  "startIst": "20-Aug-2026 09:00",
  "endIst": "20-Aug-2026 09:30",
  "durationMinutes": 30
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
