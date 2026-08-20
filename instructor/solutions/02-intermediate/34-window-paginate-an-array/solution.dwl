%dw 2.0
import * from dw::core::Arrays
output application/json
var page = 2
var size = 2
---
payload drop ((page - 1) * size) take size
