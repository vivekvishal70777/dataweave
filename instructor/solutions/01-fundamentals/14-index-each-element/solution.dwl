%dw 2.0
output application/json
---
payload map {
  index: $$ + 1,
  value: $
}
