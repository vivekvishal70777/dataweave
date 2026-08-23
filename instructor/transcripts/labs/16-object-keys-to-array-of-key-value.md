# LAB 16 — Object keys to array of `{ key, value }`

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/16-object-keys-to-array-of-key-value/` |
| Solution | `instructor/solutions/01-fundamentals/16-object-keys-to-array-of-key-value/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-16-object-keys-to-array-of-key-value.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 16. Object keys to array of `{ key, value }`. Convert `{ "a": 1, "b": 2 }` to entries.

pluck turns an object into an array of key-value pairs. mapObject would keep an object.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "a": 1, "b": 2 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 16 — Object keys to array of `{ key, value }`**
> Folder: `student/labs/01-fundamentals/16-object-keys-to-array-of-key-value/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-16-object-keys-to-array-of-key-value-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload pluck ((v, k) -> { key: k, value: v })
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

pluck turns an object into an array of key-value pairs. mapObject would keep an object.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 17 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 16

Object keys to array of `{ key, value }`

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
