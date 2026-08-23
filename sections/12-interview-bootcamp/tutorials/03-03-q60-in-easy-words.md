# Q60 in easy words

*Section: Interview bootcamp · easy words*

## In one sentence

Tell a story in eight beats: read XML, clean types, money, join customer you already have, shape names, write JSON, catch bad rows, keep it one-pass.

## Like this in real life

Unload a SOAP truck, put stickers in *your* shop language, do not phone the warehouse for every box.

## Remember

1. Reader: `ns`, Envelope/Body, `*Line`, `@sku`.
2. Normalize: `as Number`, date formats.
3. Enrich: `fun money`, `do` for line total.
4. Join: `vars.customer` already fetched — not `lookup` per line.
5. Shape: `orderId`, `currency`, `lines`.
6. Writer: `skipNullOn="everywhere"`.
7. Errors: `try` on bad price.
8. Scale: `map` once, no `orderBy` unless the API demands it.

Labs 41 and 54 are the typing version.
