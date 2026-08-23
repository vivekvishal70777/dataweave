# LAB 59 — Salesforce Account composite to nested customer API

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/59-salesforce-account-composite-to-nested-customer-api/` |
| Solution | `instructor/solutions/05-mapping/59-salesforce-account-composite-to-nested-customer-api/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-59-salesforce-account-composite-to-nested-customer-api.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 59. Salesforce Account composite to nested customer API. Join `contacts` onto `accounts` by AccountId. Output `accountId`, `name`, `city`, and `contacts[]` with `fullName` and `email`. Empty contact list if none. Do not call lookup.

groupBy contacts by AccountId. Map accounts. Empty array if no contacts. No lookup.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

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

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 59 — Salesforce Account composite to nested customer API**
> Folder: `student/labs/05-mapping/59-salesforce-account-composite-to-nested-customer-api/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-59-salesforce-account-composite-to-nested-customer-api-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var byAcct = payload.contacts groupBy $.AccountId
---
payload.accounts map (a) -> {
  accountId: a.Id,
  name: a.Name,
  city: a.BillingCity,
  contacts: (byAcct[a.Id] default []) map {
    fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
    email: $.Email
  }
}
```

**SAY:** That should match Expected:

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

## Part 4 — Interview phrase and close

**SAY:**

groupBy contacts by AccountId. Map accounts. Empty array if no contacts. No lookup.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 60 in this file.

## Instructor notes (do not read verbatim)

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
