%dw 2.0
output application/json
---
{
  allOrNone: false,
  records: payload.accounts
    filter ((a) -> !isEmpty(a.name default ""))
    map (a) -> {
      attributes: { "type": "Account" },
      Name: a.name,
      "ExternalId__c": a.sourceId
    }
}
