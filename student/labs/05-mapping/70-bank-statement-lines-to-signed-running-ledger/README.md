# Lab 70 — Bank statement lines to signed running ledger

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** CR positive, DR negative. Running balance from 0. fun money.

**Input:**

```json
[
  { "nar": "SALARY", "dc": "CR", "amt": "1000.00" },
  { "nar": "UPI", "dc": "DR", "amt": "250.5" },
  { "nar": "REV", "dc": "CR", "amt": "50" }
]
```

**Expected:**

```json
[
  { "narration": "SALARY", "amount": 1000.00, "balance": 1000.00 },
  { "narration": "UPI", "amount": -250.50, "balance": 749.50 },
  { "narration": "REV", "amount": 50.00, "balance": 799.50 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
