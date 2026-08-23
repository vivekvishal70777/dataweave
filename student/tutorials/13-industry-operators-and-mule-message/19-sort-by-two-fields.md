# Sort by two fields

*Section: Industry operators, message, and MIME · Interview Q79 · easy words*

## In one sentence

orderBy is one key. Descending numbers use minus. Two SQL columns is not two orderBy calls in a row.

## Like this in real life

Sort by region, and inside region by amount. Use a composite key or sort groups. Do not assume SQL ORDER BY a,b.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
payload orderBy ((o) -> o.region ++ "|" ++ leftPad((100000000 - (o.amount as Number)) as String, 12, "0"))
```

## Remember

Name this trap. Interviewers love it.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
