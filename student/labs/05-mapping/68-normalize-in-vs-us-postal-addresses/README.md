# Lab 68 — Normalize IN vs US postal addresses

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** IN: pin as postal. US: first 5 of zip. Uppercase city.

**Input:**

```json
[
  { "country": "IN", "addr1": "Lane 2", "city": "pune", "pin": "411001", "zip": null },
  { "country": "US", "addr1": "1 Main", "city": "austin", "pin": null, "zip": "78701-1234" }
]
```

**Expected:**

```json
[
  { "country": "IN", "line1": "Lane 2", "city": "PUNE", "postal": "411001" },
  { "country": "US", "line1": "1 Main", "city": "AUSTIN", "postal": "78701" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
