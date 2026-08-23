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
