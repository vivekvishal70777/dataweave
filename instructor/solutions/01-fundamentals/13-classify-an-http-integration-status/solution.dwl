%dw 2.0
output application/json
var s = payload.httpStatus as Number
---
if ([408, 429] contains s) "retry"
else if (s >= 500 and s < 600) "retry"
else if (s >= 200 and s < 300) "ok"
else if (s >= 400 and s < 500) "client"
else "other"
