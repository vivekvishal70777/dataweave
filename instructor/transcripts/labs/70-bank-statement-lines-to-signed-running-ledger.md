# LAB 70 — Bank statement lines to signed running ledger

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/70-bank-statement-lines-to-signed-running-ledger/` |
| Solution | `instructor/solutions/05-mapping/70-bank-statement-lines-to-signed-running-ledger/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-70-bank-statement-lines-to-signed-running-ledger.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 70. Bank statement lines to signed running ledger. CR positive, DR negative. Running balance from 0. fun money.

CR plus, DR minus. reduce running balance. fun money.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "nar": "SALARY", "dc": "CR", "amt": "1000.00" },
  { "nar": "UPI", "dc": "DR", "amt": "250.5" },
  { "nar": "REV", "dc": "CR", "amt": "50" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 70 — Bank statement lines to signed running ledger**
> Folder: `student/labs/05-mapping/70-bank-statement-lines-to-signed-running-ledger/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-70-bank-statement-lines-to-signed-running-ledger-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload reduce ((row, acc = { bal: 0, out: [] }) -> do {
  var signed = if (row.dc == "DR") -(row.amt as Number) else (row.amt as Number)
  var next = acc.bal + signed
  ---
  {
    bal: next,
    out: acc.out ++ [{
      narration: row.nar,
      amount: money(signed),
      balance: money(next)
    }]
  }
}).out
```

**SAY:** That should match Expected:

```
[
  { "narration": "SALARY", "amount": 1000.00, "balance": 1000.00 },
  { "narration": "UPI", "amount": -250.50, "balance": 749.50 },
  { "narration": "REV", "amount": 50.00, "balance": 799.50 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

CR plus, DR minus. reduce running balance. fun money.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 71 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 70

Bank statement lines to signed running ledger

## Expected

```
[
  { "narration": "SALARY", "amount": 1000.00, "balance": 1000.00 },
  { "narration": "UPI", "amount": -250.50, "balance": 749.50 },
  { "narration": "REV", "amount": 50.00, "balance": 799.50 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
