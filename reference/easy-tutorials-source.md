# Easy tutorial source (do not teach from this file)

Parsed by `scripts/generate_easy_tutorials.py`. One block per interview question.

%%% 1
TITLE: What is DataWeave?
ONE: DataWeave is MuleSoft’s language for changing data from one shape to another.
LIFE: Think of a translator. A Salesforce Contact comes in as JSON. Your API wants a smaller JSON. DataWeave does that translation.
REMEMBER: In Mule 4 you write DataWeave in Transform Message, and also as #[...] in other steps. It is not Java.

%%% 2
TITLE: DataWeave 1.0 vs 2.0
ONE: Interviews want DataWeave 2.0 (Mule 4). Version 1.0 is the old Mule 3 style.
LIFE: Like switching from an old phone OS to a new one. Same idea, different buttons. Header is %dw 2.0, output is output application/json, not %output.
REMEMBER: If they say MEL, that is Mule 3. Mule 4 is DataWeave everywhere.

%%% 3
TITLE: The three parts of a script
ONE: Every script has a header, a line of dashes, then a body that becomes the output.
LIFE: Like a letter: address at the top (version and output type), a line, then the message.
REMEMBER: Say it out loud: percent dw two point oh, output, dash dash dash, then the expression.

%%% 4
TITLE: Variables (var)
ONE: var stores a value you can reuse. You cannot change it later. It is immutable.
LIFE: Like writing a GST rate of 0.18 on a sticky note. You read it many times. You do not scribble a new number on the same note.
REMEMBER: Put var in the header, or inside a do block for a local value.

%%% 5
TITLE: Functions (fun)
ONE: fun is a named recipe: give inputs, get an output. No side effects if you keep it pure.
LIFE: Like a kitchen function fullName(first, last) that always returns the same plate for the same ingredients.
REMEMBER: You can overload by types. Prefer type annotations in modules.

%%% 6
TITLE: Data types
ONE: Values have types: String, Number, Boolean, Array, Object, Date, Null, Binary, and more.
LIFE: A price should be a Number, not the text "99.99", until you coerce it. Mixing them is how scripts explode.
REMEMBER: Type names start with a capital. Any means “I did not specify.”

%%% 7
TITLE: Changing types with as
ONE: as tries to convert a value, like "10" as Number → 10.
LIFE: Like pouring juice into a measuring cup. If the cup is for millilitres and you pour sand, it fails.
REMEMBER: Failed as is an error. Use try, not default, when conversion can fail. Dates need a format.

%%% 8
TITLE: map and filter
ONE: filter keeps some items. map changes each item. You often filter first, then map.
LIFE: A conveyor belt of orders. Filter = throw away unpaid. Map = stick a shipping label on each remaining box.
REMEMBER: Name the item (order) -> in interviews. $ is shorter but harder to read.

%%% 9
TITLE: pluck
ONE: pluck walks an object and returns an array of whatever you build from each key and value.
LIFE: A form with fields Name, Age, City. pluck turns it into a list of rows for a spreadsheet.
REMEMBER: map is for arrays. mapObject is for objects that stay objects. pluck is object → array.

%%% 10
TITLE: plus-plus vs plus
ONE: ++ joins strings, arrays, or objects. + adds numbers. Do not mix them up.
LIFE: "Hello" ++ " " ++ "World" is gluing paper. 1 + 2 is maths. Glue on numbers, or maths on words, and Mule shouts.
REMEMBER: Object ++ is a shallow merge. The right-hand key wins.

%%% 11
TITLE: Missing fields and null
ONE: default replaces null. The safe selector ? stops you crashing if a parent is missing.
LIFE: If the guest left the email blank, print noreply. If they have no address at all, do not look for city inside nothing.
REMEMBER: default does not catch as Number failures. That is try.

%%% 12
TITLE: if / else
ONE: if/else is an expression. It must produce a value. There is no Java question-mark colon.
LIFE: Like a vending machine: if code is 503, spit out "retry". Every path must spit something.
REMEMBER: You need else. A lonely if is illegal.

