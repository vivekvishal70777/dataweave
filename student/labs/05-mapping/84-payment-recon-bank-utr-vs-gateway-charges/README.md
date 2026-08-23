# Lab 84 — Payment recon: bank UTR vs gateway charges

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Match on utr. Status MATCHED if amounts equal (as Number), AMOUNT_MISMATCH if both exist else UNMATCHED. Include both sides.

**Input:**

```json
{
  "bank": [
    { "utr": "U1", "amt": "100.00" },
    { "utr": "U2", "amt": "40" }
  ],
  "gateway": [
    { "utr": "U1", "amt": 100 },
    { "utr": "U3", "amt": 9 }
  ]
}
```

**Expected:**

```json
[
  { "utr": "U1", "status": "MATCHED", "bank": 100.00, "gateway": 100.00 },
  { "utr": "U2", "status": "UNMATCHED", "bank": 40.00, "gateway": null },
  { "utr": "U3", "status": "UNMATCHED", "bank": null, "gateway": 9.00 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
