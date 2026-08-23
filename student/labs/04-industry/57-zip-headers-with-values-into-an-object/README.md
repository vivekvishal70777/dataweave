# Lab 57 — Zip headers with values into an object

**Level:** industry  
**Section folder:** `04-industry`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Dynamic columns: `headers` + `values` (same length). Build `{ Name: "Asha", Amount: "10.5" }` using `zip` and dynamic keys.

**Input:**

```json
{
  "headers": ["Name", "Amount", "City"],
  "values": ["Asha", "10.5", "Pune"]
}
```

**Expected:**

```json
{ "Name": "Asha", "Amount": "10.5", "City": "Pune" }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
