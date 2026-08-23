%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var byId = payload.customers groupBy $.id
---
payload.charges.data map (c) -> {
  chargeId: c.id,
  email: (byId[c.customer][0].email) default "unknown",
  amount: money((c.amount as Number) / 100),
  paid: c.paid
}