%%% 13
TITLE: Selectors (dot, brackets, star, dots)
ONE: Dot is a field. Brackets are index or odd names. Star is repeating children. Two dots means “search descendants.”
LIFE: A filing cabinet. customer.name is a labelled drawer. [0] is the first folder. .*item is every “item” tab. ..id is “find every id sticker in the whole cabinet.”
REMEMBER: XML attributes use at-sign: order.@id.

%%% 14
TITLE: JSON to XML and back
ONE: Change the output MIME type and shape a tree. XML must have exactly one root.
LIFE: JSON is Lego bricks in a bag. XML is the same bricks snapped under one lid. No lid, or two lids, and XML is invalid.
REMEMBER: JSON → XML = output application/xml plus a root key. XML → JSON = output application/json and pick elements.

%%% 15
TITLE: sizeOf and isEmpty
ONE: sizeOf counts. isEmpty asks “is there nothing?” Prefer isEmpty when you only care about empty vs not.
LIFE: Do not count every grain of rice to see if the bowl is empty. Just look.
REMEMBER: sizeOf works on arrays, objects (keys), and strings.

%%% 16
TITLE: Split, join, and case
ONE: splitBy cuts a string into an array. joinBy glues an array into a string. upper / lower / capitalize change case.
LIFE: CSV line "Asha,IT,Pune" splitBy comma is three boxes. joinBy comma packs them again.
REMEMBER: Import dw::core::Strings for trim, replace, substringAfter.

%%% 17
TITLE: vars, attributes, properties
ONE: payload is the body. vars are flow variables. attributes are metadata (HTTP headers, query). p() is config.
LIFE: Parcel = payload. Sticky notes on the box = attributes. Your notebook = vars. Office policy sheet = properties.
REMEMBER: HTTP query values are often strings. Coerce page as Number.

%%% 18
TITLE: Transform Message vs #[...]
ONE: Transform Message is a full script with preview. #[...] is a tiny DataWeave expression inside another processor.
LIFE: Transform Message is a full kitchen. #[payload.orderId] is grabbing one spice while the soup is already cooking.
REMEMBER: Both are DataWeave 2 in Mule 4. Big mappings belong in Transform Message.

%%% 19
TITLE: write and read
ONE: write turns a value into text or bytes. read parses text or bytes back into data. They do not change the script’s output MIME by themselves.
LIFE: write is photocopying a form to PDF in your hand. output application/json is the stamp on the envelope you actually mail.
REMEMBER: write(payload) on a huge file can break streaming.

%%% 20
TITLE: skipNullOn and writer properties
ONE: Writer properties sit on the output line. skipNullOn="everywhere" hides null fields in JSON or XML.
LIFE: If a field is empty, do not print a blank line on the invoice.
REMEMBER: indent=false makes compact JSON. CSV uses header=true and separator.

%%% 21
TITLE: mapObject
ONE: mapObject walks an object and returns an object. Use it to rename keys or change every value.
LIFE: A form where you uppercase every label but keep the same boxes.
REMEMBER: map = lists. mapObject = objects. Mixing them is a common interview fail.

%%% 22
TITLE: groupBy, orderBy, distinctBy
ONE: groupBy buckets items by a key (returns an object of arrays). orderBy sorts. distinctBy unique by a key (keeps first).
LIFE: groupBy customerId is sorting mail into pigeonholes. distinctBy email throws duplicate letters, keeping the first.
REMEMBER: groupBy is not an array. You pluck or namesOf to walk groups.

%%% 23
TITLE: reduce
ONE: reduce folds a list into one value: a sum, or a growing object.
LIFE: A running total on a till. Each item updates the drawer. The drawer is the accumulator.
REMEMBER: Give the accumulator a starting value (acc = 0 or acc = {}) or the first item becomes the seed.

%%% 24
TITLE: flatten
ONE: flatten removes one level of nesting in arrays. [[1,2],[3]] becomes [1,2,3].
LIFE: Opening inner boxes once. Boxes inside those inner boxes stay closed. That deeper job is recursion.
REMEMBER: One flatten is not a deep flatten.

%%% 25
TITLE: Merging objects
ONE: ++ copies keys. If both sides have the same key, the right side wins. That merge is shallow.
LIFE: Overlaying a new config file on an old one. retries: 5 replaces retries: 2. Nested objects are replaced whole, not mixed, unless you use mergeWith.
REMEMBER: mergeWith is the deep-merge follow-up.

