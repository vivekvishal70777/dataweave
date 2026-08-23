# Lab 31 — Left join orders to customers

**Level:** moderate  
**Section folder:** `02-intermediate`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** `payload.orders` left-join `payload.customers` on `customerId` / `id`. Output `orderId`, `customerName` (`null` if missing). Include the unmatched order.

**Input:**

```json
{
  "orders": [
    { "id": "O1", "customerId": "C1" },
    { "id": "O2", "customerId": "C9" }
  ],
  "customers": [{ "id": "C1", "name": "Asha Rao" }]
}
```

**Expected:** O1 named, O2 `customerName` null.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
