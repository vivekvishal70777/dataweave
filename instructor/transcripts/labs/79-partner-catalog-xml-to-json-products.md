# LAB 79 — Partner catalog XML to JSON products

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/79-partner-catalog-xml-to-json-products/` |
| Solution | `instructor/solutions/05-mapping/79-partner-catalog-xml-to-json-products/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-79-partner-catalog-xml-to-json-products.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 79. Partner catalog XML to JSON products. Read attributes id and repeating Item. price as Number. Single XML root.

Partner XML ns URI. Star Item. Attribute id. Price as Number.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```xml
<Catalog xmlns="http://partner.example/cat">
  <Item id="I1"><Name>Bolt</Name><Price>2.5</Price></Item>
  <Item id="I2"><Name>Nut</Name><Price>0.75</Price></Item>
</Catalog>
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 79 — Partner catalog XML to JSON products**
> Folder: `student/labs/05-mapping/79-partner-catalog-xml-to-json-products/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-79-partner-catalog-xml-to-json-products-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
ns cat http://partner.example/cat
output application/json
---
payload.cat#Catalog.*cat#Item map {
  id: $.@id,
  name: $.cat#Name,
  price: $.cat#Price as Number
}
```

**SAY:** That should match Expected:

```
[
  { "id": "I1", "name": "Bolt", "price": 2.5 },
  { "id": "I2", "name": "Nut", "price": 0.75 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Partner XML ns URI. Star Item. Attribute id. Price as Number.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 80 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 79

Partner catalog XML to JSON products

## Expected

```
[
  { "id": "I1", "name": "Bolt", "price": 2.5 },
  { "id": "I2", "name": "Nut", "price": 0.75 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
