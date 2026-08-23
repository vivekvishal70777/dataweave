%dw 2.0
output application/json
var byG = payload.roleMap groupBy $.group
---
{
  userId: payload.user.sub,
  email: payload.user.email,
  roles: (
    payload.user.groups
      flatMap ((g) -> (byG[g] default []) map $.role)
      distinctBy $
      orderBy $
  )
}
