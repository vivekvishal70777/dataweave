%dw 2.0
output application/json
---
{
  specversion: "1.0",
  id: payload.eventId,
  source: payload.source,
  type: payload.type,
  time: payload.now,
  datacontenttype: "application/json",
  data: payload - "eventId" - "now" - "source" - "type"
}
