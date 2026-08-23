# LAB 84 — Payment recon: bank UTR vs gateway charges

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/84-payment-recon-bank-utr-vs-gateway-charges/` |
| Solution | `instructor/solutions/05-mapping/84-payment-recon-bank-utr-vs-gateway-charges/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-84-payment-recon-bank-utr-vs-gateway-charges.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 84. Payment recon: bank UTR vs gateway charges. Match on utr. Status MATCHED if amounts equal (as Number), AMOUNT_MISMATCH if both exist else UNMATCHED. Include both sides.

Union of UTR keys. MATCHED only if both amounts equal.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "bank": [
    { "utr": "U1", "amt": "100.00" },
    { "utr": "U2", "amt": "40" }
  ],
  "gateway": [
    { "utr": "U1", "amt": 100 },
    { "utr": "U3", "amt": 9 }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 84 — Payment recon: bank UTR vs gateway charges**
> Folder: `student/labs/05-mapping/84-payment-recon-bank-utr-vs-gateway-charges/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-84-payment-recon-bank-utr-vs-gateway-charges-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
fun money(n) = if (n == null) null else (n as Number) as String {format: "0.00"} as Number
var b = payload.bank groupBy $.utr
var g = payload.gateway groupBy $.utr
var keys = (namesOf(b) ++ namesOf(g)) distinctBy $
---
keys map (k) -> do {
  var bv = b[k][0].amt default null
  var gv = g[k][0].amt default null
  ---
  {
    utr: k,
    status: if (bv != null and gv != null)
              if ((bv as Number) == (gv as Number)) "MATCHED" else "AMOUNT_MISMATCH"
            else "UNMATCHED",
    bank: money(bv),
    gateway: money(gv)
  }
}
```

**SAY:** That should match Expected:

```
[
  { "utr": "U1", "status": "MATCHED", "bank": 100.00, "gateway": 100.00 },
  { "utr": "U2", "status": "UNMATCHED", "bank": 40.00, "gateway": null },
  { "utr": "U3", "status": "UNMATCHED", "bank": null, "gateway": 9.00 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

Union of UTR keys. MATCHED only if both amounts equal.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 85 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 84

Payment recon: bank UTR vs gateway charges

## Expected

```
[
  { "utr": "U1", "status": "MATCHED", "bank": 100.00, "gateway": 100.00 },
  { "utr": "U2", "status": "UNMATCHED", "bank": 40.00, "gateway": null },
  { "utr": "U3", "status": "UNMATCHED", "bank": null, "gateway": 9.00 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
