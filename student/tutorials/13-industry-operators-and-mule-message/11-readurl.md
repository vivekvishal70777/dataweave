# readUrl

*Section: Industry operators, message, and MIME · Interview Q71 · easy words*

## In one sentence

readUrl loads a small file from classpath or URL. read parses something already in memory.

## Like this in real life

A tiny countries.json packed in the app. Not a 2 GB file inside map.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
readUrl("classpath://modules/iso-countries.json", "application/json")
```

## Remember

Large files: File connector, then one Transform.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
