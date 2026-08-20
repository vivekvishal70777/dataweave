# Instructor solution — Lab 79

Log-safe HTTP headers (redact secrets)

## Expected

```
{
  "Authorization": "****",
  "X-Correlation-Id": "corr-9",
  "Cookie": "****",
  "Accept": "application/json"
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
