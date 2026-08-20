# Instructor solution — Lab 81

Dead-letter / replay envelope

## Expected

```
{
  "replayKey": "C1|O-1",
  "failedAt": "2026-08-20T08:00:00Z",
  "errorType": "HTTP:CONNECTIVITY",
  "original": { "orderId": "O-1", "customerId": "C1" }
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
