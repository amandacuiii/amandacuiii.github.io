#!/usr/bin/env python3
"""
Extracts base64-encoded images from pottery-data.json into photos/pottery/,
replacing them with file paths. Skips images that are already file paths.
"""
import json, base64, os, re

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SITE_DIR, 'pottery-data.json')
OUT_DIR   = os.path.join(SITE_DIR, 'photos', 'pottery')

os.makedirs(OUT_DIR, exist_ok=True)

with open(JSON_PATH) as f:
    data = json.load(f)

def safe_name(name):
    return re.sub(r'[^a-zA-Z0-9]+', '-', (name or 'piece')).strip('-').lower()[:40]

def next_index():
    """Find the next available index by scanning existing files."""
    existing = [f for f in os.listdir(OUT_DIR) if re.match(r'^\d{3}-', f)]
    if not existing:
        return 1
    indices = [int(f[:3]) for f in existing]
    return max(indices) + 1

idx = next_index()
extracted = 0

for piece in data:
    piece_slug = safe_name(piece.get('name', ''))

    def extract(b64_str, suffix=''):
        global idx, extracted
        if not b64_str or not b64_str.startswith('data:image'):
            return b64_str  # already a path or empty, leave as-is
        header, b64data = b64_str.split(',', 1)
        ext = 'png' if 'png' in header else 'jpg'
        fname = f'{idx:03d}-{piece_slug}{suffix}.{ext}'
        # Avoid overwriting existing files
        while os.path.exists(os.path.join(OUT_DIR, fname)):
            fname = f'{idx:03d}-{piece_slug}{suffix}-x.{ext}'
            break
        with open(os.path.join(OUT_DIR, fname), 'wb') as f:
            f.write(base64.b64decode(b64data))
        idx += 1
        extracted += 1
        return f'photos/pottery/{fname}'

    piece['mainImage'] = extract(piece.get('mainImage', ''))

    new_progress = []
    for j, pp in enumerate(piece.get('progressPhotos') or []):
        new_progress.append(extract(pp, f'-p{j+1}'))
    piece['progressPhotos'] = new_progress

with open(JSON_PATH, 'w') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

if extracted:
    print(f'✅ Extracted {extracted} images → photos/pottery/')
else:
    print('✅ No new images to extract (all pieces already use file paths)')

size_kb = os.path.getsize(JSON_PATH) / 1024
print(f'📄 pottery-data.json: {size_kb:.1f} KB')
