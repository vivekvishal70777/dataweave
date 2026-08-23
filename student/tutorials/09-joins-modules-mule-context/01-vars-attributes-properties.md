# vars, attributes, properties

*Section: Joins, modules, and Mule context · Interview Q17 · easy words*

## In one sentence

payload is the body. vars are flow variables. attributes are metadata (HTTP headers, query). p() is config.

## Like this in real life

Parcel = payload. Sticky notes on the box = attributes. Your notebook = vars. Office policy sheet = properties.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
vars.customerId
attributes.headers["content-type"]
attributes.queryParams.page
p("http.host")               // from configuration properties
Mule::p("api.version")       // same idea in some contexts
```

## Remember

HTTP query values are often strings. Coerce page as Number.

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
