# and, or, not

*Section: Industry operators, message, and MIME · Interview Q78 · easy words*

## In one sentence

Use and or not, not Java && || !. Parenthesize mixed conditions. if needs else.

## Like this in real life

“(paid) and (amount > 0)” — say it in English, then add parentheses so the machine agrees.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
(lower(o.status) == "paid") and ((o.amount as Number) > 0)
```

## Remember

not binds tightest.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
