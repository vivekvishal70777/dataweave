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
