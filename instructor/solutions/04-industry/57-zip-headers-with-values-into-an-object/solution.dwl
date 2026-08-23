%dw 2.0
import zip from dw::core::Arrays
output application/json
---
zip(payload.headers, payload.values)
  reduce ((pair, acc = {}) -> acc ++ { (pair[0]): pair[1] })
