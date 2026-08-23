%dw 2.0
output application/csv header=true
---
payload map {
  orderId: $.orderId,
  customerId: $.customerId,
  amount: $.amount
}
