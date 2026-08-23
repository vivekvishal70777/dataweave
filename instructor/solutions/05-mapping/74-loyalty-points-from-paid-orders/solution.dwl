%dw 2.0
output application/json
---
payload
  filter ((o) -> ["paid", "settled"] contains lower(o.status))
  groupBy $.customerId
  pluck ((rows, cid) -> {
    customerId: cid,
    points: floor(sum(rows.amount map ($ as Number)))
  })
