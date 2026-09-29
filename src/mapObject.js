/**
 * Iterates each own enumerable property of an object, runs an operation
 * on that entry, and returns a new object with the same keys.
 *
 * The input object is not mutated. Keys are visited in insertion order.
 *
 * @template T, R
 * @param {Record<string, T>} object
 * @param {(value: T, key: string, object: Record<string, T>) => R} operation
 * @returns {Record<string, R>}
 */
export function mapObject(object, operation) {
  if (object === null || typeof object !== "object" || Array.isArray(object)) {
    throw new TypeError("mapObject expects a plain object");
  }
  if (typeof operation !== "function") {
    throw new TypeError("mapObject expects an operation function");
  }

  const result = {};
  for (const key of Object.keys(object)) {
    result[key] = operation(object[key], key, object);
  }
  return result;
}
