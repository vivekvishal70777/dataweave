%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
var intra = payload.shipFromState == payload.shipToState
var raw = payload.lines filter ((l) -> (l.qty as Number) > 0) map (l) -> do {
  var qty = l.qty as Number
  var price = l.netpr as Number
  var disc = (l.disc default 0) as Number
  ---
  { sku: l.matnr, qty: qty, net: money(qty * price * (1 - disc)) }
}
var sub = money(sum(raw.net))
var tax = money(sub * 0.18)
---
{
  invoiceId: payload.vbeln,
  currency: payload.waerk,
  taxCode: if (intra) "CGST_SGST" else "IGST",
  lines: raw,
  subtotal: sub,
  tax: tax,
  grandTotal: money(sub + tax)
}
