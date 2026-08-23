# LAB 25 — Merge config overlay (right wins)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/25-merge-config-overlay-right-wins/` |
| Solution | `instructor/solutions/02-intermediate/25-merge-config-overlay-right-wins/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-25-merge-config-overlay-right-wins.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 25. Merge config overlay (right wins). Shallow-merge `base` with `overlay`. Right-hand keys win. Both objects live on

plus-plus shallow merge. Overlay lives on payload so Playground works.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "base": { "timeout": 30, "retries": 2, "region": "us-east-1" },
  "overlay": { "retries": 5, "region": "ap-south-1" }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 25 — Merge config overlay (right wins)**
> Folder: `student/labs/02-intermediate/25-merge-config-overlay-right-wins/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-25-merge-config-overlay-right-wins-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.base ++ payload.overlay
```

**SAY:** That should match Expected:

```
{ "timeout": 30, "retries": 5, "region": "ap-south-1" }
```

## Part 4 — Interview phrase and close

**SAY:**

plus-plus shallow merge. Overlay lives on payload so Playground works.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 26 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 25

Merge config overlay (right wins)

## Expected

```
{ "timeout": 30, "retries": 5, "region": "ap-south-1" }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
