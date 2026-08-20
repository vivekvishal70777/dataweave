%dw 2.0
output application/json
---
payload filter ((o) -> o.status == "PAID")
