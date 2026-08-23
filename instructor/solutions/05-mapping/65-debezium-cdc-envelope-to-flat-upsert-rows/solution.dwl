%dw 2.0
output application/json
---
payload.changes map (c) -> do {
  var row = if (c.op == "d") c.before else c.after
  ---
  {
    action: if (c.op == "d") "DELETE" else "UPSERT",
    id: row.id,
    status: row.status,
    tsMs: c.ts_ms
  }
}
