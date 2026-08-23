%dw 2.0
output application/json
---
payload.base ++ payload.overlay
