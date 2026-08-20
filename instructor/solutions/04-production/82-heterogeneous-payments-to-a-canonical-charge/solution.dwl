%dw 2.0
output application/json
fun charge(p) =
  p.method match {
    case "card" -> { method: "card", instrument: p.last4, ref: p.authCode }
    case "upi" -> { method: "upi", instrument: p.vpa, ref: p.txnId }
    case "netbanking" -> { method: "netbanking", instrument: p.bank, ref: p.refNo }
    else -> { method: "other", instrument: null, ref: null }
  }
---
payload.payments map charge($)
