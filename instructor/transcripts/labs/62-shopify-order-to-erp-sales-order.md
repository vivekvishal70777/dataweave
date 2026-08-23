# LAB 62 — Shopify order to ERP sales order

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/62-shopify-order-to-erp-sales-order/` |
| Solution | `instructor/solutions/05-mapping/62-shopify-order-to-erp-sales-order/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-62-shopify-order-to-erp-sales-order.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 62. Shopify order to ERP sales order. Map line_items; skip SKU GIFT. Money strings. soldTo = last then first. channel WEB.

Skip GIFT sku. soldTo last then first. price as Number with fun money.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "id": 991,
  "currency": "USD",
  "shipping_address": { "first_name": "Sam", "last_name": "Patel" },
  "line_items": [
    { "sku": "TEE-M", "quantity": 2, "price": "19.99" },
    { "sku": "GIFT", "quantity": 1, "price": "25.00" },
    { "sku": "HAT", "quantity": 1, "price": "12.5" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 62 — Shopify order to ERP sales order**
> Folder: `student/labs/05-mapping/62-shopify-order-to-erp-sales-order/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-62-shopify-order-to-erp-sales-order-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  erpOrderId: payload.id as String,
  currency: payload.currency,
  channel: "WEB",
  soldTo: (payload.shipping_address.last_name default "") ++ " " ++ (payload.shipping_address.first_name default ""),
  lines: payload.line_items
    filter ((l) -> l.sku != "GIFT")
    map { sku: $.sku, qty: $.quantity as Number, unitPrice: money($.price as Number) }
}
```

**SAY:** That should match Expected:

```
{
  "erpOrderId": "991",
  "currency": "USD",
  "channel": "WEB",
  "soldTo": "Patel Sam",
  "lines": [
    { "sku": "TEE-M", "qty": 2, "unitPrice": 19.99 },
    { "sku": "HAT", "qty": 1, "unitPrice": 12.50 }
  ]
}
```

## Part 4 — Interview phrase and close

**SAY:**

Skip GIFT sku. soldTo last then first. price as Number with fun money.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 63 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 62

Shopify order to ERP sales order

## Expected

```
{
  "erpOrderId": "991",
  "currency": "USD",
  "channel": "WEB",
  "soldTo": "Patel Sam",
  "lines": [
    { "sku": "TEE-M", "qty": 2, "unitPrice": 19.99 },
    { "sku": "HAT", "qty": 1, "unitPrice": 12.50 }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
