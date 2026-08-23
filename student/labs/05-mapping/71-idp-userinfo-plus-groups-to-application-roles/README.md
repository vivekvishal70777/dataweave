# Lab 71 — IdP userinfo plus groups to application roles

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Map groups to roles via table. Unique sorted roles. admin group → role ADMIN plus USER.

**Input:**

```json
{
  "roleMap": [
    { "group": "finance", "role": "FIN_READ" },
    { "group": "admin", "role": "ADMIN" },
    { "group": "admin", "role": "USER" }
  ],
  "user": { "sub": "u1", "email": "x@y.com", "groups": ["finance", "admin", "unknown"] }
}
```

**Expected:**

```json
{
  "userId": "u1",
  "email": "x@y.com",
  "roles": ["ADMIN", "FIN_READ", "USER"]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
