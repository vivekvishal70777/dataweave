%dw 2.0
output application/json
---
{
  active: ["y", "yes", "true"] contains lower(payload.active)
}
