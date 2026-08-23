%dw 2.0
ns soap http://schemas.xmlsoap.org/soap/envelope/
ns ord http://acme.com/order
output application/json
---
{
  orderId: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@id,
  currency: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.@currency,
  lines: payload.soap#Envelope.soap#Body.ord#PurchaseOrder.*ord#Line map {
    sku: $.@sku,
    qty: $.@qty as Number,
    unitPrice: $.@unitPrice as Number
  }
}
