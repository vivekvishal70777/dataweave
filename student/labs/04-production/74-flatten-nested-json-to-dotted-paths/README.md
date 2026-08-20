# Lab 74 — Flatten nested JSON to dotted paths

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Produce a flat object for analytics/CSV. Object keys join with `.`. Arrays use numeric indexes. Leaf values stay as-is.

**Input:**

```json
{
  "orderId": "O-1",
  "customer": { "name": "Asha", "addr": { "city": "Pune" } },
  "lines": [
    { "sku": "A", "qty": 2 },
    { "sku": "B", "qty": 1 }
  ]
}
```

**Expected:**

```json
{
  "orderId": "O-1",
  "customer.name": "Asha",
  "customer.addr.city": "Pune",
  "lines.0.sku": "A",
  "lines.0.qty": 2,
  "lines.1.sku": "B",
  "lines.1.qty": 1
}
```

**Interview talking point:** Dotted flatten is how many data lakes ingest API JSON. Watch streaming: this **walks the whole tree**.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
