# LAB 68 — Normalize IN vs US postal addresses

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/68-normalize-in-vs-us-postal-addresses/` |
| Solution | `instructor/solutions/05-mapping/68-normalize-in-vs-us-postal-addresses/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-68-normalize-in-vs-us-postal-addresses.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 68. Normalize IN vs US postal addresses. IN: pin as postal. US: first 5 of zip. Uppercase city.

IN uses pin. US zip first five chars. Upper city.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "country": "IN", "addr1": "Lane 2", "city": "pune", "pin": "411001", "zip": null },
  { "country": "US", "addr1": "1 Main", "city": "austin", "pin": null, "zip": "78701-1234" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 68 — Normalize IN vs US postal addresses**
> Folder: `student/labs/05-mapping/68-normalize-in-vs-us-postal-addresses/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-68-normalize-in-vs-us-postal-addresses-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload map (a) -> {
  country: a.country,
  line1: a.addr1,
  city: upper(a.city),
  postal: if (a.country == "IN") a.pin as String
          else (a.zip as String)[0 to 4]
}
```

**SAY:** That should match Expected:

```
[
  { "country": "IN", "line1": "Lane 2", "city": "PUNE", "postal": "411001" },
  { "country": "US", "line1": "1 Main", "city": "AUSTIN", "postal": "78701" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

IN uses pin. US zip first five chars. Upper city.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 69 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 68

Normalize IN vs US postal addresses

## Expected

```
[
  { "country": "IN", "line1": "Lane 2", "city": "PUNE", "postal": "411001" },
  { "country": "US", "line1": "1 Main", "city": "AUSTIN", "postal": "78701" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
