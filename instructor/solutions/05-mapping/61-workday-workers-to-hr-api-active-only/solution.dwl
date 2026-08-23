%dw 2.0
output application/json
---
payload.Report_Entry
  filter ((w) -> lower(w.Status) == "active")
  map {
    id: $.wid,
    fullName: ($.Legal_First default "") ++ " " ++ ($.Legal_Last default ""),
    fte: $.FTE as Number,
    managerId: $.manager.wid default null
  }
