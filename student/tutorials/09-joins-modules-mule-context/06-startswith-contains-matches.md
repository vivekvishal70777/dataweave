# startsWith, contains, matches

*Section: Joins, modules, and Mule context · Interview Q39 · easy words*

## In one sentence

startsWith and contains are simple text tests. matches is a full-string regular expression.

## Like this in real life

"MuleSoft" startsWith "Mule" is true. matches /[a-z]+/ is “the whole string is letters,” not “letters somewhere.”

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
"MuleSoft" startsWith "Mule"     // true
["a", "b"] contains "a"          // true
"abc123" matches /[a-z]+[0-9]+/  // true (full match vs regex)
```

## Remember

For a piece inside a string, use find or contains, not matches.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q39). Then try the lab listed for this section.
