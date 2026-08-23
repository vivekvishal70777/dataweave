# Quiz 9 — Advanced

1. Deep flatten of mixed nested arrays is done with:
   - A) A single `flatten` call always
   - B) Recursion + `match` on `Array` (and `flatMap`)
   - C) `splitBy`
   - D) `p()`

2. Dynamic object keys require:
   - A) `{ f.name: f.value }`
   - B) `{ (f.name): f.value }`  (parentheses)
   - C) `map` only
   - D) CSV `header=false`

3. `distinctBy` keeps:
   - A) The last duplicate
   - B) The **first** match
   - C) All duplicates
   - D) None of the items

4. Namespaced XML element `order` in namespace `ns0` is selected like:
   - A) `payload.ns0.order`
   - B) `payload.ns0#order`
   - C) `payload.@ns0`
   - D) `payload..ns0`

5. Recursive PII masking walks:
   - A) Only the first key
   - B) Objects with `mapObject` and arrays with `map`, matching secret key names
   - C) Only CSV
   - D) Only `vars`

6. A SOAP purchase order inside `Envelope/Body` with prefix `ord` is typically selected with:
   - A) `payload.ord.PurchaseOrder` only
   - B) `ns` declarations plus `payload.soap#Envelope.soap#Body.ord#PurchaseOrder`
   - C) `p("soap")`
   - D) `lookup("soap")`