%%% 26
TITLE: update
ONE: update changes a nested field without rewriting the whole tree. Needs Mule 4.3+.
LIFE: Changing only the city on an address label, not reprinting the whole shipping box.
REMEMBER: case .customer.address.city -> upper($)

%%% 27
TITLE: do blocks
ONE: do makes a tiny local header (var/fun) so the main header stays clean.
LIFE: Scratch paper inside one map step: compute tax, then output the line. Throw the scratch paper away.
REMEMBER: Use do when a map body would be messy.

%%% 28
TITLE: match
ONE: match picks a branch by value, type, or a condition. Always have else.
LIFE: A sorting hat: 2xx → ok, 4xx → client, else → other.
REMEMBER: This is not Java switch with break. It is an expression.

%%% 29
TITLE: try
ONE: try runs a risky expression and lets you orElse a fallback if it fails.
LIFE: Tasting soup. If it burns (bad as Number), serve water (0 or null) instead of throwing the pot.
REMEMBER: try is not Mule On Error. HTTP timeouts still need On Error.

%%% 30
TITLE: Dates and periods
ONE: Parse with as Date {format:...}. Format with as String {format:...}. Add |P7D| for seven days.
LIFE: A calendar stamp. The same instant can print as 20-Aug-2026. A period is “how long,” not a clock time.
REMEMBER: Pipe literals: |2026-08-20|. Prefer injecting time over now() in modules.

%%% 31
TITLE: CSV to JSON
ONE: With header=true, each CSV row becomes an object. Keys come from the header line. Coerce numbers.
LIFE: Excel export → list of records. Amount is text until as Number.
REMEMBER: Set MIME application/csv on the incoming message.

%%% 32
TITLE: JSON to CSV
ONE: output application/csv header=true. Object keys become column names.
LIFE: Your API list becomes a finance spreadsheet.
REMEMBER: Every row object should use the same keys.

%%% 33
TITLE: XML attributes vs elements
ONE: @id is an attribute on the tag. A child tag is an element. *item is repeating children.
LIFE: <order id="O-1"> — id is written on the sticker. <amount>50</amount> is a box inside.
REMEMBER: To write attributes: order @(id: payload.id): { ... }

%%% 34
TITLE: Modules and import
ONE: import brings functions from dw::core::Strings, Arrays, Objects, Dates, Crypto, Runtime, or your own .dwl file.
LIFE: Borrowing a toolbox instead of forging every hammer.
REMEMBER: Custom modules live under src/main/resources/modules. import x from modules::Pricing

%%% 35
TITLE: Dollar signs in lambdas
ONE: $ is the item. $$ is usually the index or key. $$$ is rare (third argument).
LIFE: In a queue, $ is the person, $$ is their number in line (starting at 0).
REMEMBER: Named arguments (item, index) -> are clearer in interviews.

%%% 36
TITLE: filterObject
ONE: filterObject keeps object keys where a test is true. Use it to drop password and ssn.
LIFE: Redacting a form before you photocopy it for the log file.
REMEMBER: Compare lower(k as String). Keys are not always plain strings.

%%% 37
TITLE: SQL-style joins
ONE: leftJoin (and friends) live in dw::core::Arrays. Result items look like { l: left, r: right }.
LIFE: Orders on the left, customers on the right. Missing customer means r is null.
REMEMBER: Import leftJoin. Then map to a flat { orderId, customerName }.

%%% 38
TITLE: Calling Java
ONE: You can import java!... and call static methods. Prefer pure DataWeave for mapping.
LIFE: Asking a neighbour (Java) to lend a special tool. Do not ask them to butter every slice in a map of 10,000 rows.
REMEMBER: Java can hurt streaming and tests. Use it for libraries DW cannot replace.

%%% 39
TITLE: startsWith, contains, matches
ONE: startsWith and contains are simple text tests. matches is a full-string regular expression.
LIFE: "MuleSoft" startsWith "Mule" is true. matches /[a-z]+/ is “the whole string is letters,” not “letters somewhere.”
REMEMBER: For a piece inside a string, use find or contains, not matches.

