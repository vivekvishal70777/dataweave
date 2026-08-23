# LAB 69 — EDI-like PO JSON to procurement canonical

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/69-edi-like-po-json-to-procurement-canonical/` |
| Solution | `instructor/solutions/05-mapping/69-edi-like-po-json-to-procurement-canonical/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-69-edi-like-po-json-to-procurement-canonical.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 69. EDI-like PO JSON to procurement canonical. Header po/vendor. Skip qty 0. needBy from yyyyMMdd to yyyy-MM-dd.

EDI PO1 skip qty 0. Date yyyyMMdd to yyyy-MM-dd.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
{
  "BEG": { "po": "PO-77", "vendor": "V-9" },
  "PO1": [
    { "sku": "BOLT", "qty": "10", "aaa": "20260820" },
    { "sku": "NUT", "qty": "0", "aaa": "20260821" }
  ]
}
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 69 — EDI-like PO JSON to procurement canonical**
> Folder: `student/labs/05-mapping/69-edi-like-po-json-to-procurement-canonical/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-69-edi-like-po-json-to-procurement-canonical-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
{
  poNum: payload.BEG.po,
  vendor: payload.BEG.vendor,
  lines: payload.PO1
    filter ((l) -> (l.qty as Number) > 0)
    map {
      sku: $.sku,
      qty: $.qty as Number,
      needBy: ($.aaa as Date {format: "yyyyMMdd"}) as String {format: "yyyy-MM-dd"}
    }
}
```

**SAY:** That should match Expected:

```
{
  "poNum": "PO-77",
  "vendor": "V-9",
  "lines": [
    { "sku": "BOLT", "qty": 10, "needBy": "2026-08-20" }
  ]
}
```

## Part 4 — Interview phrase and close

**SAY:**

EDI PO1 skip qty 0. Date yyyyMMdd to yyyy-MM-dd.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 70 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 69

EDI-like PO JSON to procurement canonical

## Expected

```
{
  "poNum": "PO-77",
  "vendor": "V-9",
  "lines": [
    { "sku": "BOLT", "qty": 10, "needBy": "2026-08-20" }
  ]
}
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
