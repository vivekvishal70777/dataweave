# LAB 65 — Debezium CDC envelope to flat upsert rows

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/65-debezium-cdc-envelope-to-flat-upsert-rows/` |
| Solution | `instructor/solutions/05-mapping/65-debezium-cdc-envelope-to-flat-upsert-rows/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-65-debezium-cdc-envelope-to-flat-upsert-rows.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 65. Debezium CDC envelope to flat upsert rows. c/u → UPSERT from after; d → DELETE from before. Include tsMs.

CDC: delete reads before. create and update read after. ts_ms on every row.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "changes": [
    { "op": "c", "ts_ms": 100, "before": null, "after": { "id": "A1", "status": "NEW" } },
    { "op": "u", "ts_ms": 101, "before": { "id": "A1", "status": "NEW" }, "after": { "id": "A1", "status": "PAID" } },
    { "op": "d", "ts_ms": 102, "before": { "id": "B9", "status": "X" }, "after": null }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 65 — Debezium CDC envelope to flat upsert rows**
> Folder: `student/labs/05-mapping/65-debezium-cdc-envelope-to-flat-upsert-rows/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-65-debezium-cdc-envelope-to-flat-upsert-rows-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload.changes map (c) -> do {
  var row = if (c.op == "d") c.before else c.after
  ---
  {
    action: if (c.op == "d") "DELETE" else "UPSERT",
    id: row.id,
    status: row.status,
    tsMs: c.ts_ms
  }
}
```

**SAY:** That should match Expected:

```
[
  { "action": "UPSERT", "id": "A1", "status": "NEW", "tsMs": 100 },
  { "action": "UPSERT", "id": "A1", "status": "PAID", "tsMs": 101 },
  { "action": "DELETE", "id": "B9", "status": "X", "tsMs": 102 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

CDC: delete reads before. create and update read after. ts_ms on every row.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 66 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 65

Debezium CDC envelope to flat upsert rows

## Expected

```
[
  { "action": "UPSERT", "id": "A1", "status": "NEW", "tsMs": 100 },
  { "action": "UPSERT", "id": "A1", "status": "PAID", "tsMs": 101 },
  { "action": "DELETE", "id": "B9", "status": "X", "tsMs": 102 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
