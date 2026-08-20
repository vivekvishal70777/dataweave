%dw 2.0
output application/json
var clock = payload.now as DateTime
---
payload.tickets map (t) -> {
  id: t.id,
  sla: t.status match {
    case "CLOSED" -> "CLOSED"
    else ->
      if ((t.dueAt as DateTime) < clock) "OVERDUE" else "ON_TRACK"
  }
}
