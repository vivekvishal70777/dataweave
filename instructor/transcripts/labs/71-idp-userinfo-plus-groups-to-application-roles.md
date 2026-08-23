# LAB 71 — IdP userinfo plus groups to application roles

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/71-idp-userinfo-plus-groups-to-application-roles/` |
| Solution | `instructor/solutions/05-mapping/71-idp-userinfo-plus-groups-to-application-roles/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-71-idp-userinfo-plus-groups-to-application-roles.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 71. IdP userinfo plus groups to application roles. Map groups to roles via table. Unique sorted roles. admin group → role ADMIN plus USER.

flatMap groups to roles. distinctBy then orderBy.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "roleMap": [
    { "group": "finance", "role": "FIN_READ" },
    { "group": "admin", "role": "ADMIN" },
    { "group": "admin", "role": "USER" }
  ],
  "user": { "sub": "u1", "email": "x@y.com", "groups": ["finance", "admin", "unknown"] }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 71 — IdP userinfo plus groups to application roles**
> Folder: `student/labs/05-mapping/71-idp-userinfo-plus-groups-to-application-roles/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-71-idp-userinfo-plus-groups-to-application-roles-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var byG = payload.roleMap groupBy $.group
---
{
  userId: payload.user.sub,
  email: payload.user.email,
  roles: (
    payload.user.groups
      flatMap ((g) -> (byG[g] default []) map $.role)
      distinctBy $
      orderBy $
  )
}
```

**SAY:** That should match Expected:

```
{
  "userId": "u1",
  "email": "x@y.com",
  "roles": ["ADMIN", "FIN_READ", "USER"]
}
```

## Part 4 — Interview phrase and close

**SAY:**

flatMap groups to roles. distinctBy then orderBy.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 72 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 71

IdP userinfo plus groups to application roles

## Expected

```
{
  "userId": "u1",
  "email": "x@y.com",
  "roles": ["ADMIN", "FIN_READ", "USER"]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
