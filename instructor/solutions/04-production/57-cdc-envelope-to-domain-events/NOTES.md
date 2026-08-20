# Instructor solution — Lab 57

CDC envelope to domain events

## Expected

```
[
  { "type": "created", "id": "1", "record": { "id": "1", "name": "Asha" }, "ts": "2026-08-20T10:00:00Z" },
  { "type": "updated", "id": "1", "record": { "id": "1", "name": "Asha R" }, "ts": "2026-08-20T11:00:00Z" },
  { "type": "deleted", "id": "2", "record": { "id": "2" }, "ts": "2026-08-20T12:00:00Z" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
