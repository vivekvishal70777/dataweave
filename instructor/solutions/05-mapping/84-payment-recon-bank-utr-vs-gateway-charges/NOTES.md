# Instructor solution — Lab 84

Payment recon: bank UTR vs gateway charges

## Expected

```
[
  { "utr": "U1", "status": "MATCHED", "bank": 100.00, "gateway": 100.00 },
  { "utr": "U2", "status": "UNMATCHED", "bank": 40.00, "gateway": null },
  { "utr": "U3", "status": "UNMATCHED", "bank": null, "gateway": 9.00 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
