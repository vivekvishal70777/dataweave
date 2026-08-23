# YAML, Excel, flat file

*Section: Industry operators, message, and MIME · Interview Q76 · easy words*

## In one sentence

DataWeave follows MIME. YAML may work. Excel often needs the Excel module. EDI uses flat-file schemas, not splitBy.

## Like this in real life

Do not open an .xlsx by splitting commas. That is the wrong tool.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
// YAML: set reader MIME application/yaml, then map like JSON.
// Excel / EDI: connector or flat-file schema first, then this script.
payload.rows map {
  sku: $.sku
}
```

## Remember

Playground may lack some MIME types. Say that in interviews.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
