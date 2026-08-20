%dw 2.0
import try from dw::Runtime
output application/json
fun isValid(r) = do {
  var ageOk = try(() -> (r.age as Number) >= 18).success default false
  ---
  (r.email default "") contains "@" and ageOk
}
---
{
  valid: payload filter isValid($),
  invalid: payload filter !isValid($)
}
