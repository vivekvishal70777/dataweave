# Pagination (drop / take)

*Section: Advanced: recursion, namespaces, diffs · Interview Q54 · easy words*

## In one sentence

drop skips items. take keeps the next n. That is page size.

## Like this in real life

Page 2 of size 2 on five boxes: skip two, take two.

## Tiny example

Read this slowly. Header first, then the body.

```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
var page = vars.page default 1
var size = vars.pageSize default 20
---
payload drop ((page - 1) * size) take size
```

## Remember

import dw::core::Arrays. Huge drop/take may still load the array.

Full interview answer: `reference/MuleSoft-DataWeave-Interview-Questions.md` (Q54). Then try the lab listed for this section.
