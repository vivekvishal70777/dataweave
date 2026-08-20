# Instructor solution — Lab 58

Multi-currency invoice with FX table

## Expected

```
{
  "lines": [
    { "sku": "A", "amount": 100, "currency": "EUR", "amountUsd": 110 },
    { "sku": "B", "amount": 50, "currency": "USD", "amountUsd": 50 }
  ],
  "totalUsd": 160,
  "errors": [
    { "sku": "C", "reason": "missing FX rate for GBP" }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
