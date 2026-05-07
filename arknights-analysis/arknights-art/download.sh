#!/usr/bin/env bash
set -u
cd "$(dirname "$0")"

declare -A GALLERIES=(
  ["YtFQp0x"]="怀黍离"
  ["fDbK60r"]="星语共愿"
  ["MR7hqqJ"]="罗小黑联动"
  ["wLSyf58"]="迷宫饭联动"
)

UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'

for gid in "${!GALLERIES[@]}"; do
  name="${GALLERIES[$gid]}"
  outdir="$name"
  mkdir -p "$outdir"
  echo "=== $name ($gid) ==="

  # Extract thumbnail detail-page slugs from gallery HTML.
  slugs=$(grep -oE 'https://postimg\.cc/[A-Za-z0-9]{6,10}' "_gallery_$gid.html" \
          | grep -v '/gallery' | sort -u)

  i=0
  for slug_url in $slugs; do
    i=$((i+1))
    slug="${slug_url##*/}"

    # Fetch detail page; extract the ?dl=1 download URL.
    detail=$(curl -sA "$UA" "$slug_url")
    dl=$(echo "$detail" | grep -oE 'https://i\.postimg\.cc/[^"]+\?dl=1' | head -1)

    if [[ -z "$dl" ]]; then
      echo "  [$i] $slug: NO DOWNLOAD URL FOUND"
      continue
    fi

    # Strip ?dl=1 to get the canonical image URL; derive filename.
    img_url="${dl%\?dl=1}"
    fname="${img_url##*/}"
    out="$outdir/${i}_${fname}"

    if [[ -f "$out" ]]; then
      echo "  [$i] exists: $out"
      continue
    fi

    # Use ?dl=1 to force download; -L follows redirects.
    if curl -sLA "$UA" -o "$out" "$dl"; then
      size=$(stat -c%s "$out" 2>/dev/null || stat -f%z "$out")
      echo "  [$i] $fname ($size bytes)"
    else
      echo "  [$i] FAILED: $slug"
      rm -f "$out"
    fi
  done
done
