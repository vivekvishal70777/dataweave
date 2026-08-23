# LAB 87 — Multi-tenant config overlay (deep-ish merge)

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/87-multi-tenant-config-overlay-deep-ish-merge/` |
| Solution | `instructor/solutions/05-mapping/87-multi-tenant-config-overlay-deep-ish-merge/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-87-multi-tenant-config-overlay-deep-ish-merge.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 87. Multi-tenant config overlay (deep-ish merge). Start from base. Overlay tenant object with ++ (right wins). Concat arrays for `plugins` only if both are arrays — interview: document ++ is shallow. Here: merge plugins with distinctBy.

Shallow plus-plus then rebuild plugins with distinctBy concat.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "base": { "timeout": 30, "plugins": ["auth"], "theme": "light" },
  "tenant": { "timeout": 10, "plugins": ["audit"], "region": "IN" }
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 87 — Multi-tenant config overlay (deep-ish merge)**
> Folder: `student/labs/05-mapping/87-multi-tenant-config-overlay-deep-ish-merge/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-87-multi-tenant-config-overlay-deep-ish-merge-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var b = payload.base
var t = payload.tenant
---
(b ++ t) ++ {
  plugins: ((b.plugins default []) ++ (t.plugins default [])) distinctBy $
}
```

**SAY:** That should match Expected:

```
{
  "timeout": 10,
  "plugins": ["auth", "audit"],
  "theme": "light",
  "region": "IN"
}
```

## Part 4 — Interview phrase and close

**SAY:**

Shallow plus-plus then rebuild plugins with distinctBy concat.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 88 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 87

Multi-tenant config overlay (deep-ish merge)

## Expected

```
{
  "timeout": 10,
  "plugins": ["auth", "audit"],
  "theme": "light",
  "region": "IN"
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
