%dw 2.0
output application/json
---
payload reduce ((p, acc = {}) -> acc ++ { (p.k): p.v })
