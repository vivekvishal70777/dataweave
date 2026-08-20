%dw 2.0
output application/json
fun overlay(a, b) =
  (a match {
    case ao is Object if b is Object ->
      ((namesOf(ao) ++ namesOf(b)) distinctBy $)
        reduce ((k, acc = {}) -> acc ++ { (k): overlay(ao[k], b[k]) })
    else -> b default a
  })
var mid = overlay(payload.defaults, payload.tenant)
var merged = overlay(mid, payload.request)
---
merged update {
  case .featureFlags -> (
    payload.request.featureFlags default
      (payload.tenant.featureFlags default payload.defaults.featureFlags)
  )
}
