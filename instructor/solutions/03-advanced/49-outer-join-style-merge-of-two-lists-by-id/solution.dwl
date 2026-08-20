%dw 2.0
output application/json
var left = payload.left groupBy ((x) -> x.id)
var right = payload.right groupBy ((x) -> x.id)
var ids = (namesOf(left) ++ namesOf(right)) distinctBy $
---
ids map (id) -> (left[id][0] default {}) ++ (right[id][0] default {})
