#!/usr/bin/env bash
# Build the student resource zip for Udemy (no instructor solutions or answer keys).
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-"$root/dist/dataweave-udemy-student-resources.zip"}"
mkdir -p "$(dirname "$out")"
rm -f "$out"
(
  cd "$root"
  zip -r "$out" \
    README.md \
    student \
    sections \
    -x "*.DS_Store"
)
echo "Wrote $out"
