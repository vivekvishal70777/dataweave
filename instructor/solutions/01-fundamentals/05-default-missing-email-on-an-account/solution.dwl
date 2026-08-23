%dw 2.0
output application/json
---
{
  Name: payload.Name,
  Email: payload.Email default "noreply@acme.invalid"
}
