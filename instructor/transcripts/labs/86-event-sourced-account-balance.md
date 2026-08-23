# LAB 86 — Event-sourced account balance

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/86-event-sourced-account-balance/` |
| Solution | `instructor/solutions/05-mapping/86-event-sourced-account-balance/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-86-event-sourced-account-balance.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 86. Event-sourced account balance. Apply events in order: credit add, debit subtract, hold subtract. Start 0. fun money. Final balance only plus last event id.

reduce events credit add debit and hold subtract. Last event id.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "events": [
    { "id": "e1", "type": "credit", "amt": "100" },
    { "id": "e2", "type": "debit", "amt": "30" },
    { "id": "e3", "type": "hold", "amt": "10.5" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 86 — Event-sourced account balance**
> Folder: `student/labs/05-mapping/86-event-sourced-account-balance/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-86-event-sourced-account-balance-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
fun apply(bal, e) =
  e.type match {
    case "credit" -> bal + (e.amt as Number)
    case "debit" -> bal - (e.amt as Number)
    case "hold" -> bal - (e.amt as Number)
    else -> bal
  }
---
{
  lastEvent: payload.events[-1].id,
  balance: money(payload.events reduce ((e, acc = 0) -> apply(acc, e)))
}
```

**SAY:** That should match Expected:

```
{
  "lastEvent": "e3",
  "balance": 59.50
}
```

## Part 4 — Interview phrase and close

**SAY:**

reduce events credit add debit and hold subtract. Last event id.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 87 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 86

Event-sourced account balance

## Expected

```
{
  "lastEvent": "e3",
  "balance": 59.50
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
