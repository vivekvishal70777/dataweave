# LAB 04 — Uppercase string fields on an address object

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/04-uppercase-string-fields-on-an-address-object/` |
| Solution | `instructor/solutions/01-fundamentals/04-uppercase-string-fields-on-an-address-object/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-04-uppercase-string-fields-on-an-address-object.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 04. Uppercase string fields on an address object. Uppercase every

mapObject walks keys and values. Uppercase only string values; leave postal codes as numbers.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{ "city": "pune", "country": "india", "postalCode": 411001 }
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 04 — Uppercase string fields on an address object**
> Folder: `student/labs/01-fundamentals/04-uppercase-string-fields-on-an-address-object/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-04-uppercase-string-fields-on-an-address-object-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload mapObject ((v, k) -> {
  (k): v match {
    case s is String -> upper(s)
    else -> v
  }
})
```

**SAY:** That should match Expected:

```
{ "city": "PUNE", "country": "INDIA", "postalCode": 411001 }
```

## Part 4 — Interview phrase and close

**SAY:**

mapObject walks keys and values. Uppercase only string values; leave postal codes as numbers.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 05 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 04

Uppercase string fields on an address object

## Expected

```
{ "city": "PUNE", "country": "INDIA", "postalCode": 411001 }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
