%dw 2.0
output application/json
---
{
  name: payload.name,
  email: payload.email default "na@example.com"
}
