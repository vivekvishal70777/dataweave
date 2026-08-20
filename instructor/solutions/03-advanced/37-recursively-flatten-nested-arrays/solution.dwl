%dw 2.0
output application/json
fun deepFlatten(x) =
  x match {
    case a is Array -> a flatMap deepFlatten($)
    else -> [x]
  }
---
deepFlatten(payload)
