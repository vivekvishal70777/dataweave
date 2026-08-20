%dw 2.0
output application/json
var skus = (payload.lines.sku distinctBy $ orderBy $) joinBy ","
---
payload.customerId ++ "|" ++ payload.externalOrderId ++ "|" ++ skus
