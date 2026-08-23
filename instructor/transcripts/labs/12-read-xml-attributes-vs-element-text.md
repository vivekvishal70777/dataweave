# LAB 12 — Read XML attributes vs element text

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/12-read-xml-attributes-vs-element-text/` |
| Solution | `instructor/solutions/01-fundamentals/12-read-xml-attributes-vs-element-text/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-12-read-xml-attributes-vs-element-text.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 12. Read XML attributes vs element text. From an order XML with `id`

Attributes use the at-sign. Element text is a child, not at-id.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```xml
<order id="O-9"><amount>50.00</amount></order>
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 12 — Read XML attributes vs element text**
> Folder: `student/labs/01-fundamentals/12-read-xml-attributes-vs-element-text/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-12-read-xml-attributes-vs-element-text-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
{
  id: payload.order.@id,
  amount: payload.order.amount as Number
}
```

**SAY:** That should match Expected:

```
{ "id": "O-9", "amount": 50.00 }
```

## Part 4 — Interview phrase and close

**SAY:**

Attributes use the at-sign. Element text is a child, not at-id.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 13 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 12

Read XML attributes vs element text

## Expected

```
{ "id": "O-9", "amount": 50.00 }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
