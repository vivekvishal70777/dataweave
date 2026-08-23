# Lab 79 — Partner catalog XML to JSON products

**Level:** mapping  
**Section folder:** `05-mapping`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Read attributes id and repeating Item. price as Number. Single XML root.

**Input:**

```xml
<Catalog xmlns="http://partner.example/cat">
  <Item id="I1"><Name>Bolt</Name><Price>2.5</Price></Item>
  <Item id="I2"><Name>Nut</Name><Price>0.75</Price></Item>
</Catalog>
```

**Expected:**

```json
[
  { "id": "I1", "name": "Bolt", "price": 2.5 },
  { "id": "I2", "name": "Nut", "price": 0.75 }
]
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
