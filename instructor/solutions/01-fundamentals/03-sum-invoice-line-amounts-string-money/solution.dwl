%dw 2.0
output application/json
---
sum(payload.amount map ($ as Number))
