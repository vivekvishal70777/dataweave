%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
}
