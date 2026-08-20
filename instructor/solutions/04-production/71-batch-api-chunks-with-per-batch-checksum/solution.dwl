%dw 2.0
import divideBy from dw::core::Arrays
output application/json
---
(payload.records divideBy payload.size) map (chunk, idx) -> {
  batchId: "B" ++ (idx + 1),
  count: sizeOf(chunk),
  ids: chunk.id,
  checksum: sum(chunk.id)
}
