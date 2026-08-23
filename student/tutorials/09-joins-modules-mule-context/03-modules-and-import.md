# Modules and import

*Section: Joins, modules, and Mule context · Interview Q34 · easy words*

## In one sentence

import brings functions from dw::core::Strings, Arrays, Objects, Dates, Crypto, Runtime, or your own .dwl file.

## Like this in real life

Borrowing a toolbox instead of forging every hammer.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Strings
import someFun from modules::MyModule
import dw::core::Arrays
output application/json
---
Arrays.drop(payload, 2)
```

## Remember

Custom modules live under src/main/resources/modules. import x from modules::Pricing

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
