# Lab 85 — Manufacturing routing duration by work order

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Sum step minutes per wo, order steps by seq. Output wo, steps[], totalMinutes.

**Input:**

```json
[
  { "wo": "WO1", "seq": 20, "step": "PAINT", "min": "15" },
  { "wo": "WO1", "seq": 10, "step": "CUT", "min": 30 },
  { "wo": "WO2", "seq": 10, "step": "PACK", "min": 5 }
]
```

**Expected:**

```json
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

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
