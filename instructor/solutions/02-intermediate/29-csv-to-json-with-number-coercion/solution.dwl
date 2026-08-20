%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number
}
