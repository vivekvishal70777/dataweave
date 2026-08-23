%dw 2.0
output application/json
fun money(n: Number) = n as String {format: "0.00"} as Number
---
payload map {
  rma: $.rma,
  restock: upper($.reason) != "DAMAGED",
  refund: money(($.qty as Number) * ($.unit as Number))
}
