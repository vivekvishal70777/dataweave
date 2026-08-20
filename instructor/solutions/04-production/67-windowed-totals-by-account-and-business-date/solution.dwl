%dw 2.0
output application/json
fun day(ts) = (ts as String)[0 to 9]
---
payload.payments
  groupBy ((p) -> p.accountId ++ "|" ++ day(p.ts))
  pluck ((rows, k) -> {
    accountId: (k splitBy "|")[0],
    date: (k splitBy "|")[1],
    total: sum(rows.amount)
  })
  orderBy ((r) -> r.accountId ++ r.date)
