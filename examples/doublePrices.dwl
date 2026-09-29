%dw 2.0
output application/json

var cart = {
  apple: 2,
  bread: 3,
  milk: 4
}
---
cart mapObject (value, key) -> {
  (key): value * 2
}
