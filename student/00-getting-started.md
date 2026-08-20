# Getting started (students)

This is a **practice-first** DataWeave 2.0 course. Every coding lecture has a starter file. Watch the concept, **pause**, try the lab, then resume for the solution walkthrough.

## What you need

- Browser: [DataWeave Playground](https://dataweave.mulesoft.com/learn/) (enough for almost every lab), **or**
- [Anypoint Studio](https://www.mulesoft.com/platform/studio) / Anypoint Code Builder with a Mule 4 project and a **Transform Message** component.

Optional: Mule runtime **4.3+** for the `update` operator and newer Array helpers (`drop`, `take`, `divideBy`, `leftJoin`).

## Lab ritual (use this every time)

1. Open `student/labs/…/README.md` and read the problem.
2. Copy the sample input. Set MIME type to `application/json` unless the lab says XML or CSV.
3. Replace the `// TODO` body in `transform.dwl`. Leave the `%dw 2.0` / `output` header unless the lab needs XML/CSV output.
4. Compare your result to **Expected**.
5. Only then look at `instructor/solutions/…/solution.dwl` (if your instructor published solutions) or the solution video.

Cover the expected output with a sticky note if you are tempted to skip the attempt.

## MIME types you will use

| Output line | When |
| --- | --- |
| `output application/json` | Default |
| `output application/xml` | XML root element required |
| `output application/csv header=true` | Spreadsheet-style export |

## If the script fails

- `+` vs `++`: `+` is numeric; strings and arrays use `++`.
- Missing field: use `default` or `?`, not Java `== null` checks only.
- XML: one root; attributes are `.@id`.
- Coercion error on `"10"`: `as Number`. Coercion that might fail: `try` / `orElse`.

## Course order

Follow the section numbers in the Udemy curriculum. Do not jump to advanced recursion or **production** labs (55–82) until you can `map` / `filter` / `groupBy` without notes.

Next: [Lab index](labs/README.md).
