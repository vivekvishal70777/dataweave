%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
fun apply(bal, e) =
  e.type match {
    case "credit" -> bal + (e.amt as Number)
    case "debit" -> bal - (e.amt as Number)
    case "hold" -> bal - (e.amt as Number)
    else -> bal
  }
---
{
  lastEvent: payload.events[-1].id,
  balance: money(payload.events reduce ((e, acc = 0) -> apply(acc, e)))
}
