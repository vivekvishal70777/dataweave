# Lab 08 — Add GST to a unit price (2 decimal money)

**Level:** easy  
**Section folder:** `01-fundamentals`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** GST 18%. Return `{ price, tax, total }` as numbers with **2 decimal places** (writer-style rounding via `format`).

**Input:**

```json
{ "price": 99.99 }
```

**Expected:**

```json
{ "price": 99.99, "tax": 18.00, "total": 117.99 }
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
