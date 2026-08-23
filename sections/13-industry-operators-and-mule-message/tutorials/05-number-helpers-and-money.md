# Number helpers and money

*Section: Industry operators, message, and MIME · Interview Q65 · easy words*

## In one sentence

sum, avg, min, max, mod, ceil, floor. Money: format 0.00 then as Number.

## Like this in real life

ERP sends "10.50" as text. Coerce, then round like a cashier, not like a calculator with dust.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
{
  abs: abs(-3),
  ceil: ceil(1.1),
  floor: floor(1.9),
  mod: 10 mod 3,
  pow: pow(2, 8)
}
```

## Remember

sum of empty can surprise you. default 0 or skip.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
