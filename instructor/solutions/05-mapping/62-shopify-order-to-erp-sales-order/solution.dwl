%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
{
  erpOrderId: payload.id as String,
  currency: payload.currency,
  channel: "WEB",
  soldTo: (payload.shipping_address.last_name default "") ++ " " ++ (payload.shipping_address.first_name default ""),
  lines: payload.line_items
    filter ((l) -> l.sku != "GIFT")
    map { sku: $.sku, qty: $.quantity as Number, unitPrice: money($.price as Number) }
}
