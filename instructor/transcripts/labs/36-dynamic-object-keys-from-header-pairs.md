# LAB 36 — Dynamic object keys from header pairs

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/36-dynamic-object-keys-from-header-pairs/` |
| Solution | `instructor/solutions/02-intermediate/36-dynamic-object-keys-from-header-pairs/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-36-dynamic-object-keys-from-header-pairs.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 36. Dynamic object keys from header pairs. HTTP/query pairs `[{ "k": "X-Request-Id", "v": "abc" }]` → object. Parentheses around the key expression.

Parentheses around header names as keys. Without them the key is literal k.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "k": "X-Request-Id", "v": "abc-123" },
  { "k": "X-Correlation-Id", "v": "corr-9" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 36 — Dynamic object keys from header pairs**
> Folder: `student/labs/02-intermediate/36-dynamic-object-keys-from-header-pairs/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-36-dynamic-object-keys-from-header-pairs-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload reduce ((p, acc = {}) -> acc ++ { (p.k): p.v })
```

**SAY:** That should match Expected:

```
{ "X-Request-Id": "abc-123", "X-Correlation-Id": "corr-9" }
```

## Part 4 — Interview phrase and close

**SAY:**

Parentheses around header names as keys. Without them the key is literal k.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 37 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 36

Dynamic object keys from header pairs

## Expected

```
{ "X-Request-Id": "abc-123", "X-Correlation-Id": "corr-9" }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
