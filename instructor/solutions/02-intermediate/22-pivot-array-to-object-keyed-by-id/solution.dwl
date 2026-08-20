%dw 2.0
output application/json
---
payload reduce ((item, acc = {}) -> acc ++ { (item.id): item.name })
