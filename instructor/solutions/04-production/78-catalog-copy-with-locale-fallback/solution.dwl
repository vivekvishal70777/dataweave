%dw 2.0
output application/json
fun label(key) =
  payload.copy[payload.locale][key] default payload.copy[payload.fallback][key] default null
---
{
  locale: payload.locale,
  hi: label("hi"),
  bye: label("bye")
}
