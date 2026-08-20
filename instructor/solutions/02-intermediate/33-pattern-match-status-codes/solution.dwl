%dw 2.0
output application/json
---
payload.code match {
  case n if n >= 200 and n < 300 -> "ok"
  case n if n >= 400 and n < 500 -> "client"
  case n if n >= 500 and n < 600 -> "server"
  else -> "other"
}
