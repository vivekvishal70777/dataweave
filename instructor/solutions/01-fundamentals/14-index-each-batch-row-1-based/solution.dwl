%dw 2.0
output application/json
---
payload map {
  rowNum: $$ + 1,
  value: $
}
