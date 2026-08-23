%dw 2.0
output application/json
---
{
  occurredAtIst: ((payload.occurredAt as DateTime) >> "Asia/Kolkata")
    as String {format: "dd-MMM-yyyy HH:mm"}
}
