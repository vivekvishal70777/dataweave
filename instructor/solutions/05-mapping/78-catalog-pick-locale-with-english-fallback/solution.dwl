%dw 2.0
output application/json
var loc = payload.locale
---
payload.products map {
  id: $.id,
  title: ($.name[loc]) default $.name.en
}
