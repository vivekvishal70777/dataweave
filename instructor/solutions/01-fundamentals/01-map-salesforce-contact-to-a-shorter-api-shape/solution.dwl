%dw 2.0
output application/json
---
payload map {
  fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
  dept: $.Department
}
