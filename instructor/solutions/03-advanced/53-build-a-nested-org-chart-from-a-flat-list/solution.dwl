%dw 2.0
output application/json
var byMgr = payload groupBy ((e) -> e.managerId default "ROOT")
fun node(e) = {
  id: e.id,
  name: e.name,
  children: (byMgr[e.id] default []) map node($)
}
---
(byMgr["ROOT"] default []) map node($)
