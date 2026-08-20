# Lab 56 — Customer 360 merge with field precedence

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Merge `erp`, `crm`, and `mdm` profiles for one customer. Scalar field precedence: **MDM > CRM > ERP**. `emails` is a union of unique lowercase addresses. `addresses` merge by `type` (same precedence for overlapping fields).

**Production rules:** Do not let a `null` in a higher source wipe a lower source’s value. Right-hand `++` would wipe; use `default` per field.

**Input:**

```json
{
  "erp": {
    "id": "E-1",
    "name": "Acme ERP",
    "phone": "111",
    "emails": ["ERP@X.com"],
    "addresses": [{ "type": "BILL", "city": "Pune", "line": "Old" }]
  },
  "crm": {
    "id": "C-1",
    "name": "Acme CRM",
    "phone": null,
    "emails": ["crm@x.com"],
    "addresses": [{ "type": "SHIP", "city": "Mumbai" }]
  },
  "mdm": {
    "id": "M-1",
    "name": null,
    "phone": "999",
    "emails": ["mdm@x.com"],
    "addresses": [{ "type": "BILL", "city": "Pune", "line": "HQ" }]
  }
}
```

**Expected:**

```json
{
  "id": "M-1",
  "name": "Acme CRM",
  "phone": "999",
  "emails": ["crm@x.com", "erp@x.com", "mdm@x.com"],
  "addresses": [
    { "type": "BILL", "city": "Pune", "line": "HQ" },
    { "type": "SHIP", "city": "Mumbai", "line": null }
  ]
}
```

**Interview talking point:** Golden-record merges need **explicit precedence**, unique keys for collections, and null-safe coalesce — not a blind `++`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
