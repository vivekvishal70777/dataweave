# Instructor solution — Lab 65

Wrap a domain payload as CloudEvents 1.0

## Expected

```
{
  "specversion": "1.0",
  "id": "e-100",
  "source": "urn:mule:orders",
  "type": "com.acme.order.created",
  "time": "2026-08-20T08:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "orderId": "O-1",
    "amount": 99
  }
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
