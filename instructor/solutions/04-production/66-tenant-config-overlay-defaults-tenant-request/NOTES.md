# Instructor solution — Lab 66

Tenant config overlay (defaults < tenant < request)

## Expected

```
{
  "timeoutMs": 9000,
  "region": "in",
  "featureFlags": ["b", "c"],
  "retry": { "max": 4, "backoffMs": 250 }
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