%%% 40
TITLE: lookup vs doing it in DataWeave
ONE: lookup calls another Mule flow and waits. Inside map it becomes N+1 slow calls.
LIFE: Phoning the warehouse once per line on a 5,000-line order. Fetch the catalog first, then join in DataWeave.
REMEMBER: Index with groupBy, or enrich before Transform Message.

%%% 41
TITLE: Streaming
ONE: Streaming means DataWeave reads a huge file in pieces. It breaks if you need the whole file at once.
LIFE: Watching a movie as it downloads vs downloading the whole movie to sort scenes. orderBy, groupBy, sizeOf(payload) need the whole movie.
REMEMBER: One-pass map and filter can stream. Mention this in every senior interview.

%%% 42
TITLE: Recursion
ONE: A function that calls itself to walk trees: arrays, objects, then leaves.
LIFE: Opening every nested gift box until you find the toy. Same motion at every layer.
REMEMBER: match { case a is Array -> ... case o is Object -> ... else -> ... }

%%% 43
TITLE: flatMap
ONE: flatMap is map, then flatten one level. Perfect for one order → many line rows.
LIFE: Each pizza order opens into several slices on a single serving tray, not a tray of trays.
REMEMBER: flatten(payload map ...) is the same idea.

%%% 44
TITLE: XML namespaces
ONE: ns prefix URI then prefix#Element. The prefix is yours. The URI must match the XML.
LIFE: Two families both named “Order.” The URI is the family address so you do not mix them.
REMEMBER: SOAP: Envelope, Body, then your element. Repeating lines use *prefix#Line.

%%% 45
TITLE: Hash vs HMAC
ONE: Hash is a checksum (integrity). HMAC is a hash with a secret (authenticity).
LIFE: Hash: “did this file change?” HMAC: “did someone with our kitchen key sign this webhook?”
REMEMBER: dw::Crypto. Watch Binary vs String and Base64 wrapping.

%%% 46
TITLE: Reusable .dwl modules
ONE: Put pure functions in a .dwl file. Import them. Unit-test them. Do not hide now() or lookup inside if you want tests.
LIFE: A shared GST calculator used by many flows, like a company spreadsheet tab everyone copies from.
REMEMBER: import withTax from modules::Pricing. Inject time as a parameter.

%%% 47
TITLE: keysOf, namesOf, valuesOf, entriesOf
ONE: keysOf is XML-aware keys. namesOf is string names (usual JSON). valuesOf is values. entriesOf is {key, value} list.
LIFE: A coat check: names of coats, the coats themselves, or tickets paired with coats.
REMEMBER: For JSON dynamic keys, namesOf is what you usually want.

%%% 48
TITLE: Dynamic keys
ONE: Wrap the key expression in parentheses: { (item.id): item.name }.
LIFE: The label on the box is printed from the barcode, not handwritten as the word “item.id”.
REMEMBER: Without ( ), the key is the literal text. This is a top interview trap.

%%% 49
TITLE: Diff two payloads
ONE: Compare old and new. List fields that changed, with from and to.
LIFE: Change-data-capture: status NEW → PAID. Amount unchanged? Skip it.
REMEMBER: Nested diffs need recursion. Flat CDC is namesOf plus !=.

%%% 50
TITLE: Function overloading
ONE: Same fun name, different argument types. The most specific match wins.
LIFE: describe("hi") vs describe(3) print different labels, like two stamps in one drawer.
REMEMBER: Pair with match { case x is Date -> } for trees.

%%% 51
TITLE: Mixed date formats
ONE: try the first format, orElseTry the next, orElse null.
LIFE: Customers type 2026-08-20 or 20/08/2026. You accept both. Garbage becomes null, not a crash.
REMEMBER: default will not save a failed as Date.

%%% 52
TITLE: Binary, Base64, multipart
ONE: Treat files as Binary. toBase64 / fromBase64 in dw::core::Binaries. Multipart parts live on payload.parts.
LIFE: A photo is bytes, not a JSON string. Do not turn a 50 MB file into a String.
REMEMBER: output application/octet-stream when the result must stay binary.

