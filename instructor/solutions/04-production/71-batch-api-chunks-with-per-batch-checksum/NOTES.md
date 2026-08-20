# Instructor solution — Lab 71

Batch API chunks with per-batch checksum

## Expected

```
[
  { "batchId": "B1", "count": 2, "ids": [1, 2], "checksum": 3 },
  { "batchId": "B2", "count": 2, "ids": [3, 4], "checksum": 7 },
  { "batchId": "B3", "count": 1, "ids": [5], "checksum": 5 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
