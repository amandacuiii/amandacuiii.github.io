#!/usr/bin/env python3
"""
Extracts base64-encoded images from pottery-data.json into pottery/,
replacing them with file paths. Matches by piece ID first, then slug.
"""
import json, base64, os, re

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SITE_DIR, 'pottery-data.json')
OUT_DIR   = SITE_DIR

os.makedirs(OUT_DIR, exist_ok=True)

with open(JSON_PATH) as f:
    data = json.load(f)

def safe_name(name):
    return re.sub(r'[^a-zA-Z0-9]+', '-', (name or 'piece')).strip('-').lower()[:40]

# Build lookup: slug → filename (for reuse)
existing_files = [f for f in os.listdir(OUT_DIR) if re.match(r'^\d{3}-', f)]
slug_map = {}
for f in existing_files:
    key = re.sub(r'^\d{3}-', '', os.path.splitext(f)[0])
    slug_map[key] = f

# Track which slugs have been claimed this run to avoid duplicate reuse
claimed = set()

def next_index():
    if not existing_files:
        return 1
    indices = [int(f[:3]) for f in existing_files if f[:3].isdigit()]
    return max(indices) + 1 if indices else 1

idx = next_index()
extracted = 0
reused = 0

for piece in data:
    piece_slug = safe_name(piece.get('name', ''))

    def extract(b64_str, suffix=''):
        global idx, extracted, reused
        if not b64_str or not b64_str.startswith('data:image'):
            return b64_str  # already a path or empty

        header, b64data = b64_str.split(',', 1)
        ext = 'png' if 'png' in header else 'jpg'
        lookup_key = f'{piece_slug}{suffix}'

        # Reuse existing file only if not already claimed by another piece this run
        if lookup_key in slug_map and lookup_key not in claimed:
            claimed.add(lookup_key)
            reused += 1
            return slug_map[lookup_key]

        # Generate a unique filename
        fname = f'{idx:03d}-{piece_slug}{suffix}.{ext}'
        while os.path.exists(os.path.join(OUT_DIR, fname)):
            idx += 1
            fname = f'{idx:03d}-{piece_slug}{suffix}.{ext}'
        with open(os.path.join(OUT_DIR, fname), 'wb') as f:
            f.write(base64.b64decode(b64data))
        slug_map[lookup_key] = fname
        claimed.add(lookup_key)
        idx += 1
        extracted += 1
        return fname

    piece['mainImage'] = extract(piece.get('mainImage', ''))

    new_progress = []
    for j, pp in enumerate(piece.get('progressPhotos') or []):
        new_progress.append(extract(pp, f'-p{j+1}'))
    piece['progressPhotos'] = new_progress

with open(JSON_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

if extracted:
    print(f'✅ Extracted {extracted} new images, reused {reused} existing → pottery/')
else:
    print(f'✅ No new images (reused {reused} existing files)')

size_kb = os.path.getsize(JSON_PATH) / 1024
print(f'📄 pottery-data.json: {size_kb:.1f} KB')
