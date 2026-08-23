# Instructor solution — Lab 59

Salesforce Account composite to nested customer API

## Expected

```
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

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
