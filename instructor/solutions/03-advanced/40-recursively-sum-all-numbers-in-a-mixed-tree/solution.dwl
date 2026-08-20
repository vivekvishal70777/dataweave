%dw 2.0
output application/json
fun sumNums(x) =
  x match {
    case n is Number -> n
    case a is Array -> sum(a map sumNums($))
    case o is Object -> sum(valuesOf(o) map sumNums($))
    else -> 0
  }
---
sumNums(payload)
