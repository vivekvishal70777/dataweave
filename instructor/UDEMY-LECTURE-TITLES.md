# Paste-ready Udemy lecture titles

Create **sections** first (names match `UDEMY-LISTING.md`). Then add these lectures in order. Mark type: Video / Article / Quiz.

## Section 1 — Welcome and setup

1. Welcome and what you will build — Video  
2. How this course works (concept, pause, lab, quiz) — Video  
3. Getting started: Playground vs Transform Message — Article (`student/00-getting-started.md`)  
4. Easy tutorials (plain language) — Articles (`student/tutorials/01-welcome-and-setup/`)  
5. Tour of the student lab folder — Video  

Easy tutorials live in `student/tutorials/<section-id>/` — **one markdown file per topic**. On Udemy, either paste each file as its own Article, or attach the section folder as a resource next to the first video.

## Section 2 — DataWeave 2.0 fundamentals

Easy tutorials: `student/tutorials/02-dataweave-fundamentals/` (7 topics).

5. What is DataWeave in Mule 4? — Video  
6. DataWeave 1.0 vs 2.0 — Video  
7. Script structure: header, output, body — Video  
8. Variables, functions, types, and `as` — Video  
9. Labs 03, 05, 08, 13 (pause and try) — Video  
10. Quiz: Fundamentals — Practice test  

## Section 3 — Arrays

Easy tutorials: `student/tutorials/03-arrays-and-core-operators/` (4 topics).

11. `map`, `filter`, `$` and `$$` — Video  
12. `sizeOf`, `isEmpty`, `flatten` — Video  
13. Labs 01–02 demo; homework 09, 10, 14, 15 — Video  
14. Quiz: Arrays — Practice test  

## Section 4 — Objects, nulls, selectors

Easy tutorials: `student/tutorials/04-objects-nulls-and-selectors/` (5 topics).

15. Selectors: `.` `[]` `.*` `..` — Video  
16. `default`, `?`, and `skipNullOn` — Video  
17. `mapObject` and `pluck` — Video  
18. Labs 04, 05, 16, 18 — Video  
19. Quiz: Objects — Practice test  

## Section 5 — Strings, numbers, conditionals

Easy tutorials: `student/tutorials/05-strings-numbers-conditionals/` (4 topics).

20. `++` vs `+`; split, join, case — Video  
21. if/else expressions (no Java ternary) — Video  
22. Labs 06, 07, 08, 13, 17 — Video  
23. Quiz: Strings and conditionals — Practice test  

## Section 6 — JSON, XML, CSV

Easy tutorials: `student/tutorials/06-json-xml-csv/` (4 topics).

24. JSON to XML (single root) — Video  
25. XML attributes and repeating elements — Video  
26. CSV to JSON and JSON to CSV — Video  
27. Labs 11, 12, 29, 30 — Video  
28. Quiz: Formats — Practice test  

## Section 7 — Intermediate transforms

Easy tutorials: `student/tutorials/07-intermediate-transforms/` (7 topics).

29. `groupBy`, `orderBy`, `distinctBy` — Video  
30. `reduce` and building objects — Video  
31. `flatMap` line items (Lab 23) — Video  
32. Merge, `update`, and `do` — Video  
33. Homework recap: totals per customer (Lab 20) — Video  
34. Quiz: Intermediate — Practice test  

## Section 8 — Dates, match, try

Easy tutorials: `student/tutorials/08-dates-match-and-errors/` (3 topics).

35. Dates, formats, and periods — Video  
36. `match` and `try` / `orElse` — Video  
37. Labs 27, 28, 33, 52 — Video  
38. Quiz: Dates, match, try — Practice test  

## Section 9 — Joins, modules, Mule context

Easy tutorials: `student/tutorials/09-joins-modules-mule-context/` (7 topics).

39. `vars`, `attributes`, and properties — Video  
40. Modules and Transform Message vs `#[...]` — Video  
41. `leftJoin` vs `groupBy` lookup (Labs 31–32) — Video  
42. Why not `lookup` or Java inside every `map` — Video  
43. Quiz: Joins and Mule — Practice test  

## Section 10 — Advanced

Easy tutorials: `student/tutorials/10-advanced-recursion-and-xml-ns/` (13 topics).

44. Recursion and `match` on types — Video  
45. Deep PII mask (Lab 39) — Video  
46. XML namespaces read and write — Video  
47. Dynamic keys, diffs, last-wins dedupe — Video  
48. Capstone invoice (Lab 54) and org chart (Lab 53) — Video  
49. Quiz: Advanced — Practice test  

## Section 11 — Production

Easy tutorials: `student/tutorials/11-performance-and-production/` (6 topics).

50. Streaming: what breaks it — Video  
51. Crypto, binary, reader/writer properties — Video  
52. Reusable `.dwl` modules and performance pitfalls — Video  
53. Quiz: Production — Practice test  

## Section 12 — Industry operators, message, and MIME

Easy tutorials: `student/tutorials/13-industry-operators-and-mule-message/` (20 topics).

59. Arrays helpers: `maxBy`, `firstWith`, `zip`, ranges — Video  
60. Types, money, timezones, `dw::core::Dates` — Video  
61. Transform Message targets, Java MIME, `readUrl`, HTTP attributes — Video  
62. XML ns extras, Excel/YAML/flat file, DW vs Batch — Video  
63. Labs 55–58 — Video (or four lab videos)  
64. Quiz: Industry message / MIME — Practice test  

## Section 13 — Interview bootcamp

This section is **practice**, not a replay of Q1–80. Those questions were already taught in sections 2–12.

Easy tutorials: `student/tutorials/12-interview-bootcamp/` (drill, whiteboard, Q60).

54. How to drill the 80-question bank — Article (attach `reference/MuleSoft-DataWeave-Interview-Questions.md`)  
55. Verbal mock interview (8 mixed questions, 60-second answers) — Video  
56. Whiteboard mock interview (3 of the 6 signature labs) — Video  
57. Nested XML to canonical JSON (Q60 design talk only) — Video  
58. Final practice test — Practice test  
59. Next steps and solutions pack (optional download) — Video  

Attach `student/` zips on lab lectures. Attach solutions only on the last lecture (or omit and keep solutions off Udemy).
