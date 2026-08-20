%dw 2.0
output application/json
fun businessDate(utc, offsetHours) = do {
  var dt = utc as DateTime
  var period = ("PT" ++ (offsetHours as String) ++ "H") as Period
  ---
  (dt + period) as String {format: "yyyy-MM-dd"}
}
---
payload.events map {
  id: $.id,
  utc: $.utc,
  businessDate: businessDate($.utc, payload.offsetHours)
}
