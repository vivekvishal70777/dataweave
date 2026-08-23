# Lab 80 — Health claims flatten ICD diagnosis codes

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** One output row per diagnosis. Copy claimId and member. Skip empty codes.

**Input:**

```json
{
  "claims": [
    { "claimId": "CL-1", "member": "M9", "dx": ["E11.9", "I10"] },
    { "claimId": "CL-2", "member": "M9", "dx": [""] }
  ]
}
```

**Expected:**

```json
[
  { "claimId": "CL-1", "member": "M9", "icd": "E11.9" },
  { "claimId": "CL-1", "member": "M9", "icd": "I10" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
