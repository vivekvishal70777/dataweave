# Lab 76 — Salesforce-style composite upsert records

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Map canonical accounts to a Composite-like body: `allOrNone: false`, each record has `attributes.type = "Account"`, `Name`, and `ExternalId__c` from `sourceId`. Skip rows with empty `name`.

**Input:**

```json
{
  "accounts": [
    { "sourceId": "E-1", "name": "Acme" },
    { "sourceId": "E-2", "name": "" },
    { "sourceId": "E-3", "name": "Globex" }
  ]
}
```

**Expected:**

```json
{
  "allOrNone": false,
  "records": [
    { "attributes": { "type": "Account" }, "Name": "Acme", "ExternalId__c": "E-1" },
    { "attributes": { "type": "Account" }, "Name": "Globex", "ExternalId__c": "E-3" }
  ]
}
```

**Interview talking point:** `allOrNone: false` is partial success at the SaaS API. Pair with Lab 55-style `errors[]` on the way back.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
