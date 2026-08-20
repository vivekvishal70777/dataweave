%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var items = payload.rows filter ((r) -> r.type != "TRAILER") map {
  id: $.id,
  amount: $.amount as Number
}
var trailer = payload.rows filter ((r) -> r.type == "TRAILER")[-1]
var total = money(sum(items.amount))
var expected = money(trailer.total as Number)
---
{
  items: items,
  total: total,
  expected: expected,
  balanced: total == expected
}
