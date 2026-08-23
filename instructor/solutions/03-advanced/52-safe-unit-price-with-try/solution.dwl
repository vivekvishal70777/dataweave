%dw 2.0
import try, orElse from dw::Runtime
output application/json
---
payload map {
  id: $.id,
  unit: try(() -> ($.amount as Number) / ($.qty as Number)) orElse null
}
