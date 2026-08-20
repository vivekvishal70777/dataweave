# Lab 63 — FIFO stock allocation across warehouses

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Allocate `need` units from warehouses ordered by `priority` ascending. Each allocation `{ warehouseId, qty }`. `shortfall` is leftover demand.

**Input:**

```json
{
  "need": 7,
  "warehouses": [
    { "id": "W2", "qty": 10, "priority": 2 },
    { "id": "W1", "qty": 4, "priority": 1 }
  ]
}
```

**Expected:**

```json
{
  "allocations": [
    { "warehouseId": "W1", "qty": 4 },
    { "warehouseId": "W2", "qty": 3 }
  ],
  "shortfall": 0
}
```

**Interview talking point:** This is a **running remainder** (`reduce`). Inventory writes still happen in the backend; DataWeave only shapes the allocation plan.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
