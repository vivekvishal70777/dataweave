# Instructor solution — Lab 76

Salesforce-style composite upsert records

## Expected

```
{
  "allOrNone": false,
  "records": [
    { "attributes": { "type": "Account" }, "Name": "Acme", "ExternalId__c": "E-1" },
    { "attributes": { "type": "Account" }, "Name": "Globex", "ExternalId__c": "E-3" }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
