%dw 2.0
output application/json
---
(payload.occurredAt as DateTime) as String {format: "dd-MMM-yyyy"}
