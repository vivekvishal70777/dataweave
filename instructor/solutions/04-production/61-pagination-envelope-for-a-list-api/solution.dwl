%dw 2.0
import * from dw::core::Arrays
output application/json
var page = payload.page as Number
var size = payload.size as Number
var total = sizeOf(payload.items)
var window = payload.items drop ((page - 1) * size) take size
var hasMore = (page * size) < total
---
{
  items: window,
  page: page,
  size: size,
  total: total,
  hasMore: hasMore,
  nextPage: if (hasMore) page + 1 else null
}
