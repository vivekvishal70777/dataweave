# Instructor solution — Lab 74

Flatten nested JSON to dotted paths

## Expected

```
{
  "orderId": "O-1",
  "customer.name": "Asha",
  "customer.addr.city": "Pune",
  "lines.0.sku": "A",
  "lines.0.qty": 2,
  "lines.1.sku": "B",
  "lines.1.qty": 1
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
