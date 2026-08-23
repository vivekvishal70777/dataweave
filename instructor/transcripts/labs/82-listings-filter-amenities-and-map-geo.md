# LAB 82 — Listings filter amenities and map geo

| Field | Value |
| --- | --- |
| Level | mapping |
| Student folder | `student/labs/05-mapping/82-listings-filter-amenities-and-map-geo/` |
| Solution | `instructor/solutions/05-mapping/82-listings-filter-amenities-and-map-geo/solution.dwl` |
| Target length | 8–12 min |
| File name | `LAB-82-listings-filter-amenities-and-map-geo.mp4` |

Do not show `solution.dwl` until after the pause card.

## Part 1 — Hook (30–60 seconds)

**ON CAMERA:** Open the student starter `transform.dwl`. Run it. Show that the output is not the expected shape.

**SAY:**

This is Lab 82. Listings filter amenities and map geo. Keep listings that contain amenity parking (any case). Output id, lat, lng, price as Number.

amenities map lower contains parking. Flatten geo.

## Part 2 — Input

**SAY:** Paste this payload. Set the MIME type to match the sample.

```json
[
  { "id": "L1", "geo": { "lat": 18.5, "lng": 73.8 }, "price": "90", "amenities": ["POOL", "Parking"] },
  { "id": "L2", "geo": { "lat": 19.0, "lng": 72.8 }, "price": "70", "amenities": ["gym"] }
]
```

## PAUSE CARD (hold 3–5 seconds)

**ON SCREEN:**

> Pause the video
> Try **Lab 82 — Listings filter amenities and map geo**
> Folder: `student/labs/05-mapping/82-listings-filter-amenities-and-map-geo/`
> Resume when you have an attempt

**SAY:** Pause now. Complete transform.dwl. Come back when you have an attempt — wrong is fine.

---

_End recording part 1 here if you split files. Start part 2 as `LAB-82-listings-filter-amenities-and-map-geo-solution.mp4`._

## Part 3 — Solution (after students return)

**SAY:** Welcome back. I will type the reference script. Follow along; do not paste blindly. Header first: percent dw two point oh, output, dash dash dash.

**TYPE:**

```dataweave
%dw 2.0
output application/json
---
payload
  filter ((l) -> (l.amenities map lower($)) contains "parking")
  map { id: $.id, lat: $.geo.lat, lng: $.geo.lng, price: $.price as Number }
```

**SAY:** That should match Expected:

```
[
  { "id": "L1", "lat": 18.5, "lng": 73.8, "price": 90 }
]
```

## Part 4 — Interview phrase and close

**SAY:**

amenities map lower contains parking. Flatten geo.

If your output differs, check plus versus plus-plus, as Number, and nulls with default. Next lab is the next numbered folder.

Stop. Do not start Lab 83 in this file.

## Instructor notes (do not read verbatim)

# Instructor solution — Lab 82

Listings filter amenities and map geo

## Expected

```
[
  { "id": "L1", "lat": 18.5, "lng": 73.8, "price": 90 }
]
```

## Teaching tip

Demo the failing starter (`payload` passthrough) first, then build the script live.
Pause the recording and ask students to pause and try before showing `solution.dwl`.
