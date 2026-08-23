# Lab 41 — SOAP namespaced purchase order to canonical JSON

**Level:** hard  
**Section folder:** `03-advanced`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Strip SOAP envelope, read `ord:PurchaseOrder` attributes and repeating `ord:Line` attributes. Two prefixes. This is a standard hard XML interview.

**Input:**

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ord="http://acme.com/order">
  <soap:Body>
    <ord:PurchaseOrder id="PO-1001" currency="INR">
      <ord:Line sku="SKU-A" qty="2" unitPrice="50.00"/>
      <ord:Line sku="SKU-B" qty="1" unitPrice="100.00"/>
    </ord:PurchaseOrder>
  </soap:Body>
</soap:Envelope>
```

**Expected:**

```json
{
  "orderId": "PO-1001",
  "currency": "INR",
  "lines": [
    { "sku": "SKU-A", "qty": 2, "unitPrice": 50.00 },
    { "sku": "SKU-B", "qty": 1, "unitPrice": 100.00 }
  ]
}
```

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
