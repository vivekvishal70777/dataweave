%dw 2.0
output application/json
var cis = payload.cmdb groupBy $.sys_id
fun sev(p) = if ((p as Number) <= 2) (p as Number) else 3
---
payload.incidents map {
  ticket: $.number,
  ciName: (cis[$.cmdb_ci][0].name) default "UNASSIGNED",
  sev: sev($.priority),
  openedAt: $.opened_at
}
