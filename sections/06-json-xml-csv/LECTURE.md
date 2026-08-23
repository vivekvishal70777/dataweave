# Section — JSON, XML, and CSV mappings

Use this file as the **article lecture** and recording outline on Udemy.

## Learning objectives

- Change `output` MIME type and produce a single XML root.
- Read and write XML attributes.
- Round-trip CSV with headers and number coercion.

## Suggested video breakdown

- JSON to XML (single root). SOAP/namespaces wait until the advanced section.
- Stress: XML needs one root; CSV keys become headers.

## Labs in this section

Student starters live under `student/labs/`.

- Lab 11
- Lab 12
- Lab 29
- Lab 30

## Teach these interview questions

### Q14. How do you transform JSON to XML (and vice versa)?

**Answer:** Change the `output` MIME type and shape the tree:

```dataweave
%dw 2.0
output application/xml
---
orders: {
  order: payload map {
    id: $.id,
    amount: $.amount
  }
}
```

JSON to XML needs a **single root**. XML to JSON is the reverse: `output application/json` and select elements/attributes (`payload.orders.order.@id` for attributes).

---

### Q31. How do you transform CSV to JSON?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
payload map {
  name: $.Name,
  amount: $.Amount as Number
}
```

CSV is typically read as an **array of objects** (header row = keys). Reader properties: `header=true`, `separator=";"`, `quoteValues=true`.

---

### Q32. How do you generate CSV from JSON?

**Answer:**

```dataweave
%dw 2.0
output application/csv header=true, separator=","
---
payload map {
  OrderId: $.id,
  Total: $.amount
}
```

Keys become column headers when `header=true`.

---

### Q33. How do you read XML attributes vs elements?

**Answer:**

```dataweave
%dw 2.0
output application/json
---
{
  id: payload.order.@id,           // attribute
  name: payload.order.customer,    // element text / child
  items: payload.order.*item       // repeating child elements
}
```

To **write** attributes:

```dataweave
order @(id: payload.id): {
  customer: payload.name
}
```

---
