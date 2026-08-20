# Lab 65 — Wrap a domain payload as CloudEvents 1.0

**Level:** production  
**Section folder:** `04-production`

## Try this first

1. Open DataWeave Playground or Transform Message.
2. Set the input MIME type to match the sample (JSON unless stated otherwise).
3. Paste `input` into the payload.
4. Complete `transform.dwl`. Do not open the instructor solution until you have an attempt.

## Problem

**Problem:** Produce a CloudEvents-like envelope. Use `payload.now` (injected; never `now()` in tests). `id` = `eventId`. `data` is the domain object without envelope fields.

**Input:**

```json
{
  "eventId": "e-100",
  "now": "2026-08-20T08:00:00Z",
  "source": "urn:mule:orders",
  "type": "com.acme.order.created",
  "orderId": "O-1",
  "amount": 99
}
```

**Expected:**

```json
{
  "specversion": "1.0",
  "id": "e-100",
  "source": "urn:mule:orders",
  "type": "com.acme.order.created",
  "time": "2026-08-20T08:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "orderId": "O-1",
    "amount": 99
  }
}
```

**Interview talking point:** Inject clocks and UUIDs as **parameters** so modules stay testable. Kafka/Anypoint MQ headers often duplicate `id` / `type`.

**Solution:** Hidden until you try it. See `instructor/solutions`.

## Files

| File | Role |
| --- | --- |
| `transform.dwl` | Your script (starter) |
| `input.json` / `input.txt` | Sample payload |
| Instructor `solution.dwl` | Reference after you try |
