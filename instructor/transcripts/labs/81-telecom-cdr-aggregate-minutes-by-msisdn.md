# LAB 81 — Telecom CDR aggregate minutes by MSISDN

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/81-telecom-cdr-aggregate-minutes-by-msisdn/` |
| Solution | `instructor/solutions/05-mapping/81-telecom-cdr-aggregate-minutes-by-msisdn/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-81-telecom-cdr-aggregate-minutes-by-msisdn.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 81. Telecom CDR aggregate minutes by MSISDN. Sum durationSec/60 floor per msisdn. Drop failed calls (status != OK).

OK calls only. floor sum seconds over 60 per msisdn.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "msisdn": "91A", "durationSec": 90, "status": "OK" },
  { "msisdn": "91A", "durationSec": 30, "status": "FAIL" },
  { "msisdn": "91B", "durationSec": 120, "status": "ok" }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 81 — Telecom CDR aggregate minutes by MSISDN**
> Folder: `student/labs/05-mapping/81-telecom-cdr-aggregate-minutes-by-msisdn/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-81-telecom-cdr-aggregate-minutes-by-msisdn-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((c) -> lower(c.status) == "ok")
  groupBy $.msisdn
  pluck ((rows, m) -> {
    msisdn: m,
    minutes: floor(sum(rows.durationSec) / 60)
  })
```

**SAY:** That should match Expected:

```
[
  { "msisdn": "91A", "minutes": 1 },
  { "msisdn": "91B", "minutes": 2 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

OK calls only. floor sum seconds over 60 per msisdn.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 82 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 81

Telecom CDR aggregate minutes by MSISDN

## Expected

```
[
  { "msisdn": "91A", "minutes": 1 },
  { "msisdn": "91B", "minutes": 2 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
