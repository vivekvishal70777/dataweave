%dw 2.0
output application/json
fun okStatus(n) = (n as Number) >= 200 and (n as Number) < 300
var good = payload.responses filter ((r) -> okStatus(r.status))
var bad = payload.responses filter ((r) -> !okStatus(r.status))
---
{
  ok: good reduce ((r, acc = {}) -> acc ++ { (r.name): r.body }),
  errors: bad map { name: $.name, status: $.status, body: $.body }
}
