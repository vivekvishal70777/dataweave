%dw 2.0
output application/json
var deny = ["password", "ssn", "accesstoken"]
---
payload filterObject ((v, k) -> !(deny contains lower(k as String)))
