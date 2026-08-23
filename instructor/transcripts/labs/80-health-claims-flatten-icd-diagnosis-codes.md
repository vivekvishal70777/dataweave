# LAB 80 — Health claims flatten ICD diagnosis codes

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/80-health-claims-flatten-icd-diagnosis-codes/` |
| Solution | `instructor/solutions/05-mapping/80-health-claims-flatten-icd-diagnosis-codes/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-80-health-claims-flatten-icd-diagnosis-codes.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 80. Health claims flatten ICD diagnosis codes. One output row per diagnosis. Copy claimId and member. Skip empty codes.

flatMap diagnoses. Skip empty ICD codes.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "claims": [
    { "claimId": "CL-1", "member": "M9", "dx": ["E11.9", "I10"] },
    { "claimId": "CL-2", "member": "M9", "dx": [""] }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 80 — Health claims flatten ICD diagnosis codes**
> Folder: `student/labs/05-mapping/80-health-claims-flatten-icd-diagnosis-codes/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-80-health-claims-flatten-icd-diagnosis-codes-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.claims
  flatMap ((c) ->
    (c.dx default [])
      filter ((code) -> !isEmpty(code))
      map { claimId: c.claimId, member: c.member, icd: $ }
  )
```

**SAY:** That should match Expected:

```
[
  { "claimId": "CL-1", "member": "M9", "icd": "E11.9" },
  { "claimId": "CL-1", "member": "M9", "icd": "I10" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

flatMap diagnoses. Skip empty ICD codes.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 81 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 80

Health claims flatten ICD diagnosis codes

## Expected

```
[
  { "claimId": "CL-1", "member": "M9", "icd": "E11.9" },
  { "claimId": "CL-1", "member": "M9", "icd": "I10" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
