%dw 2.0
output application/json
fun pick(mdm, crm, erp) = mdm default (crm default erp)
fun addrKey(a) = a.type
fun mergeAddr() = do {
  var tagged =
    (payload.erp.addresses default [] map $ ++ { _src: 0 })
      ++ (payload.crm.addresses default [] map $ ++ { _src: 1 })
      ++ (payload.mdm.addresses default [] map $ ++ { _src: 2 })
  var byType = tagged groupBy addrKey
  ---
  namesOf(byType) map (t) -> do {
    var rows = byType[t]
    var erp = (rows filter ((r) -> r._src == 0))[0]
    var crm = (rows filter ((r) -> r._src == 1))[0]
    var mdm = (rows filter ((r) -> r._src == 2))[0]
    ---
    {
      type: t as String,
      city: pick(mdm.city, crm.city, erp.city),
      line: pick(mdm.line, crm.line, erp.line)
    }
  }
}
var stacked = [payload.erp, payload.crm, payload.mdm]
---
{
  id: pick(payload.mdm.id, payload.crm.id, payload.erp.id),
  name: pick(payload.mdm.name, payload.crm.name, payload.erp.name),
  phone: pick(payload.mdm.phone, payload.crm.phone, payload.erp.phone),
  emails: (stacked.emails flatten map lower($)) distinctBy $ orderBy $,
  addresses: mergeAddr()
}
