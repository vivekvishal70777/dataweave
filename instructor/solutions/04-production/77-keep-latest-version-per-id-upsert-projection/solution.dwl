%dw 2.0
output application/json
---
valuesOf(
  payload reduce ((e, acc = {}) -> do {
    var cur = acc[e.id]
    ---
    if (cur == null or (e.version as Number) >= (cur.version as Number))
      acc ++ { (e.id): e }
    else acc
  })
)
