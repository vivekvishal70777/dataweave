# Lab 78 — Catalog copy with locale fallback

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Resolve `hi` and `bye` for `locale`, then `fallback`. Missing key → `null` (do not fail).

**Input:**

```json
{
  "locale": "de",
  "fallback": "en",
  "copy": {
    "en": { "hi": "Hello", "bye": "Bye" },
    "fr": { "hi": "Bonjour" }
  }
}
```

**Expected:**

```json
{
  "locale": "de",
  "hi": "Hello",
  "bye": "Bye"
}
```

**Interview talking point:** Storefront and notification templates always need **fallback chains**. Same pattern as MDM field precedence (Lab 56).

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
