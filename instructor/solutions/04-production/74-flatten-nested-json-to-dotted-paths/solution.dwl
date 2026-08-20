%dw 2.0
output application/json
fun joinPath(prefix, key) =
  if (prefix == "") key else prefix ++ "." ++ key
fun flatten(x, prefix) =
  x match {
    case o is Object ->
      o pluck ((v, k) -> flatten(v, joinPath(prefix, k as String)))
        reduce ((part, acc = {}) -> acc ++ part)
    case a is Array ->
      a map ((item, idx) -> flatten(item, joinPath(prefix, idx as String)))
        reduce ((part, acc = {}) -> acc ++ part)
    else -> { (prefix): x }
  }
---
flatten(payload, "")
