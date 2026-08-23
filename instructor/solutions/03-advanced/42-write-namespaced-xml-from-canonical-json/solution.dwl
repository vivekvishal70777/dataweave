%dw 2.0
ns ord http://acme.com/order
output application/xml
---
ord#PurchaseOrder @(id: payload.orderId, currency: payload.currency): {
  (payload.lines map (li) -> {
    ord#Line @(sku: li.sku, qty: li.qty, unitPrice: li.unitPrice): {}
  })
}
