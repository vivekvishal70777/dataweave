%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var rates = payload.fx groupBy $.ccy
var converted = payload.lines
  filter ((l) -> rates[l.currency] != null)
  map (l) -> {
    id: l.id,
    usd: money((l.amount as Number) / (rates[l.currency][0].perUsd as Number))
  }
---
{
  lines: converted,
  totalUsd: money(sum(converted.usd))
}
