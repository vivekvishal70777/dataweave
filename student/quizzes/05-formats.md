# Quiz 5 — JSON, XML, CSV

1. JSON to XML in DataWeave requires:
   - A) Multiple XML roots
   - B) A **single** root element
   - C) CSV headers
   - D) Java `Document`

2. XML attribute `id` on `order` is read as:
   - A) `payload.order.id`
   - B) `payload.order.@id`
   - C) `payload.@order`
   - D) `payload.order.#id`

3. Repeating XML children named `item` are often selected with:
   - A) `payload.item[all]`
   - B) `payload.*item`
   - C) `payload..@item`
   - D) `flatten(payload)`

4. Incoming CSV with a header row is typically:
   - A) A single string only
   - B) An array of objects (keys from the header)
   - C) A Java Map of rows to XML
   - D) Binary

5. `output application/csv header=true` uses object keys as:
   - A) XML namespaces
   - B) Column headers
   - C) Mule variables
   - D) MIME subtypes
