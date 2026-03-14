#!/bin/bash
set -euo pipefail

echo "Checking Git LFS files..."

MISSING=()
while IFS= read -r -d '' file; do
  if ! git lfs ls-files --error-log=git-lfs.log "$file" >/dev/null 2>&amp;1; then
    MISSING+=("$file")
  fi
done < <(git ls-files -z)

if [ ${#MISSING[@]} -ne 0 ]; then
  echo "❌ Missing LFS tracking for:"
  printf '%s\n' "${MISSING[@]}"
  exit 1
fi

echo "✅ All large files tracked by Git LFS."
exit 0

