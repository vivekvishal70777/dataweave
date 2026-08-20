# Instructor solution — Lab 70

JSON Merge Patch (RFC 7396) plus changelog

## Expected

```
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

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
