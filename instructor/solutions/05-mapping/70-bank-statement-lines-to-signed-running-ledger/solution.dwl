%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload reduce ((row, acc = { bal: 0, out: [] }) -> do {
  var signed = if (row.dc == "DR") -(row.amt as Number) else (row.amt as Number)
  var next = acc.bal + signed
  ---
  {
    bal: next,
    out: acc.out ++ [{
      narration: row.nar,
      amount: money(signed),
      balance: money(next)
    }]
  }
}).out
