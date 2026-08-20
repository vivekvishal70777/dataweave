%dw 2.0
output application/json
fun applyPatch(base, patch) =
  if (patch == null) null
  else if ((patch is Object) and (base is Object)) do {
    var keys = (namesOf(base) ++ namesOf(patch)) distinctBy $
    ---
    keys reduce ((k, acc = {}) ->
      if (namesOf(patch) contains k)
        (if (patch[k] == null) acc else acc ++ { (k): applyPatch(base[k], patch[k]) })
      else acc ++ { (k): base[k] }
    )
  }
  else patch
fun diffs(a, b, path) =
  if (a == b) []
  else if ((a is Object) and (b is Object)) do {
    var keys = (namesOf(a) ++ namesOf(b)) distinctBy $
    ---
    keys flatMap ((k) -> diffs(a[k], b[k], if (path == "") (k as String) else path ++ "." ++ (k as String)))
  }
  else [{ path: path, from: a default null, to: b default null }]
var result = applyPatch(payload.base, payload.patch)
---
{
  result: result,
  changed: diffs(payload.base, result, "") orderBy $.path
}
