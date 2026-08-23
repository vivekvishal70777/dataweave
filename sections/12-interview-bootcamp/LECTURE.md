# Section — Interview bootcamp

Use this file as the **article lecture** and recording outline on Udemy.

**Easy-word tutorials (one page per topic):** [`../../student/tutorials/12-interview-bootcamp/README.md`](../../student/tutorials/12-interview-bootcamp/README.md) (copies also in `tutorials/` next to this file).

## Learning objectives

- Answer the 80-question bank out loud.
- Whiteboard the six signature programs.
- Talk through the nested XML → JSON design (Q60).

## Suggested video breakdown

- Do not re-teach Q1–80. Those answers were already taught in sections 2–12.
- Record timed drills: verbal flashcards, then whiteboard labs, then Q60 as a design talk.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 20
- Lab 23
- Lab 32
- Lab 39
- Lab 41
- Lab 53
- Lab 54

## This is not a second teaching pass

Q1–80 already appear in **topic sections** (easy tutorial → concept video → demo → lab → quiz).
Do **not** record another 80 videos here. Students drill from **prompts only** (no answer key in the zip).

Students use `student/resources/interview-prompts.md` (questions only). Never attach the full Q&A zip here.

### What to publish in this section

1. **Article** — how to drill. Attach **`student/resources/interview-prompts.md` only** (80 questions, no answers).
2. **Video: verbal mock** — you ask 8 mixed questions (easy + hard). Pause card after each prompt. Then you give a model 60-second answer. Do not open Studio.
3. **Video: whiteboard** — timebox 8 minutes each on Labs 23, 20, 32, 39, 41, 53/54 (pick 3 on camera; assign the rest).
4. **Video: Q60 design talk** — eight beats only (reader, types, money, join, shape, writer, try, scale). They already coded Lab 41 + 54.
5. **Practice test** — final quiz, not a lecture.

### Question checklist (titles only — do not read answers on camera)

- Q1. What is DataWeave?
- Q2. What is the difference between DataWeave 1.0 and DataWeave 2.0?
- Q3. What is the basic structure of a DataWeave script?
- Q4. How do you declare a variable in DataWeave?
- Q5. How do you define a custom function?
- Q6. What are the main DataWeave data types?
- Q7. How do you convert types (`as`)?
- Q8. How do `map` and `filter` work on arrays?
- Q9. What is `pluck`?
- Q10. How do you concatenate strings and arrays?
- Q11. How do you handle missing fields and nulls?
- Q12. How do you write if/else in DataWeave?
- Q13. What is the difference between `.` and `[]` selectors?
- Q14. How do you transform JSON to XML (and vice versa)?
- Q15. What does `sizeOf` and `isEmpty` do?
- Q16. How do you split, join, and change case of strings?
- Q17. How do you read Mule variables, attributes, and properties in DataWeave?
- Q18. What is the difference between Transform Message and a DataWeave expression in a Set Payload?
- Q19. How do you `write` and `read` data inside a script?
- Q20. What does `output application/json skipNullOn="everywhere"` do?
- Q21. Explain `mapObject`. When do you use it instead of `map`?
- Q22. How do `groupBy`, `orderBy`, and `distinctBy` work?
- Q23. Explain `reduce`. Give an example of a sum and of building an object.
- Q24. How do you flatten nested arrays?
- Q25. How do you merge two objects? What happens with duplicate keys?
- Q26. How do you update a nested field without rebuilding the whole object?
- Q27. What is a `do` block and why is it useful?
- Q28. How does pattern matching (`match`) work?
- Q29. How do you handle errors in DataWeave (`try`)?
- Q30. How do you work with dates and periods?
- Q31. How do you transform CSV to JSON?
- Q32. How do you generate CSV from JSON?
- Q33. How do you read XML attributes vs elements?
- Q34. What are DataWeave modules? How do you import them?
- Q35. Explain `$`, `$$`, and `$$$` in lambdas.
- Q36. How do you filter object keys dynamically?
- Q37. How do you join two arrays like a SQL join?
- Q38. How do you call Java from DataWeave? When should you not?
- Q39. What is the difference between `startsWith`, `contains`, and `matches`?
- Q40. How do you use `lookup` (Mule 4) vs DataWeave-only alternatives?
- Q41. How does DataWeave streaming work? When does it break?
- Q42. Write a recursive function to flatten a nested tree of objects/arrays.
- Q43. How do you implement `flatMap` / why does it matter?
- Q44. How do you preserve XML namespaces and generate namespaced output?
- Q45. Explain `dw::Crypto` hashing vs HMAC. When is each used?
- Q46. How do you write a reusable `.dwl` module and unit-test it?
- Q47. What is the difference between `valuesOf`, `keysOf`, `namesOf`, and `entriesOf`?
- Q48. How do you dynamically construct object keys?
- Q49. How do you compare two payloads and produce a diff of changed fields?
- Q50. Explain function overloading and type patterns in DataWeave.
- Q51. How do you parse a non-standard date or mixed-format field robustly?
- Q52. How do you process multipart / binary / Base64 in DataWeave?
- Q53. What are reader/writer properties you should mention for XML, JSON, and CSV?
- Q54. How do you implement pagination-style `take` / `drop` / windows on arrays?
- Q55. How would you de-duplicate while keeping the last occurrence?
- Q56. Explain `then`, `also`, and chaining vs nested calls.
- Q57. How do you mask PII in a payload of unknown shape?
- Q58. What performance pitfalls do interviewers expect you to name?
- Q59. How do you write an infix-friendly custom function and use lambdas as arguments (higher-order functions)?
- Q60. End-to-end: map a nested order XML to a canonical JSON API model (talk through the design).
- Q61. What `dw::core::Arrays` helpers do interviewers expect besides map/filter?
- Q62. How do ranges and `slice` work?
- Q63. How do you `zip` two arrays?
- Q64. How do you test types (`is`, `typeOf`)?
- Q65. Which number helpers should you name?
- Q66. How do you handle timezones?
- Q67. What is in `dw::core::Dates` / `Periods`?
- Q68. How do you `replace`, `find`, and split SKUs with Strings helpers?
- Q69. How does Transform Message set payload **and** variables?
- Q70. When is `application/java` the payload type?
- Q71. What is `readUrl` vs `read`?
- Q72. How do you debug DataWeave (`log`, `application/dw`)?
- Q73. DataWeave `try` vs Mule On Error?
- Q74. Which HTTP `attributes` should you memorize?
- Q75. Default XML namespaces, CDATA, mixed content?
- Q76. YAML, Excel, and flat file — does DataWeave do them?
- Q77. `dw::util::Values::mask` vs recursive mask?
- Q78. Boolean operators and precedence?
- Q79. How do you sort by two fields (region, then amount desc)?
- Q80. DataWeave vs For Each vs Batch Job vs Java?
