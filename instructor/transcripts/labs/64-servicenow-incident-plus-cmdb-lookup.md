# LAB 64 — ServiceNow incident plus CMDB lookup

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/64-servicenow-incident-plus-cmdb-lookup/` |
| Solution | `instructor/solutions/05-mapping/64-servicenow-incident-plus-cmdb-lookup/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-64-servicenow-incident-plus-cmdb-lookup.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 64. ServiceNow incident plus CMDB lookup. ciName from cmdb; missing UNASSIGNED. Priority 1-2 stay, else sev 3.

CMDB groupBy sys_id. Priority 1-2 else sev 3. Missing CI UNASSIGNED.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "cmdb": [
    { "sys_id": "ci1", "name": "sap-prd-db" }
  ],
  "incidents": [
    { "number": "INC001", "cmdb_ci": "ci1", "priority": "1", "opened_at": "2026-08-01T04:00:00Z" },
    { "number": "INC002", "cmdb_ci": "gone", "priority": "3", "opened_at": "2026-08-02T10:00:00Z" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 64 — ServiceNow incident plus CMDB lookup**
> Folder: `student/labs/05-mapping/64-servicenow-incident-plus-cmdb-lookup/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-64-servicenow-incident-plus-cmdb-lookup-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
var cis = payload.cmdb groupBy $.sys_id
fun sev(p) = if ((p as Number) <= 2) (p as Number) else 3
---
payload.incidents map {
  ticket: $.number,
  ciName: (cis[$.cmdb_ci][0].name) default "UNASSIGNED",
  sev: sev($.priority),
  openedAt: $.opened_at
}
```

**SAY:** That should match Expected:

```
[
  { "ticket": "INC001", "ciName": "sap-prd-db", "sev": 1, "openedAt": "2026-08-01T04:00:00Z" },
  { "ticket": "INC002", "ciName": "UNASSIGNED", "sev": 3, "openedAt": "2026-08-02T10:00:00Z" }
]
```

## Part 4 — Interview phrase and close

**SAY:**

CMDB groupBy sys_id. Priority 1-2 else sev 3. Missing CI UNASSIGNED.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 65 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 64

ServiceNow incident plus CMDB lookup

## Expected

```
[
  { "ticket": "INC001", "ciName": "sap-prd-db", "sev": 1, "openedAt": "2026-08-01T04:00:00Z" },
  { "ticket": "INC002", "ciName": "UNASSIGNED", "sev": 3, "openedAt": "2026-08-02T10:00:00Z" }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
