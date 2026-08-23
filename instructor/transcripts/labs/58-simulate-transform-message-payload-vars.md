# LAB 58 — Simulate Transform Message payload + vars

| Field | Value |
| --- | --- |
| Level | industry |
| Student folder | `student/labs/04-industry/58-simulate-transform-message-payload-vars/` |
| Solution | `instructor/solutions/04-industry/58-simulate-transform-message-payload-vars/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-58-simulate-transform-message-payload-vars.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 58. Simulate Transform Message payload + vars. One script returns

One script, two targets: canonical payload plus vars.correlationId. Playground cannot set Mule vars.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "headers": { "xCorrelationId": "corr-9" },
  "order": { "id": "O-1", "amount": "42.00" }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 58 — Simulate Transform Message payload + vars**
> Folder: `student/labs/04-industry/58-simulate-transform-message-payload-vars/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-58-simulate-transform-message-payload-vars-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var canonical = {
  orderId: payload.order.id,
  amount: payload.order.amount as Number
}
---
{
  payload: canonical,
  vars: {
    correlationId: payload.headers.xCorrelationId default "missing",
    recordCount: 1
  }
}
```

**SAY:** That should match Expected:

```
{
  "payload": { "orderId": "O-1", "amount": 42.00 },
  "vars": { "correlationId": "corr-9", "recordCount": 1 }
}
```

## Part 4 — Interview phrase and close

**SAY:**

One script, two targets: canonical payload plus vars.correlationId. Playground cannot set Mule vars.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 59 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 58

Simulate Transform Message payload + vars

## Expected

```
{
  "payload": { "orderId": "O-1", "amount": 42.00 },
  "vars": { "correlationId": "corr-9", "recordCount": 1 }
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
