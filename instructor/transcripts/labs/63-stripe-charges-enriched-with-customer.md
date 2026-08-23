# LAB 63 — Stripe charges enriched with customer

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/63-stripe-charges-enriched-with-customer/` |
| Solution | `instructor/solutions/05-mapping/63-stripe-charges-enriched-with-customer/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-63-stripe-charges-enriched-with-customer.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 63. Stripe charges enriched with customer. Join charges to customers. Amount cents/100. Missing email unknown.

Stripe cents divide 100. groupBy customer. Missing email unknown.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "customers": [
    { "id": "cus_1", "email": "a@x.com" }
  ],
  "charges": {
    "data": [
      { "id": "ch_1", "customer": "cus_1", "amount": 1999, "paid": true },
      { "id": "ch_2", "customer": "cus_missing", "amount": 500, "paid": false }
    ]
  }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 63 — Stripe charges enriched with customer**
> Folder: `student/labs/05-mapping/63-stripe-charges-enriched-with-customer/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-63-stripe-charges-enriched-with-customer-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var byId = payload.customers groupBy $.id
---
payload.charges.data map (c) -> {
  chargeId: c.id,
  email: (byId[c.customer][0].email) default "unknown",
  amount: money((c.amount as Number) / 100),
  paid: c.paid
}
```

**SAY:** That should match Expected:

```
[
  { "chargeId": "ch_1", "email": "a@x.com", "amount": 19.99, "paid": true },
  { "chargeId": "ch_2", "email": "unknown", "amount": 5.00, "paid": false }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Stripe cents divide 100. groupBy customer. Missing email unknown.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 64 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 63

Stripe charges enriched with customer

## Expected

```
[
  { "chargeId": "ch_1", "email": "a@x.com", "amount": 19.99, "paid": true },
  { "chargeId": "ch_2", "email": "unknown", "amount": 5.00, "paid": false }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
