# Lab 55 — Canonical order API with line errors

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Map a commerce order to a canonical JSON API. Compute `lineTotal`, `subtotal`, `tax`, `grandTotal`. If a line has a non-numeric `qty` or `price`, omit it from `lines` and append `{ sku, reason }` to `errors`. Missing `customerId` becomes `null` (do not fail the whole document).

**Production rules:** Round money to 2 decimal places via `as String {format: "0.00"} as Number`. Tax applies only to the successful subtotal. Keep `correlationId` from the source.

**Input:**

```json
{
  "correlationId": "corr-9",
  "customerId": null,
  "taxRate": 0.18,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50 },
    { "sku": "B", "qty": "bad", "price": 100 },
    { "sku": "C", "qty": 1, "price": 100 }
  ]
}
```

**Expected:**

```json
{
  "correlationId": "corr-9",
  "customerId": null,
  "lines": [
    { "sku": "A", "qty": 2, "price": 50, "lineTotal": 100 },
    { "sku": "C", "qty": 1, "price": 100, "lineTotal": 100 }
  ],
  "subtotal": 200,
  "tax": 36,
  "grandTotal": 236,
  "errors": [
    { "sku": "B", "reason": "qty or price is not numeric" }
  ]
}
```

**Interview talking point:** Partial success is normal in B2B: ship the good lines, park bad lines in `errors[]` (or a DLQ field). Do not hide HTTP/DB calls inside the `map`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
