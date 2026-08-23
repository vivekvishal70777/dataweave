%dw 2.0
output application/json
---
payload mapObject ((v, k) -> {
  (k): v match {
    case s is String -> upper(s)
    else -> v
  }
})
