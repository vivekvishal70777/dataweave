# Instructor solution — Lab 55

Canonical order API with line errors

## Expected

```
{
  "correlationId": "corr-9",
  "customerId": null,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50, "lineTotal": 100 },
    { "sku": "C", "qty": 1, "price": 100, "lineTotal": 100 }
  ],
  "subtotal": 200,
  "tax": 36,
  "grandTotal": 236,
  "errors": [
    { "sku": "B", "reason": "qty or price is not numeric" }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
