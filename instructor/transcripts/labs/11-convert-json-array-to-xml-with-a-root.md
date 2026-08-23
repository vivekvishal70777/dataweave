# LAB 11 — Convert JSON array to XML with a root

| Field | Value |
| --- | --- |
| Level | easy |
| Student folder | `student/labs/01-fundamentals/11-convert-json-array-to-xml-with-a-root/` |
| Solution | `instructor/solutions/01-fundamentals/11-convert-json-array-to-xml-with-a-root/solution.dwl` |
| Target length | 6–10 min |
| File name | `LAB-11-convert-json-array-to-xml-with-a-root.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 11. Convert JSON array to XML with a root. Wrap users as XML `users/user`.

XML needs one root. Change output to application/xml and wrap the array.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[{ "id": 1, "name": "Asha" }, { "id": 2, "name": "Ben" }]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 11 — Convert JSON array to XML with a root**
> Folder: `student/labs/01-fundamentals/11-convert-json-array-to-xml-with-a-root/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-11-convert-json-array-to-xml-with-a-root-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/xml
---
users: {
  user: payload map {
    id: $.id,
    name: $.name
  }
}
```

**SAY:** That should match Expected:

```
<users>
  <user><id>1</id><name>Asha</name></user>
  <user><id>2</id><name>Ben</name></user>
</users>
```

## Part 4 — Interview phrase and close

**SAY:**

XML needs one root. Change output to application/xml and wrap the array.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 12 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 11

Convert JSON array to XML with a root

## Expected

```
<users>
  <user><id>1</id><name>Asha</name></user>
  <user><id>2</id><name>Ben</name></user>
</users>
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