%%% 53
TITLE: Reader and writer properties
ONE: Readers parse input (CSV header, XML encoding). Writers shape output (indent, skipNullOn).
LIFE: Incoming stamp vs outgoing stamp. CSV separator is often on the MIME type of the message, not only in the script.
REMEMBER: JSON streaming, XML writeDeclaration, CSV header=true.

%%% 54
TITLE: Pagination (drop / take)
ONE: drop skips items. take keeps the next n. That is page size.
LIFE: Page 2 of size 2 on five boxes: skip two, take two.
REMEMBER: import dw::core::Arrays. Huge drop/take may still load the array.

%%% 55
TITLE: Last-wins dedupe
ONE: distinctBy keeps the first. For last-wins, reduce into an object keyed by id, then valuesOf.
LIFE: Two profile updates with the same email. You want the latest row, not the first.
REMEMBER: This is the CDC upsert story.

%%% 56
TITLE: then and also
ONE: then passes the left value into the next expression as $. also is rare. Prefer a clear do block if chaining gets clever.
LIFE: then is “take this tray and make a box { count, items }.”
REMEMBER: Readable beats clever in interviews.

%%% 57
TITLE: Mask PII in an unknown tree
ONE: Walk objects and arrays. If the key is email/ssn/password, output stars. Else keep walking.
LIFE: A marker over secrets on every page of a mixed folder, not only the cover sheet.
REMEMBER: Mask before log. Known paths can use update instead.

%%% 58
TITLE: Performance pitfalls
ONE: Name: groupBy on huge data, O(n²) nested filter, lookup in map, payload as String, XML .. on big docs, breaking streaming.
LIFE: Index the customer list once (groupBy id), then map orders. Do not search the whole list for every order.
REMEMBER: Coerce money once. No I/O inside map.

%%% 59
TITLE: Higher-order functions
ONE: Functions can take functions. map already does this. You can write applyTwice(x, f).
LIFE: A machine that applies “uppercase” twice, or any stamp you pass in.
REMEMBER: Lambdas are values. Interviewers may ask compose or treeMap.

%%% 60
TITLE: End-to-end XML to canonical JSON (design)
ONE: Talk the pipeline: read namespaces, coerce types, money functions, join customer from vars, skipNullOn, no lookup per line.
LIFE: Unpacking a SOAP crate, labelling products in your shop’s language, and not phoning the warehouse for every SKU.
REMEMBER: Reader → normalize → enrich → shape → writer → errors → scale. Lab 41 plus Lab 54.

%%% 61
TITLE: maxBy, firstWith, and friends
ONE: maxBy returns the whole item with the biggest field, not just the number. firstWith returns the first match.
LIFE: richest order is the whole order record. firstPaid is the first PAID in line, even if a later one is bigger.
REMEMBER: import dw::core::Arrays. Guard empty lists.

%%% 62
TITLE: Ranges and slice
ONE: [0 to 2] is the first three items (inclusive). 1 to 5 is numbers 1,2,3,4,5. slice is a clear window.
LIFE: Taking pages 1–3 of a report.
REMEMBER: Prefer slice / take / drop in production code.

%%% 63
TITLE: zip
ONE: zip pairs two arrays: headers with values. Then you can build an object.
LIFE: A blank form (headers) and a handwritten row (values). zip staples them cell by cell.
REMEMBER: Length follows the shorter array.

%%% 64
TITLE: is and typeOf
ONE: is checks a type. typeOf names it. DataWeave has no Java ===.
LIFE: “Is this a box of apples or a single apple?” Arrays and objects need different walks.
REMEMBER: payload is Object. match { case x is Array -> }.

%%% 65
TITLE: Number helpers and money
ONE: sum, avg, min, max, mod, ceil, floor. Money: format 0.00 then as Number.
LIFE: ERP sends "10.50" as text. Coerce, then round like a cashier, not like a calculator with dust.
REMEMBER: sum of empty can surprise you. default 0 or skip.

%%% 66
TITLE: Timezones
ONE: DateTime has an offset. Shift with >> "Asia/Kolkata". Store UTC. Convert at the edge.
LIFE: A meeting at 14:05 UTC is 19:35 in India. Same moment, different wall clock.
REMEMBER: Do not use now() in a pricing module. Inject asOf.

