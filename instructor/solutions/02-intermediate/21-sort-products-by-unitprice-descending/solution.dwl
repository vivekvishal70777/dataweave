%dw 2.0
output application/json
---
payload orderBy ((p) -> -p.unitPrice)
