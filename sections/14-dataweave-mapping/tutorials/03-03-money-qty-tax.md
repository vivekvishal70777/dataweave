# Money, zero qty, tax

*Section: DataWeave Mapping · easy words*

## In one sentence

ERP amounts are strings. `as Number`, skip qty 0, `fun money` (`0.00` format), then tax.

## Like this in real life

A cashier does not add `"100.00"` as text. They tap the number keys, skip empty carts, then GST.

## Remember

- Intra-state GST: CGST+SGST. Inter-state: IGST.
- `default` does not catch bad `as Number` — use `try`.

Labs 60, 73, 88.
