%dw 2.0
output application/json
fun event(c) =
  c.op match {
    case "c" -> { type: "created", id: c.after.id, record: c.after, ts: c.ts }
    case "u" -> { type: "updated", id: c.after.id, record: c.after, ts: c.ts }
    case "d" -> { type: "deleted", id: c.before.id, record: c.before, ts: c.ts }
    else -> null
  }
---
payload.changes map event($) filter $ != null
