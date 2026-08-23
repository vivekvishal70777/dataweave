%dw 2.0
output application/json
var b = payload.base
var t = payload.tenant
---
(b ++ t) ++ {
  plugins: ((b.plugins default []) ++ (t.plugins default [])) distinctBy $
}
