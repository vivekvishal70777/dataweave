# Lab 73 — India GST split CGST SGST vs IGST by state

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Same state: half of 18% each CGST and SGST. Different: full IGST 18%. fun money on taxable amount.

**Input:**

```json
{
  "fromState": "KA",
  "toState": "MH",
  "taxable": "1000.00"
}
```

**Expected:**

```json
{
  "taxable": 1000.00,
  "cgst": 0.00,
  "sgst": 0.00,
  "igst": 180.00
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
