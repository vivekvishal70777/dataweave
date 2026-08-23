%dw 2.0
output application/json
fun money(n) = if (n == null) null else (n as Number) as String {format: "0.00"} as Number
var b = payload.bank groupBy $.utr
var g = payload.gateway groupBy $.utr
var keys = (namesOf(b) ++ namesOf(g)) distinctBy $
---
keys map (k) -> do {
  var bv = b[k][0].amt default null
  var gv = g[k][0].amt default null
  ---
  {
    utr: k,
    status: if (bv != null and gv != null)
              if ((bv as Number) == (gv as Number)) "MATCHED" else "AMOUNT_MISMATCH"
            else "UNMATCHED",
    bank: money(bv),
    gateway: money(gv)
  }
}
