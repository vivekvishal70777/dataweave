# Lab 01 — Map employee JSON to a shorter shape

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** From each employee, output `fullName` (first + last) and `dept`.

**Input:**

```json
[
  { "firstName": "Asha", "lastName": "Rao", "department": "IT" },
  { "firstName": "Ben", "lastName": "Cole", "department": "HR" }
]
```

**Expected:**

```json
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "HR" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
