%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var rated = payload.lines map (l) -> do {
  var rate = payload.rates[l.currency]
  ---
  l ++ {
    amountUsd: if (rate != null) money((l.amount as Number) * rate) else null,
    fxError: rate == null
  }
}
var good = rated filter !$.fxError
---
{
  lines: good map {
    sku: $.sku,
    amount: $.amount,
    currency: $.currency,
    amountUsd: $.amountUsd
  },
  totalUsd: money(sum(good.amountUsd)),
  errors: rated filter $.fxError map {
    sku: $.sku,
    reason: "missing FX rate for " ++ $.currency
  }
}
