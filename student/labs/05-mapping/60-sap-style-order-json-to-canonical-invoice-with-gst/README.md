# Lab 60 — SAP-style order JSON to canonical invoice with GST

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Skip lines with qty 0. `fun money`. Line net = qty * price * (1 - discount). CGST+SGST vs IGST 18% by comparing ship-from and ship-to state. Grand total = subtotal + tax.

**Input:**

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

**Expected:**

```json
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

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
