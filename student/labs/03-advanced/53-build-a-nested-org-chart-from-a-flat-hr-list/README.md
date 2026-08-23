# Lab 53 — Build a nested org chart from a flat HR list

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Flat employees + `managerId` → nested `children`. Index by manager. Roots have `managerId: null`.

**Input:**

```json
[
  { "id": "1", "name": "CEO", "managerId": null },
  { "id": "2", "name": "Eng", "managerId": "1" },
  { "id": "3", "name": "Dev", "managerId": "2" }
]
```

**Expected:** CEO → children Eng → children Dev.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
