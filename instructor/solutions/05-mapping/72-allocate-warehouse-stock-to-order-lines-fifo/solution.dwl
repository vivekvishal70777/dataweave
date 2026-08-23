%dw 2.0
output application/json
---
payload.order reduce ((line, acc = { stock: payload.stock groupBy $.sku, out: [] }) -> do {
  var have = (acc.stock[line.sku][0].onHand default 0) as Number
  var give = min([line.qty as Number, have])
  var rest = have - give
  ---
  {
    stock: acc.stock mapObject ((v, k) ->
      if ((k as String) == line.sku) { (k): [{ sku: line.sku, onHand: rest }] }
      else { (k): v }
    ),
    out: acc.out ++ [{ sku: line.sku, requested: line.qty as Number, allocated: give }]
  }
}).out
