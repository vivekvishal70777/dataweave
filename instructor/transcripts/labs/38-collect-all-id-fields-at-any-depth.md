# LAB 38 — Collect all `id` fields at any depth

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/38-collect-all-id-fields-at-any-depth/` |
| Solution | `instructor/solutions/03-advanced/38-collect-all-id-fields-at-any-depth/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-38-collect-all-id-fields-at-any-depth.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 38. Collect all `id` fields at any depth. Return every `id` in a nested integration payload. Descendant `payload..id` is acceptable; be ready to recurse if the interviewer forbids `..`.

Descendant selector payload..id, or recurse if they forbid two dots.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "id": "root",
  "child": { "id": "c1", "items": [{ "id": "i1" }, { "sku": "x" }] }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 38 — Collect all `id` fields at any depth**
> Folder: `student/labs/03-advanced/38-collect-all-id-fields-at-any-depth/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-38-collect-all-id-fields-at-any-depth-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload..id
```

**SAY:** That should match Expected:

`["root", "c1", "i1"]` (walk order may vary)

## Part 4 — Interview phrase and close

**SAY:**

Descendant selector payload..id, or recurse if they forbid two dots.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 39 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 38

Collect all `id` fields at any depth

## Expected (note)

`["root", "c1", "i1"]` (walk order may vary)

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
