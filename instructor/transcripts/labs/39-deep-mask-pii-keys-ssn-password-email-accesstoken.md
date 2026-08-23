# LAB 39 — Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`)

| Field | Value |
| --- | --- |
| Level | hard |
| Student folder | `student/labs/03-advanced/39-deep-mask-pii-keys-ssn-password-email-accesstoken/` |
| Solution | `instructor/solutions/03-advanced/39-deep-mask-pii-keys-ssn-password-email-accesstoken/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-39-deep-mask-pii-keys-ssn-password-email-accesstoken.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 39. Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`). Replace those keys with `"

Mask email, ssn, password, and accessToken at every depth before you log.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "name": "Asha Rao",
  "email": "asha@acme.com",
  "address": { "ssn": "AAAAA1234A", "city": "Pune" },
  "auth": { "accessToken": "00Dxx...", "password": "x" }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 39 — Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`)**
> Folder: `student/labs/03-advanced/39-deep-mask-pii-keys-ssn-password-email-accesstoken/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-39-deep-mask-pii-keys-ssn-password-email-accesstoken-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var hidden = ["ssn", "password", "email", "accesstoken"]
fun mask(x) =
  x match {
    case o is Object -> o mapObject ((v, k) -> {
      (k): if (hidden contains lower(k as String)) "****" else mask(v)
    })
    case a is Array -> a map mask($)
    else -> x
  }
---
mask(payload)
```

**SAY:** That should match Expected:

secret fields `"****"`, `name` and `city` unchanged.

## Part 4 — Interview phrase and close

**SAY:**

Mask email, ssn, password, and accessToken at every depth before you log.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 40 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 39

Deep mask PII keys (`ssn`, `password`, `email`, `accessToken`)

## Expected (note)

secret fields `"****"`, `name` and `city` unchanged.

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
