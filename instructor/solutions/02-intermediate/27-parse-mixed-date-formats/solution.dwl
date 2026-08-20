%dw 2.0
import try, orElseTry, orElse from dw::Runtime
output application/json
fun parseDate(s) =
  try(() -> s as Date {format: "yyyy-MM-dd"})
    orElseTry (() -> s as Date {format: "dd/MM/yyyy"})
    orElse null
---
payload map { id: $.id, date: parseDate($.date as String) }
