%dw 2.0
output application/json
---
payload.colors
  filter ((c) -> c.discontinued == false)
  flatMap ((c) ->
    payload.sizes map (sz) -> {
      sku: payload.base ++ "-" ++ c.code ++ "-" ++ sz
    }
  )
