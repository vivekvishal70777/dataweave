%dw 2.0
output application/json
var old = vars.old
var newp = payload
var allKeys = (namesOf(old) ++ namesOf(newp)) distinctBy $
---
allKeys
  filter ((k) -> old[k] != newp[k])
  map (k) -> { field: k, from: old[k], to: newp[k] }
