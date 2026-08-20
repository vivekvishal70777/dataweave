# Instructor solution — Lab 77

Keep latest version per id (upsert projection)

## Expected

```
[
  { "id": "A", "version": 3, "payload": { "name": "new" } },
  { "id": "B", "version": 1, "payload": { "name": "b" } }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
