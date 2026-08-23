# Instructor solution — Lab 65

Debezium CDC envelope to flat upsert rows

## Expected

```
[
  { "action": "UPSERT", "id": "A1", "status": "NEW", "tsMs": 100 },
  { "action": "UPSERT", "id": "A1", "status": "PAID", "tsMs": 101 },
  { "action": "DELETE", "id": "B9", "status": "X", "tsMs": 102 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
