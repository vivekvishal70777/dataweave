# Lab 01 — Map Salesforce Contact to a shorter API shape

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** From each Contact, output `fullName` (FirstName + LastName, single space) and `dept` from `Department`. Skip building Java-style loops.

**Input:**

```json
[
  { "Id": "003xx000001", "FirstName": "Asha", "LastName": "Rao", "Department": "IT", "Email": "asha@acme.com" },
  { "Id": "003xx000002", "FirstName": "Ben", "LastName": "Cole", "Department": "Finance", "Email": "ben@acme.com" }
]
```

**Expected:**

```json
[
  { "fullName": "Asha Rao", "dept": "IT" },
  { "fullName": "Ben Cole", "dept": "Finance" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
