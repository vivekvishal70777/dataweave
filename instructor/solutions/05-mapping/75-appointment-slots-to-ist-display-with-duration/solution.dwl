%dw 2.0
output application/json
var s = payload.start as DateTime
var e = payload.end as DateTime
---
{
  id: payload.id,
  startIst: (s >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  endIst: (e >> "Asia/Kolkata") as String {format: "dd-MMM-yyyy HH:mm"},
  durationMinutes: ((e as Number) - (s as Number)) / 60000
}
