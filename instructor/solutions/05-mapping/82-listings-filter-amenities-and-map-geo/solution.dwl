%dw 2.0
output application/json
---
payload
  filter ((l) -> (l.amenities map lower($)) contains "parking")
  map { id: $.id, lat: $.geo.lat, lng: $.geo.lng, price: $.price as Number }
