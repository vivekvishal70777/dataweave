%dw 2.0
output application/json
---
payload filter ((o) ->
  (["paid", "settled"] contains lower(o.status as String))
  and ((o.amount as Number) > 0)
)
