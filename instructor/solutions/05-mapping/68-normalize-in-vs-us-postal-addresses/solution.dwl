%dw 2.0
output application/json
---
payload map (a) -> {
  country: a.country,
  line1: a.addr1,
  city: upper(a.city),
  postal: if (a.country == "IN") a.pin as String
          else (a.zip as String)[0 to 4]
}
