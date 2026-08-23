# LAB 26 — Update nested city to uppercase (Mule 4.3+)

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/26-update-nested-city-to-uppercase-mule-4-3/` |
| Solution | `instructor/solutions/02-intermediate/26-update-nested-city-to-uppercase-mule-4-3/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-26-update-nested-city-to-uppercase-mule-4-3.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 26. Update nested city to uppercase (Mule 4.3+). Uppercase `customer.address.city` without rebuilding the whole tree by hand.

update needs Mule 4.3 plus. Case path to city, then upper of dollar.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "customer": { "id": "C-9", "address": { "city": "pune", "postalCode": "411001" } } }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 26 — Update nested city to uppercase (Mule 4.3+)**
> Folder: `student/labs/02-intermediate/26-update-nested-city-to-uppercase-mule-4-3/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-26-update-nested-city-to-uppercase-mule-4-3-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
}
```

**SAY:** That should match Expected:

city `"PUNE"`, other fields unchanged.

## Part 4 — Interview phrase and close

**SAY:**

update needs Mule 4.3 plus. Case path to city, then upper of dollar.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 27 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 26

Update nested city to uppercase (Mule 4.3+)

## Expected (note)

city `"PUNE"`, other fields unchanged.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
