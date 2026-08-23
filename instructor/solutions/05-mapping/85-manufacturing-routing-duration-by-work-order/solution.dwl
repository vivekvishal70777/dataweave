%dw 2.0
output application/json
---
payload groupBy $.wo
  pluck ((rows, wo) -> do {
    var ordered = rows orderBy $.seq map { seq: $.seq as Number, step: $.step, min: $.min as Number }
    ---
    { wo: wo, steps: ordered, totalMinutes: sum(ordered.min) }
  })
