# Whiteboard set (interview bootcamp)

Close solutions. Eight minutes each. Say the header out loud (`%dw 2.0`, `output`, `---`) before the body.

| # | Lab | Skill | Prompt in one sentence |
| --- | --- | --- | --- |
| 23 | `student/labs/02-intermediate/23-expand-order-lines-flatmap/` | `flatMap` | One row per line item with `orderId` and `sku`. |
| 20 | `student/labs/02-intermediate/20-total-amount-per-customer/` | `groupBy` + `sum` | `{ customerId, total }` per customer. |
| 32 | `student/labs/02-intermediate/32-join-without-leftjoin-groupby-lookup/` | lookup index | Left-join orders to customers **without** `leftJoin`. |
| 39 | `student/labs/03-advanced/39-deep-mask-pii-keys-ssn-password-email/` | recursion | Mask `ssn` / `password` / `email` at any depth. |
| 53 | `student/labs/03-advanced/53-build-a-nested-org-chart-from-a-flat-list/` | tree | Flat list + `managerId` → nested `children`. |
| 54 | `student/labs/03-advanced/54-invoice-compute-line-totals-tax-and-grand-total/` | `var` / `do` | Line totals, subtotal, tax, grand total. |

## Extra prompts (no dedicated lab file)

1. Nested JSON orders → CSV of line items (`output application/csv header=true`).
2. Employees by department, average salary.
3. Deep-merge two configs; concatenate arrays on key collision (describe rules, then code).

## How to run this as a Udemy lecture

1. Screen: timer + empty Playground.
2. Student voiceover optional: “Pause and try.”
3. After 8 minutes, paste **only** the input, then type the solution from `instructor/solutions`.
4. End with Q60 talk-through (namespaced XML → canonical JSON) from `sections/12-interview-bootcamp/LECTURE.md`.
