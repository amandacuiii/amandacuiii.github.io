#!/bin/bash
# Run this after exporting pottery-data.json from the admin tool.
# It extracts embedded images, updates the JSON, and pushes to GitHub.

set -e

SITE_DIR="$(cd "$(dirname "$0")" && pwd)"
DOWNLOADS=~/Downloads

# Find most recently downloaded pottery-data.json
JSON_SRC=$(ls -t "$DOWNLOADS"/pottery-data.json "$DOWNLOADS"/pottery-data*.json 2>/dev/null | head -1)

if [ -z "$JSON_SRC" ]; then
  echo "❌ No pottery-data.json found in ~/Downloads"
  echo "   Export it from admin.html first, then re-run this script."
  exit 1
fi

echo "📂 Found: $JSON_SRC"
cp "$JSON_SRC" "$SITE_DIR/pottery-data.json"

echo "🖼  Extracting images..."
python3 "$SITE_DIR/extract-pottery-images.py"

echo "📡 Committing and pushing to GitHub..."
cd "$SITE_DIR"
git add pottery-data.json *.jpg *.jpeg *.png 2>/dev/null; true
git commit -m "Update pottery data and images" --allow-empty
git push origin main

echo ""
echo "✅ Done! amandacui.com will update in ~1 minute."
