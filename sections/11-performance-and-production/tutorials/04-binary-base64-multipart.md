# Binary, Base64, multipart

*Section: Streaming, crypto, modules, and pitfalls · Interview Q52 · easy words*

## In one sentence

Treat files as Binary. toBase64 / fromBase64 in dw::core::Binaries. Multipart parts live on payload.parts.

## Like this in real life

A photo is bytes, not a JSON string. Do not turn a 50 MB file into a String.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Binaries
output application/json
---
{
  b64: toBase64(payload as Binary),
  bytes: fromBase64(vars.fileBase64),
  asText: (payload as Binary) as String {encoding: "UTF-8"}
}
```

## Remember

output application/octet-stream when the result must stay binary.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q52). Then try the lab listed for this section.
