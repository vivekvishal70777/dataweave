# LAB 48 — Validate and partition good vs bad rows

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/48-validate-and-partition-good-vs-bad-rows/` |
| Solution | `instructor/solutions/03-advanced/48-validate-and-partition-good-vs-bad-rows/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-48-validate-and-partition-good-vs-bad-rows.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 48. Validate and partition good vs bad rows. A row is valid if `email` contains `"@"` and `age` is a Number `>= 18`. Return `{ valid, invalid }`.

Partition with groupBy a boolean or two filters. Call out valid versus errors.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "email": "a@x.com", "age": 20 }, { "email": "bad", "age": 17 }, { "email": "b@x.com", "age": "x" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 48 — Validate and partition good vs bad rows**
> Folder: `student/labs/03-advanced/48-validate-and-partition-good-vs-bad-rows/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-48-validate-and-partition-good-vs-bad-rows-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
import try from dw::Runtime
output application/json
fun isValid(r) = do {
  var ageOk = try(() -> (r.age as Number) >= 18).success default false
  ---
  (r.email default "") contains "@" and ageOk
}
---
{
  valid: payload filter isValid($),
  invalid: payload filter !isValid($)
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Partition with groupBy a boolean or two filters. Call out valid versus errors.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 49 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 48

Validate and partition good vs bad rows

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
