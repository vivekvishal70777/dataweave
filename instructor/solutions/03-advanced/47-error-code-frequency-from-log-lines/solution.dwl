%dw 2.0
output application/json
var words = lower(payload) splitBy /[^a-z0-9]+/
---
(words filter !isEmpty($))
  groupBy $
  mapObject ((v, k) -> { (k): sizeOf(v) })
