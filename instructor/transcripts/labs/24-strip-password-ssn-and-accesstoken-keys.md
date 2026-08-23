# LAB 24 — Strip password, ssn, and accessToken keys

| Field | Value |
| --- | --- |
| Level | moderate |
| Student folder | `student/labs/02-intermediate/24-strip-password-ssn-and-accesstoken-keys/` |
| Solution | `instructor/solutions/02-intermediate/24-strip-password-ssn-and-accesstoken-keys/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-24-strip-password-ssn-and-accesstoken-keys.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 24. Strip password, ssn, and accessToken keys. Drop secret keys from a flat object before logging. Keys compared as strings.

filterObject drops password, ssn, and accessToken. Compare lowercased keys.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "name": "Asha Rao",
  "password": "s3cret",
  "ssn": "AAAAA1234A",
  "accessToken": "00Dxx...",
  "city": "Pune"
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 24 — Strip password, ssn, and accessToken keys**
> Folder: `student/labs/02-intermediate/24-strip-password-ssn-and-accesstoken-keys/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-24-strip-password-ssn-and-accesstoken-keys-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var deny = ["password", "ssn", "accesstoken"]
---
payload filterObject ((v, k) -> !(deny contains lower(k as String)))
```

**SAY:** That should match Expected:

```
{ "name": "Asha Rao", "city": "Pune" }
```

## Part 4 — Interview phrase and close

**SAY:**

filterObject drops password, ssn, and accessToken. Compare lowercased keys.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 25 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 24

Strip password, ssn, and accessToken keys

## Expected

```
{ "name": "Asha Rao", "city": "Pune" }
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
