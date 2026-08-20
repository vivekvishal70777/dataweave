%dw 2.0
output application/json skipNullOn="everywhere"
fun diff(a, b) =
  if (a == b) null
  else (a match {
    case ao is Object if b is Object -> do {
      var keys = (namesOf(ao) ++ namesOf(b)) distinctBy $
      var kids = keys reduce ((k, acc = {}) -> do {
        var d = diff(ao[k], b[k])
        ---
        if (d == null) acc else acc ++ { (k): d }
      })
      ---
      if (isEmpty(kids)) null else kids
    }
    else -> { from: a, to: b }
  })
---
diff(vars.old, payload)
