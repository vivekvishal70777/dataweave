# LAB 41 — SOAP namespaced purchase order to canonical JSON

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/41-soap-namespaced-purchase-order-to-canonical-json/` |
| Solution | `instructor/solutions/03-advanced/41-soap-namespaced-purchase-order-to-canonical-json/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-41-soap-namespaced-purchase-order-to-canonical-json.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 41. SOAP namespaced purchase order to canonical JSON. Strip SOAP envelope, read `ord:PurchaseOrder` attributes and repeating `ord:Line` attributes. Two prefixes. This is a standard hard XML interview.

Two ns prefixes. Envelope Body PurchaseOrder. Star Line. Attributes with at-sign.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ord="http://acme.com/order">
  <soap:Body>
    <ord:PurchaseOrder id="PO-1001" currency="INR">
      <ord:Line sku="SKU-A" qty="2" unitPrice="50.00"/>
      <ord:Line sku="SKU-B" qty="1" unitPrice="100.00"/>
    </ord:PurchaseOrder>
  </soap:Body>
</soap:Envelope>
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 41 — SOAP namespaced purchase order to canonical JSON**
> Folder: `student/labs/03-advanced/41-soap-namespaced-purchase-order-to-canonical-json/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-41-soap-namespaced-purchase-order-to-canonical-json-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
ns soap http://schemas.xmlsoap.org/soap/envelope/
ns ord http://acme.com/order
output application/json
---
{
  orderId: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@id,
  currency: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@currency,
  lines: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.*ord#Line map {
    sku: $.@sku,
    qty: $.@qty as Number,
    unitPrice: $.@unitPrice as Number
  }
}
```

**SAY:** That should match Expected:

```
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

## Part 4 — Interview phrase and close

**SAY:**

Two ns prefixes. Envelope Body PurchaseOrder. Star Line. Attributes with at-sign.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 42 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 41

SOAP namespaced purchase order to canonical JSON

## Expected

```
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
