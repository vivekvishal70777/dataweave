# update

*Section: Group, reduce, merge, and update · Interview Q26 · easy words*

## In one sentence

update changes a nested field without rewriting the whole tree. Needs Mule 4.3+.

## Like this in real life

Changing only the city on an address label, not reprinting the whole shipping box.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
output application/json
---
payload update {
  case .customer.address.city -> upper($)
  case .items[0].qty -> $ + 1
}
```

## Remember

case .customer.address.city -> upper($)

After you try the lab for this section, replay the concept video. Spoken model answers are on the bootcamp mock video — not in a downloadable answer key.
