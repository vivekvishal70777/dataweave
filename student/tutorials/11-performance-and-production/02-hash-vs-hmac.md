# Hash vs HMAC

*Section: Streaming, crypto, modules, and pitfalls · Interview Q45 · easy words*

## In one sentence

Hash is a checksum (integrity). HMAC is a hash with a secret (authenticity).

## Like this in real life

Hash: “did this file change?” HMAC: “did someone with our kitchen key sign this webhook?”

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import dw::Crypto
output application/json
---
{
  sha: Crypto::hashWith(payload as Binary, "SHA-256"),
  hmac: Crypto::HMACBinary(payload as Binary, "secret" as Binary, "HmacSHA256")
}
```

## Remember

dw::Crypto. Watch Binary vs String and Base64 wrapping.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q45). Then try the lab listed for this section.
