%dw 2.0
output application/json
fun mapLeaves(x) =
  x match {
    case s is String -> upper(s)
    case a is Array -> a map mapLeaves($)
    case o is Object -> o mapObject ((v, k) -> { (k): mapLeaves(v) })
    else -> x
  }
---
mapLeaves(payload)
