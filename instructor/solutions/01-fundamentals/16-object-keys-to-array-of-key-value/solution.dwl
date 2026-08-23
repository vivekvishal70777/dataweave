%dw 2.0
output application/json
---
payload pluck ((v, k) -> { key: k as String, value: v })
