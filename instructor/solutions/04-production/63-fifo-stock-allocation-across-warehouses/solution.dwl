%dw 2.0
output application/json
var ordered = payload.warehouses orderBy ((w) -> w.priority)
var plan = ordered reduce ((w, acc = { left: payload.need as Number, rows: [] }) -> do {
  var take = if (acc.left < w.qty) acc.left else w.qty
  var row = if (take > 0) [{ warehouseId: w.id, qty: take }] else []
  ---
  { left: acc.left - take, rows: acc.rows ++ row }
})
---
{
  allocations: plan.rows,
  shortfall: plan.left
}
