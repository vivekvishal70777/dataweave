# Lab 59 — Bill of materials: explode one level

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Each product has `components` (sku list). Replace each component sku with `{ sku, name, unitCost }` from `catalog`. Unknown sku → `{ sku, name: null, unitCost: null, missing: true }`. Output the parent with `exploded` and `bomCost` (sum of known costs only).

**Input:**

```json
{
  "catalog": [
    { "sku": "P", "name": "Pump", "unitCost": 10, "components": ["G", "S"] },
    { "sku": "G", "name": "Gasket", "unitCost": 2, "components": [] },
    { "sku": "S", "name": "Screw", "unitCost": 1, "components": [] }
  ],
  "parentSku": "P"
}
```

**Expected:**

```json
{
  "sku": "P",
  "name": "Pump",
  "exploded": [
    { "sku": "G", "name": "Gasket", "unitCost": 2, "missing": false },
    { "sku": "S", "name": "Screw", "unitCost": 1, "missing": false }
  ],
  "bomCost": 3
}
```

**Interview talking point:** One-level explode is a **groupBy catalog** lookup. Multi-level explode is recursion plus a cycle guard (visited set) — mention it; do not infinite-loop in production.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
