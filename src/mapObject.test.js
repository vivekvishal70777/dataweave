import assert from "node:assert/strict";
import test from "node:test";
import { mapObject } from "./mapObject.js";

test("transforms every value and keeps the original keys", () => {
  const cart = { apple: 2, bread: 3, milk: 4 };
  const doubled = mapObject(cart, (price) => price * 2);

  assert.deepEqual(doubled, { apple: 4, bread: 6, milk: 8 });
  assert.deepEqual(cart, { apple: 2, bread: 3, milk: 4 });
});

test("passes the value, key, and source object to the operation", () => {
  const calls = [];
  const source = { a: 1, b: 2 };

  mapObject(source, (value, key, object) => {
    calls.push([value, key, object]);
    return `${key}:${value}`;
  });

  assert.deepEqual(calls, [
    [1, "a", source],
    [2, "b", source],
  ]);
});

test("returns an empty object for an empty input", () => {
  assert.deepEqual(mapObject({}, () => 1), {});
});

test("rejects non-objects and missing operations", () => {
  assert.throws(() => mapObject(null, (value) => value), TypeError);
  assert.throws(() => mapObject([1, 2], (value) => value), TypeError);
  assert.throws(() => mapObject({ a: 1 }, "nope"), TypeError);
});
