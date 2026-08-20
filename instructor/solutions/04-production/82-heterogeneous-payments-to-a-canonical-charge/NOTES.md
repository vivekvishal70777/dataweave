# Instructor solution — Lab 82

Heterogeneous payments to a canonical charge

## Expected

```
[
  { "method": "card", "instrument": "4242", "ref": "A1" },
  { "method": "upi", "instrument": "asha@upi", "ref": "U9" },
  { "method": "netbanking", "instrument": "HDFC", "ref": "N3" },
  { "method": "other", "instrument": null, "ref": null }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
