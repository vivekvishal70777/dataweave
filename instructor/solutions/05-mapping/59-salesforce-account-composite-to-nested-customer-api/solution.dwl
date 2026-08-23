%dw 2.0
output application/json
var byAcct = payload.contacts groupBy $.AccountId
---
payload.accounts map (a) -> {
  accountId: a.Id,
  name: a.Name,
  city: a.BillingCity,
  contacts: (byAcct[a.Id] default []) map {
    fullName: ($.FirstName default "") ++ " " ++ ($.LastName default ""),
    email: $.Email
  }
}
