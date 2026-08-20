%dw 2.0
output application/json
var body = payload.Envelope.Body
var fault = body.Fault
---
if (fault != null)
  { ok: false, code: fault.faultcode, message: fault.faultstring }
else
  { ok: true, data: body - "Fault" }
