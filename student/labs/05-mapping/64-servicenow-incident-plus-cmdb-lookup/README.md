# Lab 64 — ServiceNow incident plus CMDB lookup

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** ciName from cmdb; missing UNASSIGNED. Priority 1-2 stay, else sev 3.

**Input:**

```json
{
  "cmdb": [
    { "sys_id": "ci1", "name": "sap-prd-db" }
  ],
  "incidents": [
    { "number": "INC001", "cmdb_ci": "ci1", "priority": "1", "opened_at": "2026-08-01T04:00:00Z" },
    { "number": "INC002", "cmdb_ci": "gone", "priority": "3", "opened_at": "2026-08-02T10:00:00Z" }
  ]
}
```

**Expected:**

```json
[
  { "ticket": "INC001", "ciName": "sap-prd-db", "sev": 1, "openedAt": "2026-08-01T04:00:00Z" },
  { "ticket": "INC002", "ciName": "UNASSIGNED", "sev": 3, "openedAt": "2026-08-02T10:00:00Z" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
