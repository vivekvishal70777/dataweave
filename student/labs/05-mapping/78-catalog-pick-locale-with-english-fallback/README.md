# Lab 78 — Catalog pick locale with English fallback

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** For each product pick name[locale] default name.en. Drop other locales.

**Input:**

```json
{
  "locale": "hi",
  "products": [
    { "id": "P1", "name": { "en": "Shirt", "hi": "Kamiz" } },
    { "id": "P2", "name": { "en": "Hat" } }
  ]
}
```

**Expected:**

```json
[
  { "id": "P1", "title": "Kamiz" },
  { "id": "P2", "title": "Hat" }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
