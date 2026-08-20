%dw 2.0
output application/json
---
payload map {
  fullName: $.firstName ++ " " ++ $.lastName,
  dept: $.department
}
