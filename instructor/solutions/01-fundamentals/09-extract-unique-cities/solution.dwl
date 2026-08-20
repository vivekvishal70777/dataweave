%dw 2.0
output application/json
---
payload.city distinctBy $ orderBy $
