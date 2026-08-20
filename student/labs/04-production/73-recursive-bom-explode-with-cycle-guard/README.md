# Lab 73 — Recursive BOM explode with cycle guard

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Explode `parentSku` through `components` to a tree. If a sku is already on the path, emit `{ sku, cycle: true, children: [] }` and stop that branch. Unknown sku: `{ sku, missing: true, children: [] }`.

**Input:**

```json
{
  "catalog": [
    { "sku": "P", "name": "Pump", "components": ["G", "S"] },
    { "sku": "G", "name": "Gasket", "components": ["S"] },
    { "sku": "S", "name": "Screw", "components": ["P"] }
  ],
  "parentSku": "P"
}
```

**Expected (shape):** Pump → Gasket → Screw → **cycle back to P**; Pump → Screw → cycle to P.

**Interview talking point:** Multi-level BOM **must** carry a visited path. Production graphs (items, parties, categories) are not trees.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
