# LAB 60 — SAP-style order JSON to canonical invoice with GST

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/60-sap-style-order-json-to-canonical-invoice-with-gst/` |
| Solution | `instructor/solutions/05-mapping/60-sap-style-order-json-to-canonical-invoice-with-gst/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-60-sap-style-order-json-to-canonical-invoice-with-gst.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 60. SAP-style order JSON to canonical invoice with GST. Skip lines with qty 0. `fun money`. Line net = qty * price * (1 - discount). CGST+SGST vs IGST 18% by comparing ship-from and ship-to state. Grand total = subtotal + tax.

Filter qty greater than zero. Discount then GST 18. fun money. Intra-state CGST_SGST vs IGST.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "vbeln": "80001234",
  "waerk": "INR",
  "shipFromState": "MH",
  "shipToState": "MH",
  "lines": [
    { "matnr": "MAT-1", "qty": "2", "netpr": "100.00", "disc": "0.10" },
    { "matnr": "MAT-2", "qty": "0", "netpr": "50", "disc": "0" },
    { "matnr": "MAT-3", "qty": 1, "netpr": "40.5", "disc": 0 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 60 — SAP-style order JSON to canonical invoice with GST**
> Folder: `student/labs/05-mapping/60-sap-style-order-json-to-canonical-invoice-with-gst/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-60-sap-style-order-json-to-canonical-invoice-with-gst-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var intra = payload.shipFromState == payload.shipToState
var raw = payload.lines filter ((l) -> (l.qty as Number) > 0) map (l) -> do {
  var qty = l.qty as Number
  var price = l.netpr as Number
  var disc = (l.disc default 0) as Number
  ---
  { sku: l.matnr, qty: qty, net: money(qty * price * (1 - disc)) }
}
var sub = money(sum(raw.net))
var tax = money(sub * 0.18)
---
{
  invoiceId: payload.vbeln,
  currency: payload.waerk,
  taxCode: if (intra) "CGST_SGST" else "IGST",
  lines: raw,
  subtotal: sub,
  tax: tax,
  grandTotal: money(sub + tax)
}
```

**SAY:** That should match Expected:

```
{
  "invoiceId": "80001234",
  "currency": "INR",
  "taxCode": "CGST_SGST",
  "lines": [
    { "sku": "MAT-1", "qty": 2, "net": 180.00 },
    { "sku": "MAT-3", "qty": 1, "net": 40.50 }
  ],
  "subtotal": 220.50,
  "tax": 39.69,
  "grandTotal": 260.19
}
```

## Part 4 — Interview phrase and close

**SAY:**

Filter qty greater than zero. Discount then GST 18. fun money. Intra-state CGST_SGST vs IGST.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 61 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 60

SAP-style order JSON to canonical invoice with GST

## Expected

```
{
  "invoiceId": "80001234",
  "currency": "INR",
  "taxCode": "CGST_SGST",
  "lines": [
    { "sku": "MAT-1", "qty": 2, "net": 180.00 },
    { "sku": "MAT-3", "qty": 1, "net": 40.50 }
  ],
  "subtotal": 220.50,
  "tax": 39.69,
  "grandTotal": 260.19
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
