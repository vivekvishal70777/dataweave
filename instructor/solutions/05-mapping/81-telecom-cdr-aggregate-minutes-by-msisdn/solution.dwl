%dw 2.0
output application/json
---
payload
  filter ((c) -> lower(c.status) == "ok")
  groupBy $.msisdn
  pluck ((rows, m) -> {
    msisdn: m,
    minutes: floor(sum(rows.durationSec) / 60)
  })
