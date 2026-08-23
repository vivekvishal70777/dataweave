# Reusable .dwl modules

*Section: Streaming, crypto, modules, and pitfalls · Interview Q46 · easy words*

## In one sentence

Put pure functions in a .dwl file. Import them. Unit-test them. Do not hide now() or lookup inside if you want tests.

## Like this in real life

A shared GST calculator used by many flows, like a company spreadsheet tab everyone copies from.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
fun withTax(amount: Number, rate: Number = 0.18) = amount * (1 + rate)
```

## Remember

import withTax from modules::Pricing. Inject time as a parameter.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q46). Then try the lab listed for this section.
