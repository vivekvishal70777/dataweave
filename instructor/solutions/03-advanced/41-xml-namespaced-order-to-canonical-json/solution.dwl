%dw 2.0
ns ns0 http://acme.com/order
output application/json
---
{
  orderId: payload.ns0#order.@id,
  lines: payload.ns0#order.*ns0#line map {
    sku: $.@sku,
    qty: $.@qty as Number
  }
}
