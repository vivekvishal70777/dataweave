# Lab 59 — Salesforce Account composite to nested customer API

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Join `contacts` onto `accounts` by AccountId. Output `accountId`, `name`, `city`, and `contacts[]` with `fullName` and `email`. Empty contact list if none. Do not call lookup.

**Input:**

```json
{
  "accounts": [
    { "Id": "001xxA", "Name": "Acme Pvt", "BillingCity": "Pune" },
    { "Id": "001xxB", "Name": "Globex", "BillingCity": "Mumbai" }
  ],
  "contacts": [
    { "AccountId": "001xxA", "FirstName": "Asha", "LastName": "Rao", "Email": "asha@acme.com" },
    { "AccountId": "001xxA", "FirstName": "Ben", "LastName": "Cole", "Email": "ben@acme.com" }
  ]
}
```

**Expected:**

```json
[
  {
    "accountId": "001xxA",
    "name": "Acme Pvt",
    "city": "Pune",
    "contacts": [
      { "fullName": "Asha Rao", "email": "asha@acme.com" },
      { "fullName": "Ben Cole", "email": "ben@acme.com" }
    ]
  },
  {
    "accountId": "001xxB",
    "name": "Globex",
    "city": "Mumbai",
    "contacts": []
  }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
