# Lab 82 — Listings filter amenities and map geo

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Keep listings that contain amenity parking (any case). Output id, lat, lng, price as Number.

**Input:**

```json
[
  { "id": "L1", "geo": { "lat": 18.5, "lng": 73.8 }, "price": "90", "amenities": ["POOL", "Parking"] },
  { "id": "L2", "geo": { "lat": 19.0, "lng": 72.8 }, "price": "70", "amenities": ["gym"] }
]
```

**Expected:**

```json
[
  { "id": "L1", "lat": 18.5, "lng": 73.8, "price": 90 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
