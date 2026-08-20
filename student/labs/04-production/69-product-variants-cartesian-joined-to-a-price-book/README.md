# Lab 69 — Product variants cartesian-joined to a price book

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** For each **active** product, cartesian `colors` × `sizes`. Join `prices` by `sku` where `sku` = `productId + "-" + color + "-" + size`. Skip combos with no price.

**Input:**

```json
{
  "products": [
    {
      "id": "TEE",
      "active": true,
      "colors": ["R", "G"],
      "sizes": ["S", "M"]
    },
    {
      "id": "HAT",
      "active": false,
      "colors": ["B"],
      "sizes": ["L"]
    }
  ],
  "prices": [
    { "sku": "TEE-R-S", "price": 10 },
    { "sku": "TEE-R-M", "price": 12 },
    { "sku": "TEE-G-S", "price": 11 }
  ]
}
```

**Expected:**

```json
[
  { "sku": "TEE-R-S", "productId": "TEE", "color": "R", "size": "S", "price": 10 },
  { "sku": "TEE-R-M", "productId": "TEE", "color": "R", "size": "M", "price": 12 },
  { "sku": "TEE-G-S", "productId": "TEE", "color": "G", "size": "S", "price": 11 }
]
```

**Interview talking point:** Cartesian product is `flatMap` + `map`. Index prices with `groupBy` **once**. Inactive products must not leak SKUs.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
