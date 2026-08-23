# LAB 22 — Pivot array to object keyed by Id

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/22-pivot-array-to-object-keyed-by-id/` |
| Solution | `instructor/solutions/02-intermediate/22-pivot-array-to-object-keyed-by-id/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-22-pivot-array-to-object-keyed-by-id.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 22. Pivot array to object keyed by Id. `[{ "Id": "001xxA", "Name": "Acme" }]` → `{ "001xxA": "Acme" }` for O(1) lookup. Dynamic key

reduce into an object keyed by Salesforce Id. Parentheses around the key.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "Id": "001xxA", "Name": "Acme Corp" },
  { "Id": "001xxB", "Name": "Globex" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 22 — Pivot array to object keyed by Id**
> Folder: `student/labs/02-intermediate/22-pivot-array-to-object-keyed-by-id/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-22-pivot-array-to-object-keyed-by-id-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((item, acc = {}) -> acc ++ { (item.Id): item.Name })
```

**SAY:** That should match Expected:

```
{ "001xxA": "Acme Corp", "001xxB": "Globex" }
```

## Part 4 — Interview phrase and close

**SAY:**

reduce into an object keyed by Salesforce Id. Parentheses around the key.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 23 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 22

Pivot array to object keyed by Id

## Expected

```
{ "001xxA": "Acme Corp", "001xxB": "Globex" }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
