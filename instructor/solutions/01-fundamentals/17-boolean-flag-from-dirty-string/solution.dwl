%dw 2.0
output application/json
---
{
  active: ["y", "yes", "true", "1"] contains lower(payload.active as String)
}
