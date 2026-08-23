# Instructor solution — Lab 85

Manufacturing routing duration by work order

## Expected

```
[
  {
    "wo": "WO1",
    "steps": [
      { "seq": 10, "step": "CUT", "min": 30 },
      { "seq": 20, "step": "PAINT", "min": 15 }
    ],
    "totalMinutes": 45
  },
  {
    "wo": "WO2",
    "steps": [
      { "seq": 10, "step": "PACK", "min": 5 }
    ],
    "totalMinutes": 5
  }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
