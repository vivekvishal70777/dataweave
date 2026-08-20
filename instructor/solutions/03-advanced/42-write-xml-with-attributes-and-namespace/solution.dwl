%dw 2.0
ns ns0 http://acme.com/order
output application/xml
---
ns0#order @(id: payload.orderId): {
  (payload.lines map (li) -> {
    ns0#line @(sku: li.sku, qty: li.qty): {}
  })
}
