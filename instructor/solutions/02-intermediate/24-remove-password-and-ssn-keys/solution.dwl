%dw 2.0
output application/json
---
payload filterObject ((v, k) -> !(["password", "ssn"] contains (k as String)))
