# Lab 70 — JSON Merge Patch (RFC 7396) plus changelog

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Apply `patch` to `base`. `null` in patch **deletes** the key. Nested objects merge recursively; non-objects replace. Also return `changed` as sorted field paths that differ (`from` / `to`). Treat missing as `null`.

**Input:**

```json
{
  "base": { "name": "Asha", "age": 30, "addr": { "city": "Pune", "zip": "411" } },
  "patch": { "age": null, "addr": { "city": "Mumbai" }, "role": "eng" }
}
```

**Expected:**

```json
{
  "result": {
    "name": "Asha",
    "addr": { "city": "Mumbai", "zip": "411" },
    "role": "eng"
  },
  "changed": [
    { "path": "addr.city", "from": "Pune", "to": "Mumbai" },
    { "path": "age", "from": 30, "to": null },
    { "path": "role", "from": null, "to": "eng" }
  ]
}
```

**Interview talking point:** HTTP PATCH in APIs is often **merge-patch**, not a full PUT. Audit/changelog is a second walk (`diff`). `skipNullOn` would hide deletions — do not use it on the changelog.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
