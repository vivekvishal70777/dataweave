%dw 2.0
output application/json
---
payload reduce ((n, acc = []) -> acc ++ [(acc[-1] default 0) + n])
