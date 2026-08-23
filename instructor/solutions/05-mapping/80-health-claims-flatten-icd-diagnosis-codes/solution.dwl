%dw 2.0
output application/json
---
payload.claims
  flatMap ((c) ->
    (c.dx default [])
      filter ((code) -> !isEmpty(code))
      map { claimId: c.claimId, member: c.member, icd: $ }
  )
