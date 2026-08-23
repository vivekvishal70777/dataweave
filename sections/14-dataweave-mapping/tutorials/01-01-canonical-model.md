# What a canonical mapping is

*Section: DataWeave Mapping · easy words*

## In one sentence

You copy the vendor’s ugly payload into **your** shop’s JSON names — `orderId`, `lines`, `money` — not SAP `vbeln`.

## Like this in real life

A warehouse relabels every box in the store language. The truck label can stay in German; the shelf cannot.

## Remember

- Header: `%dw 2.0`, `output application/json`, `---`.
- Drop fields you do not own.
- Lookups already on the payload — never `lookup` inside `map`.

Then open Lab 59.
