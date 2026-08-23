# LAB 17 — Boolean flag from dirty string

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/17-boolean-flag-from-dirty-string/` |
| Solution | `instructor/solutions/01-fundamentals/17-boolean-flag-from-dirty-string/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-17-boolean-flag-from-dirty-string.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 17. Boolean flag from dirty string. `"Y"` / `"yes"` / `"true"` / `"1"` (any case) → `true`, else `false`. Common in SAP/legacy flags.

Legacy flags: y yes true 1. Do not rely on Java parseBoolean alone.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "active": "Yes" }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 17 — Boolean flag from dirty string**
> Folder: `student/labs/01-fundamentals/17-boolean-flag-from-dirty-string/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-17-boolean-flag-from-dirty-string-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
{
  active: ["y", "yes", "true", "1"] contains lower(payload.active as String)
}
```

**SAY:** That should match Expected:

```
{ "active": true }
```

## Part 4 — Interview phrase and close

**SAY:**

Legacy flags: y yes true 1. Do not rely on Java parseBoolean alone.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 18 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 17

Boolean flag from dirty string

## Expected

```
{ "active": true }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
