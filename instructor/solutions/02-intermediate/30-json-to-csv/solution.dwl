%dw 2.0
output application/csv header=true
---
payload map {
  id: $.id,
  name: $.name
}
