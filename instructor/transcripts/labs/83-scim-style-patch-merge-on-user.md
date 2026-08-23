# LAB 83 — SCIM-style patch merge on user

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/83-scim-style-patch-merge-on-user/` |
| Solution | `instructor/solutions/05-mapping/83-scim-style-patch-merge-on-user/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-83-scim-style-patch-merge-on-user.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 83. SCIM-style patch merge on user. Apply replace email and add phone. Reduce over ops starting from user.

Reduce patch ops. replace email, add phone with plus-plus.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "user": { "id": "U1", "email": "old@x.com", "phones": ["111"] },
  "ops": [
    { "op": "replace", "path": "email", "value": "new@x.com" },
    { "op": "add", "path": "phones", "value": "222" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 83 — SCIM-style patch merge on user**
> Folder: `student/labs/05-mapping/83-scim-style-patch-merge-on-user/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-83-scim-style-patch-merge-on-user-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.ops reduce ((op, acc = payload.user) ->
  if (op.op == "replace" and op.path == "email")
    acc ++ { email: op.value }
  else if (op.op == "add" and op.path == "phones")
    acc ++ { phones: (acc.phones default []) ++ [op.value] }
  else acc
)
```

**SAY:** That should match Expected:

```
{
  "id": "U1",
  "email": "new@x.com",
  "phones": ["111", "222"]
}
```

## Part 4 — Interview phrase and close

**SAY:**

Reduce patch ops. replace email, add phone with plus-plus.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 84 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 83

SCIM-style patch merge on user

## Expected

```
{
  "id": "U1",
  "email": "new@x.com",
  "phones": ["111", "222"]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
