%dw 2.0
output application/json
---
{
  replayKey: payload.record.customerId ++ "|" ++ payload.record.orderId,
  failedAt: payload.now,
  errorType: payload.errorType,
  original: payload.record
}
