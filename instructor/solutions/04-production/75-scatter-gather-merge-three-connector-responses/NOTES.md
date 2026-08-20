# Instructor solution — Lab 75

Scatter-gather: merge three connector responses

## Expected

```
{
  "ok": {
    "crm": { "id": "C1" },
    "mdm": { "id": "M1" }
  },
  "errors": [
    { "name": "erp", "status": 500, "body": { "error": "down" } }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
