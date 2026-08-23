%dw 2.0
output application/json
---
payload.ops reduce ((op, acc = payload.user) ->
  if (op.op == "replace" and op.path == "email")
    acc ++ { email: op.value }
  else if (op.op == "add" and op.path == "phones")
    acc ++ { phones: (acc.phones default []) ++ [op.value] }
  else acc
)
