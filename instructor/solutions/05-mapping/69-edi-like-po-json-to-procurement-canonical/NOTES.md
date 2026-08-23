# Instructor solution — Lab 69

EDI-like PO JSON to procurement canonical

## Expected

```
{
  "poNum": "PO-77",
  "vendor": "V-9",
  "lines": [
    { "sku": "BOLT", "qty": 10, "needBy": "2026-08-20" }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
