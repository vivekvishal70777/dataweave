# Quiz 6 — Intermediate transforms

1. `groupBy` returns:
   - A) An array of keys
   - B) An **object** (group name → array of items)
   - C) A Boolean
   - D) CSV

2. If `reduce` has no accumulator initializer:
   - A) It always errors
   - B) The first element is the seed; iteration starts at the second
   - C) It returns null
   - D) It behaves like `map`

3. `++` merge of two objects is:
   - A) Deep merge of nested objects always
   - B) Shallow: right key overwrites
   - C) Array concatenation only
   - D) XML-only

4. `update { case .customer.address.city -> upper($) }` needs roughly:
   - A) DataWeave 1.0
   - B) Mule 4.3+ / DataWeave 2.3+
   - C) Java 8 only
   - D) CSV reader

5. `flatMap` is the right tool when:
   - A) You need a 1-to-many expansion then one-level flatten
   - B) You only uppercase a string
   - C) You set HTTP status
   - D) You declare a namespace
