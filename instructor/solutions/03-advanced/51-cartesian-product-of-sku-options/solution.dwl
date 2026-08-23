%dw 2.0
output application/json
---
payload.colors flatMap ((c) ->
  payload.sizes map (s) -> { color: c, size: s }
)