%%% 67
TITLE: Dates module helpers
ONE: daysBetween, atBeginningOfDay, plus |P1M|. Periods are durations.
LIFE: Invoice due in 30 days. SLA clock in hours (|PT2H|).
REMEMBER: import dw::core::Dates.

%%% 68
TITLE: replace, find, substring
ONE: replace can use regex. find extracts matches. substringBefore("-") takes the SKU family.
LIFE: Black out invoice numbers in a comment. Pull INV-123 out of a sentence.
REMEMBER: matches = whole string. find = pieces inside.

%%% 69
TITLE: Several outputs in Transform Message
ONE: One component can set payload and variables. Each target is its own script.
LIFE: Stamp the parcel (payload) and write the tracking number in your notebook (vars) in the same desk visit.
REMEMBER: Playground cannot set Mule vars. Lab 58 simulates both in one JSON.

%%% 70
TITLE: application/java
ONE: After many connectors, payload is a Java Map/List, not a JSON string. Selectors still use dot.
LIFE: The same shopping list, written in pencil (Java) not printed as JSON. You still read “milk.”
REMEMBER: Do not payload as String then parse unless you must.

%%% 71
TITLE: readUrl
ONE: readUrl loads a small file from classpath or URL. read parses something already in memory.
LIFE: A tiny countries.json packed in the app. Not a 2 GB file inside map.
REMEMBER: Large files: File connector, then one Transform.

%%% 72
TITLE: log and application/dw
ONE: log prints and returns the value. application/dw is a debug view. Never log PII.
LIFE: A sticky “DEBUG: order O-1” on the belt. Not a photocopy of passports.
REMEMBER: log is not try and not On Error.

%%% 73
TITLE: try vs On Error
ONE: try is inside the script (bad coerce). On Error is the flow (HTTP 500, timeout).
LIFE: Burnt toast = try, serve jam. House fire = fire alarm (On Error), not more jam.
REMEMBER: error.errorType and error.errorMessage.payload live in On Error scopes.

%%% 74
TITLE: HTTP attributes in detail
ONE: uriParams are path variables. queryParams are ?page=. headers are request/response headers. method is GET/POST.
LIFE: /orders/O-1?page=2 — O-1 is uriParams, 2 is queryParams (often a string).
REMEMBER: Know Listener vs HTTP Request. Coerce query numbers.

%%% 75
TITLE: Default XML namespace and CDATA
ONE: Default xmlns still needs ns and prefix#Element. The URI must match. CDATA is usually just text.
LIFE: A nameless family still has an address (URI). You give them a nickname (prefix) in DataWeave.
REMEMBER: Mixed content is messy. Push back on the contract if you can.

%%% 76
TITLE: YAML, Excel, flat file
ONE: DataWeave follows MIME. YAML may work. Excel often needs the Excel module. EDI uses flat-file schemas, not splitBy.
LIFE: Do not open an .xlsx by splitting commas. That is the wrong tool.
REMEMBER: Playground may lack some MIME types. Say that in interviews.

%%% 77
TITLE: Values::mask vs recursive mask
ONE: Known paths → update or mask. Unknown depth → recursive match on types (Lab 39).
LIFE: If secrets always sit in customer.ssn, use a precise marker. If secrets hide anywhere, search the whole house.
REMEMBER: Mask before logging.

%%% 78
TITLE: and, or, not
ONE: Use and or not, not Java && || !. Parenthesize mixed conditions. if needs else.
LIFE: “(paid) and (amount > 0)” — say it in English, then add parentheses so the machine agrees.
REMEMBER: not binds tightest.

%%% 79
TITLE: Sort by two fields
ONE: orderBy is one key. Descending numbers use minus. Two SQL columns is not two orderBy calls in a row.
LIFE: Sort by region, and inside region by amount. Use a composite key or sort groups. Do not assume SQL ORDER BY a,b.
REMEMBER: Name this trap. Interviewers love it.

%%% 80
TITLE: DataWeave vs For Each vs Batch vs Java
ONE: DataWeave maps CPU-only. For Each calls connectors per item. Batch is huge files and retries. Java is special libraries.
LIFE: DW = folding letters. For Each = posting each letter. Batch = the industrial mail warehouse. Java = a custom stamp machine.
REMEMBER: No lookup/HTTP inside map.
