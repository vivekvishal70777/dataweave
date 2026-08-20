# Instructor solution — Lab 56

Customer 360 merge with field precedence

## Expected

```
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

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
