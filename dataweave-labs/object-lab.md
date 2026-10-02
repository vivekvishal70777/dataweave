# DataWeave Lab: Objects

Five practice questions on DataWeave objects (`%dw 2.0`).

Each solution uses one or more of these core functions:

| Function | Input | Output | Lambda arguments |
| --- | --- | --- | --- |
| `mapObject` | Object | Object | `(value, key, index)` |
| `pluck` | Object | Array | `(value, key, index)` |
| `map` | Array | Array | `(item, index)` |

`mapObject` rebuilds an object. `pluck` turns each key/value pair into an array element. `map` transforms each element of an array (including an array of objects, or the array `pluck` just produced).

Object keys in DataWeave are type `Key`. Cast with `as String` when you concatenate a key or store it in a field. A dynamic key is wrapped in parentheses: `{(key): value}`.

Paste any script into the [DataWeave Playground](https://dataweave.mulesoft.com/) or a Transform Message in Anypoint Studio. Set the sample input as the payload (`application/json`).

---

## Question 1 — Rebuild an object with `mapObject`

A catalog service returns each SKU as a key. The integration needs every key uppercased, a 10% list-price markup, and the original price kept beside the new price.

**Input**

```json
{
  "pen": { "price": 100, "currency": "USD" },
  "notebook": { "price": 250, "currency": "USD" },
  "eraser": { "price": 50, "currency": "USD" }
}
```

**Expected output**

```json
{
  "PEN": { "price": 100, "listPrice": 110, "currency": "USD" },
  "NOTEBOOK": { "price": 250, "listPrice": 275, "currency": "USD" },
  "ERASER": { "price": 50, "listPrice": 55, "currency": "USD" }
}
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload mapObject ((item, sku) -> {
  (upper(sku as String)): {
    price: item.price,
    listPrice: item.price * 11 / 10,
    currency: item.currency
  }
})
```

**Why this works**

`mapObject` visits every pair. `item` is the value (`{ price, currency }`) and `sku` is the key. `(upper(sku as String))` builds a new key. The value is a new object, so the original payload is left unchanged. `price * 11 / 10` is the 10% markup (`100 → 110`, `250 → 275`, `50 → 55`).

---

## Question 2 — Turn an object into an array with `pluck`

An employee directory is keyed by employee id. A downstream API wants a JSON array, with the id copied into each record as `empId`.

**Input**

```json
{
  "E01": { "name": "Asha", "dept": "IT" },
  "E02": { "name": "Ravi", "dept": "HR" },
  "E03": { "name": "Mei", "dept": "IT" }
}
```

**Expected output**

```json
[
  { "empId": "E01", "name": "Asha", "dept": "IT" },
  { "empId": "E02", "name": "Ravi", "dept": "HR" },
  { "empId": "E03", "name": "Mei", "dept": "IT" }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload pluck ((employee, id) -> {
  empId: id as String,
  name: employee.name,
  dept: employee.dept
})
```

**Why this works**

`pluck` walks the object the same way `mapObject` does, but collects the lambda results into an array. Promoting `id` into the body is the usual way to flatten a map-style object into records. Order follows the object’s key order.

---

## Question 3 — Transform an array of objects with `map`

Order lines arrive as an array. Produce a customer summary: uppercase the item name and add `lineTotal` (`qty * price`). Drop `qty` and `price` from the output.

**Input**

```json
[
  { "orderId": "O100", "item": "pen", "qty": 3, "price": 10 },
  { "orderId": "O101", "item": "notebook", "qty": 2, "price": 25 },
  { "orderId": "O102", "item": "eraser", "qty": 4, "price": 5 }
]
```

**Expected output**

```json
[
  { "orderId": "O100", "item": "PEN", "lineTotal": 30 },
  { "orderId": "O101", "item": "NOTEBOOK", "lineTotal": 50 },
  { "orderId": "O102", "item": "ERASER", "lineTotal": 20 }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload map ((order) -> {
  orderId: order.orderId,
  item: upper(order.item),
  lineTotal: order.qty * order.price
})
```

**Why this works**

`map` is the array counterpart of `mapObject`. Each `order` is one object. Returning a fresh object selects and computes fields; fields you omit (`qty`, `price`) disappear from that element.

---

## Question 4 — Filter with `mapObject`, then list with `pluck`

User accounts are stored as an object. Inactive accounts must be removed, and the remaining accounts must be returned as an array of `{ userId, name, role }`.

**Input**

```json
{
  "u1": { "name": "Asha", "active": true, "role": "admin" },
  "u2": { "name": "Ravi", "active": false, "role": "viewer" },
  "u3": { "name": "Mei", "active": true, "role": "editor" }
}
```

**Expected output**

```json
[
  { "userId": "u1", "name": "Asha", "role": "admin" },
  { "userId": "u3", "name": "Mei", "role": "editor" }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
payload mapObject ((user, id) ->
  if (user.active)
    { (id): user }
  else
    {}
) pluck ((user, id) -> {
  userId: id as String,
  name: user.name,
  role: user.role
})
```

**Why this works**

`mapObject` merges whatever object the lambda returns. Returning `{}` for Ravi adds no key, so that account is dropped. Returning `{ (id): user }` keeps the original key. `mapObject` and `pluck` are left-associative, so the filtered object is what `pluck` receives. `pluck` then promotes each surviving key to `userId`.

---

## Question 5 — `map`, `mapObject`, and `pluck` together

Each department is one element of an array. Staff inside a department is an object keyed by employee id. Return one flat array of people. Uppercase each name, add `bonus` as 10% of `salary`, and include the department name on every row.

**Input**

```json
[
  {
    "department": "IT",
    "staff": {
      "E01": { "name": "Asha", "salary": 100 },
      "E02": { "name": "Ravi", "salary": 80 }
    }
  },
  {
    "department": "HR",
    "staff": {
      "E03": { "name": "Mei", "salary": 90 }
    }
  }
]
```

**Expected output**

```json
[
  { "empId": "E01", "name": "ASHA", "department": "IT", "salary": 100, "bonus": 10 },
  { "empId": "E02", "name": "RAVI", "department": "IT", "salary": 80, "bonus": 8 },
  { "empId": "E03", "name": "MEI", "department": "HR", "salary": 90, "bonus": 9 }
]
```

**Solution**

```dataweave
%dw 2.0
output application/json
---
flatten(
  payload map ((dept) ->
    dept.staff mapObject ((person, id) -> {
      (id): {
        name: upper(person.name),
        salary: person.salary,
        bonus: person.salary * 10 / 100
      }
    }) pluck ((person, id) -> {
      empId: id as String,
      name: person.name,
      department: dept.department,
      salary: person.salary,
      bonus: person.bonus
    })
  )
)
```

**Why this works**

1. `map` walks the department array. The lambda closes over `dept`, so `dept.department` is still in scope while staff is rewritten.
2. `mapObject` rebuilds that department’s `staff` object: the key stays the employee id, the name is uppercased, and `bonus` is `salary * 10 / 100`.
3. `pluck` turns the rebuilt staff object into an array of flat records.
4. `map` therefore returns an array of arrays (`[[E01, E02], [E03]]`). `flatten` joins them into one array.

---

## Quick reference

```dataweave
%dw 2.0
output application/json
---
{
  // Object -> Object. Rename a key and change its value.
  mapped: { a: 1, b: 2 } mapObject ((value, key) -> {
    (upper(key as String)): value * 10
  }),
  // Object -> Array. One element per pair.
  plucked: { a: 1, b: 2 } pluck ((value, key) -> {
    key: key as String,
    value: value
  }),
  // Array of objects -> Array of objects.
  mappedArray: [{ n: "ada" }, { n: "grace" }] map ((row) -> {
    name: upper(row.n)
  })
}
```

That script evaluates to:

```json
{
  "mapped": { "A": 10, "B": 20 },
  "plucked": [
    { "key": "a", "value": 1 },
    { "key": "b", "value": 2 }
  ],
  "mappedArray": [
    { "name": "ADA" },
    { "name": "GRACE" }
  ]
}
```
