%dw 2.0
output application/xml
---
users: {
  user: payload map {
    id: $.id,
    name: $.name
  }
}
