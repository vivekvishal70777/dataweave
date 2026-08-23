# LAB 42 — Write namespaced XML from canonical JSON

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/42-write-namespaced-xml-from-canonical-json/` |
| Solution | `instructor/solutions/03-advanced/42-write-namespaced-xml-from-canonical-json/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-42-write-namespaced-xml-from-canonical-json.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 42. Write namespaced XML from canonical JSON. Inverse of 41: JSON → `ord:PurchaseOrder` with line attributes. One root. MIME `application/xml`.

Write ns hash PurchaseOrder and Line attributes. One root.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 42 — Write namespaced XML from canonical JSON**
> Folder: `student/labs/03-advanced/42-write-namespaced-xml-from-canonical-json/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-42-write-namespaced-xml-from-canonical-json-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
ns ord http://acme.com/order
output application/xml
---
ord#PurchaseOrder @(id: payload.orderId, currency: payload.currency): {
  (payload.lines map (li) -> {
    ord#Line @(sku: li.sku, qty: li.qty, unitPrice: li.unitPrice): {}
  })
}
```

**SAY:** That should match Expected:

_No expected block in the reference drill; run the solution on camera and show the preview._

## Part 4 — Interview phrase and close

**SAY:**

Write ns hash PurchaseOrder and Line attributes. One root.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 43 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 42

Write namespaced XML from canonical JSON

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
