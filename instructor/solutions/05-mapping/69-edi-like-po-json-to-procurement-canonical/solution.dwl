%dw 2.0
output application/json
---
{
  poNum: payload.BEG.po,
  vendor: payload.BEG.vendor,
  lines: payload.PO1
    filter ((l) -> (l.qty as Number) > 0)
    map {
      sku: $.sku,
      qty: $.qty as Number,
      needBy: ($.aaa as Date {format: "yyyyMMdd"}) as String {format: "yyyy-MM-dd"}
    }
}
