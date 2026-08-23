%dw 2.0
output application/json
---
valuesOf(
  payload reduce ((item, acc = {}) -> acc ++ { (item.email): item })
)
