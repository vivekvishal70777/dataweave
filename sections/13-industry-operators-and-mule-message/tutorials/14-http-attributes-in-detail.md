# HTTP attributes in detail

*Section: Industry operators, message, and MIME · Interview Q74 · easy words*

## In one sentence

uriParams are path variables. queryParams are ?page=. headers are request/response headers. method is GET/POST.

## Like this in real life

/orders/O-1?page=2 — O-1 is uriParams, 2 is queryParams (often a string).

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  method: attributes.method,
  id: attributes.uriParams.id,
  page: attributes.queryParams.page,
  corr: attributes.headers['x-correlation-id']
}
```

## Remember

Know Listener vs HTTP Request. Coerce query numbers.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
