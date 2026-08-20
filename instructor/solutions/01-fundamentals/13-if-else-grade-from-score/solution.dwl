%dw 2.0
output application/json
---
if (payload.score >= 90) "A"
else if (payload.score >= 75) "B"
else if (payload.score >= 50) "C"
else "F"
