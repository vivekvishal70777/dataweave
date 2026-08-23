%dw 2.0
import * from dw::core::Arrays
output application/json
---
{
  richest: payload maxBy ((o) -> o.amount as Number),
  firstPaid: payload firstWith ((o) -> lower(o.status as String) == "paid")
}
