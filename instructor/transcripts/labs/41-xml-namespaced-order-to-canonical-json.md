# LAB 41 — XML namespaced order to canonical JSON

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/41-xml-namespaced-order-to-canonical-json/` |
| Solution | `instructor/solutions/03-advanced/41-xml-namespaced-order-to-canonical-json/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-41-xml-namespaced-order-to-canonical-json.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 41. XML namespaced order to canonical JSON. Map `ns0:order` with repeating `ns0:line` and attribute `id`.

Declare ns. Repeating line items with star. Attributes with at-sign.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```xml
<ns0:order xmlns:ns0="http://acme.com/order" id="O-1">
  <ns0:line sku="A" qty="2"/>
  <ns0:line sku="B" qty="1"/>
</ns0:order>
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 41 — XML namespaced order to canonical JSON**
> Folder: `student/labs/03-advanced/41-xml-namespaced-order-to-canonical-json/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-41-xml-namespaced-order-to-canonical-json-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
ns ns0 http://acme.com/order
output application/json
---
{
  orderId: payload.ns0#order.@id,
  lines: payload.ns0#order.*ns0#line map {
    sku: $.@sku,
    qty: $.@qty as Number
  }
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Declare ns. Repeating line items with star. Attributes with at-sign.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 42 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 41

XML namespaced order to canonical JSON

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
