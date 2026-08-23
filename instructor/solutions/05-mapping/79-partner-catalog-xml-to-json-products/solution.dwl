%dw 2.0
ns cat http://partner.example/cat
output application/json
---
payload.cat#Catalog.*cat#Item map {
  id: $.@id,
  name: $.cat#Name,
  price: $.cat#Price as Number
}
