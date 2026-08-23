# Lab 61 — Workday workers to HR API (active only)

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Keep Active workers (any case). `fullName` from legal names. `managerId` from `manager.wid` (null-safe). Coerce `fte`.

**Input:**

```json
{
  "Report_Entry": [
    { "wid": "W1", "Legal_First": "Ira", "Legal_Last": "Shah", "Status": "Active", "FTE": "1.0", "manager": { "wid": "W9" } },
    { "wid": "W2", "Legal_First": "Jon", "Legal_Last": "Lee", "Status": "Terminated", "FTE": "1", "manager": {} },
    { "wid": "W3", "Legal_First": "Mia", "Legal_Last": "Das", "Status": "active", "FTE": 0.5 }
  ]
}
```

**Expected:**

```json
[
  { "id": "W1", "fullName": "Ira Shah", "fte": 1.0, "managerId": "W9" },
  { "id": "W3", "fullName": "Mia Das", "fte": 0.5, "managerId": null }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
