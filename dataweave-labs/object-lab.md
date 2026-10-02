# DataWeave Lab: Objects

Five practice questions on DataWeave objects (`%dw 2.0`).

Every solution uses all three functions in one script:

| Function | Input | Output | Lambda arguments |
| --- | --- | --- | --- |
| `map` | Array | Array | `(item, index)` |
| `mapObject` | Object | Object | `(value, key, index)` |
| `pluck` | Object | Array | `(value, key, index)` |

They share the same precedence and are left-associative, so this groups as `((obj mapObject f) pluck g) map h`:

```dataweave
obj mapObject ((value, key) -> { (key): value }) pluck ((value, key) -> value) map ((item) -> item)
```

Object keys are type `Key`. Cast with `as String` before concatenating a key or storing it. A dynamic key is wrapped in parentheses: `{(key): value}`. Returning `{}` from `mapObject` drops that pair.

Paste any script into the [DataWeave Playground](https://dataweave.mulesoft.com/) with the sample payload as `application/json`.

---

## Question 1 — Flat invoice lines

Each order is an array element. Its `items` field is an object keyed by SKU. Build one flat array of lines. Uppercase the SKU and set `lineTotal` to `qty * price`.

**Input**

```json
[
  {
    "orderId": "O100",
    "items": {
      "pen": { "qty": 2, "price": 10 },
      "notebook": { "qty": 1, "price": 25 }
    }
  },
  {
    "orderId": "O101",
    "items": {
      "eraser": { "qty": 4, "price": 5 }
    }
  }
]
```

**Expected output**

```json
[
  { "orderId": "O100", "sku": "PEN", "qty": 2, "lineTotal": 20 },
  { "orderId": "O100", "sku": "NOTEBOOK", "qty": 1, "lineTotal": 25 },
  { "orderId": "O101", "sku": "ERASER", "qty": 4, "lineTotal": 20 }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
flatten(
  payload map ((order) ->
    order.items mapObject ((item, sku) -> {
      (sku): {
        qty: item.qty,
        lineTotal: item.qty * item.price
      }
    }) pluck ((item, sku) -> {
      orderId: order.orderId,
      sku: upper(sku as String),
      qty: item.qty,
      lineTotal: item.lineTotal
    })
  )
)
```

**How the three functions combine**

- `map` walks the order array. `order.orderId` stays in scope for every line of that order.
- `mapObject` rebuilds `items`: the SKU key is unchanged, and the value gains `lineTotal`.
- `pluck` turns that object into an array of flat line records.
- `map` therefore yields an array of arrays. `flatten` joins them into one list.

---

## Question 2 — Passed subjects for each student

Each student has a `scores` object keyed by subject. Keep subjects with a score of at least 40. Grade `A` when the score is at least 75, otherwise grade `B`. Return one object per student, with `passed` as an array.

**Input**

```json
[
  {
    "name": "Asha",
    "scores": { "math": 80, "science": 35, "english": 70 }
  },
  {
    "name": "Ravi",
    "scores": { "math": 40, "science": 90, "english": 30 }
  }
]
```

**Expected output**

```json
[
  {
    "student": "Asha",
    "passed": [
      { "subject": "MATH", "score": 80, "grade": "A" },
      { "subject": "ENGLISH", "score": 70, "grade": "B" }
    ]
  },
  {
    "student": "Ravi",
    "passed": [
      { "subject": "MATH", "score": 40, "grade": "B" },
      { "subject": "SCIENCE", "score": 90, "grade": "A" }
    ]
  }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload map ((student) -> {
  student: student.name,
  passed: student.scores mapObject ((score, subject) ->
    if (score >= 40)
      {
        (subject): {
          score: score,
          grade: if (score >= 75) "A" else "B"
        }
      }
    else
      {}
  ) pluck ((row, subject) -> {
    subject: subject as String,
    score: row.score,
    grade: row.grade
  }) map ((row) -> {
    subject: upper(row.subject),
    score: row.score,
    grade: row.grade
  })
})
```

**How the three functions combine**

- The outer `map` builds one result object per student.
- `mapObject` keeps passing scores and attaches `grade`. A failing subject returns `{}`, so that key is removed.
- `pluck` turns the remaining subject object into an array.
- The inner `map` uppercases each subject name on that array.

---

## Question 3 — Reorder list per warehouse

Each warehouse has an `inventory` object of SKU to quantity on hand. A SKU needs a reorder when quantity is below 10. `reorderQty` is `10 - onHand`. Keep one object per warehouse. `reorders` is the array of SKUs that need a reorder.

**Input**

```json
[
  {
    "warehouse": "BLR",
    "inventory": { "pen": 4, "notebook": 20, "eraser": 8 }
  },
  {
    "warehouse": "DEL",
    "inventory": { "pen": 15, "notebook": 3 }
  }
]
```

**Expected output**

```json
[
  {
    "warehouse": "BLR",
    "reorders": [
      { "sku": "PEN", "onHand": 4, "reorderQty": 6 },
      { "sku": "ERASER", "onHand": 8, "reorderQty": 2 }
    ]
  },
  {
    "warehouse": "DEL",
    "reorders": [
      { "sku": "NOTEBOOK", "onHand": 3, "reorderQty": 7 }
    ]
  }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload map ((warehouse) -> {
  warehouse: warehouse.warehouse,
  reorders: warehouse.inventory mapObject ((qty, sku) ->
    if (qty < 10)
      { (sku): qty }
    else
      {}
  ) pluck ((qty, sku) -> {
    sku: sku as String,
    onHand: qty
  }) map ((row) -> {
    sku: upper(row.sku),
    onHand: row.onHand,
    reorderQty: 10 - row.onHand
  })
})
```

**How the three functions combine**

- `map` walks warehouses and wraps each result.
- `mapObject` drops SKUs with quantity 10 or more. Survivors stay as `sku -> qty`.
- `pluck` copies each surviving key and quantity into a row.
- The inner `map` uppercases the SKU and computes `reorderQty`.

---

## Question 4 — Customer contact channels

Each customer has a `channels` object keyed by channel type (`email`, `sms`). Normalize the address to lowercase, then publish an array of contacts. `kind` is the channel name in uppercase. `preferred` is true when `priority` is 1.

**Input**

```json
[
  {
    "customerId": "C1",
    "name": "Asha",
    "channels": {
      "email": { "address": "Asha@Example.com", "priority": 1 },
      "sms": { "address": "+91-999", "priority": 2 }
    }
  },
  {
    "customerId": "C2",
    "name": "Ravi",
    "channels": {
      "email": { "address": "Ravi@Example.com", "priority": 2 }
    }
  }
]
```

**Expected output**

```json
[
  {
    "customerId": "C1",
    "name": "Asha",
    "contacts": [
      { "kind": "EMAIL", "address": "asha@example.com", "preferred": true },
      { "kind": "SMS", "address": "+91-999", "preferred": false }
    ]
  },
  {
    "customerId": "C2",
    "name": "Ravi",
    "contacts": [
      { "kind": "EMAIL", "address": "ravi@example.com", "preferred": false }
    ]
  }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload map ((customer) -> {
  customerId: customer.customerId,
  name: customer.name,
  contacts: customer.channels mapObject ((channel, kind) -> {
    (kind): {
      address: lower(channel.address),
      priority: channel.priority
    }
  }) pluck ((channel, kind) -> {
    kind: kind as String,
    address: channel.address,
    priority: channel.priority
  }) map ((contact) -> {
    kind: upper(contact.kind),
    address: contact.address,
    preferred: contact.priority == 1
  })
})
```

**How the three functions combine**

- `map` walks the customer array.
- `mapObject` rebuilds `channels` with a lowercased address and the original priority.
- `pluck` turns each channel into a record and keeps the channel name as `kind`.
- The inner `map` uppercases `kind` and replaces `priority` with the boolean `preferred`.

---

## Question 5 — Skill rows from an employee object

The payload is an object keyed by employee id, so the root value is an object. Each employee has a `skills` object of skill name to level (1 through 5). Keep skills at level 3 or higher. `label` is `"expert"` when the level is at least 5, otherwise `"skilled"`. Return one flat array.

**Input**

```json
{
  "E01": {
    "name": "Asha",
    "skills": { "java": 5, "sql": 2, "dataweave": 4 }
  },
  "E02": {
    "name": "Mei",
    "skills": { "java": 3, "python": 1 }
  }
}
```

**Expected output**

```json
[
  { "empId": "E01", "name": "Asha", "skill": "JAVA", "level": 5, "label": "expert" },
  { "empId": "E01", "name": "Asha", "skill": "DATAWEAVE", "level": 4, "label": "skilled" },
  { "empId": "E02", "name": "Mei", "skill": "JAVA", "level": 3, "label": "skilled" }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
flatten(
  payload pluck ((employee, id) -> {
    empId: id as String,
    name: employee.name,
    skills: employee.skills
  }) map ((employee) ->
    employee.skills mapObject ((level, skill) ->
      if (level >= 3)
        {
          (skill): {
            level: level,
            label: if (level >= 5) "expert" else "skilled"
          }
        }
      else
        {}
    ) pluck ((row, skill) -> {
      empId: employee.empId,
      name: employee.name,
      skill: upper(skill as String),
      level: row.level,
      label: row.label
    })
  )
)
```

**How the three functions combine**

- The outer `pluck` turns the employee object into an array and promotes each employee id to `empId`.
- `map` walks that array. Inside it, `mapObject` drops skills below level 3 and adds `label`.
- The inner `pluck` turns the remaining skills into rows, with the employee fields copied onto each row.
- `flatten` joins each employee’s skill arrays into one list. SQL (level 2) and Python (level 1) are absent.
