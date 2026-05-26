#!/usr/bin/env python3
"""Build a Kodi-installable ZIP for the RadioHY addon.

Output: script.audio.radiohy-<version>.zip
Files are placed at the ZIP root (no top-level folder).
"""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ADDON_XML = ROOT / 'addon.xml'

EXCLUDE_NAMES = {
    '.git', '.claude', '.vscode', '.gitignore',
    '__pycache__', 'skins',
    'make_zip.py', 'copy_files.py', 'test.py', 'TODO.txt', 'README.md', 'stations.json',
}
EXCLUDE_SUFFIXES = {'.pyc', '.pyo', '.zip'}
EXCLUDE_PATHS = {
    ROOT / 'resources' / 'lib' / 'export_json.py',
}


def parse_addon_meta():
    text = ADDON_XML.read_text(encoding='utf-8')
    m = re.search(r'<addon\b[^>]*\bid=["\']([^"\']+)["\'][^>]*\bversion=["\']([^"\']+)["\']', text)
    addon_id = m.group(1)
    version = m.group(2)
    return addon_id, version


def collect_files():
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        if any(part in EXCLUDE_NAMES for part in path.parts):
            continue
        if path.suffix in EXCLUDE_SUFFIXES:
            continue
        if path in EXCLUDE_PATHS:
            continue
        yield path


def main():
    addon_id, version = parse_addon_meta()
    zip_name = f'{addon_id}-{version}.zip'
    zip_path = ROOT / zip_name

    files = list(collect_files())

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            arcname = file.relative_to(ROOT)
            zf.write(file, arcname)
            print(f'  + {arcname}')

    print(f'\nCreated {zip_name} ({zip_path.stat().st_size // 1024} KB, {len(files)} files)')


if __name__ == '__main__':
    sys.exit(main())
