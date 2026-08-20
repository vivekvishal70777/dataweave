%dw 2.0
output application/json
var secret = ["authorization", "cookie", "x-api-key"]
---
payload.headers mapObject ((v, k) -> {
  (k): if (secret contains lower(k as String)) "****" else v
})
