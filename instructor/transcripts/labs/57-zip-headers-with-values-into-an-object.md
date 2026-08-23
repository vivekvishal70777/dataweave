# LAB 57 — Zip headers with values into an object

| Field | Value |
| --- | --- |
| Level | industry |
| Student folder | `student/labs/04-industry/57-zip-headers-with-values-into-an-object/` |
| Solution | `instructor/solutions/04-industry/57-zip-headers-with-values-into-an-object/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-57-zip-headers-with-values-into-an-object.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 57. Zip headers with values into an object. Dynamic columns: `headers` + `values` (same length). Build `{ Name: "Asha", Amount: "10.5" }` using `zip` and dynamic keys.

zip headers with values. Reduce into an object. Parentheses around the key.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "headers": ["Name", "Amount", "City"],
  "values": ["Asha", "10.5", "Pune"]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 57 — Zip headers with values into an object**
> Folder: `student/labs/04-industry/57-zip-headers-with-values-into-an-object/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-57-zip-headers-with-values-into-an-object-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  reduce ((pair, acc = {}) -> acc ++ { (pair[0]): pair[1] })
```

**SAY:** That should match Expected:

```
{ "Name": "Asha", "Amount": "10.5", "City": "Pune" }
```

## Part 4 — Interview phrase and close

**SAY:**

zip headers with values. Reduce into an object. Parentheses around the key.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 58 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 57

Zip headers with values into an object

## Expected

```
{ "Name": "Asha", "Amount": "10.5", "City": "Pune" }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
