from pathlib import Path
import json, zipfile
root = Path(__file__).resolve().parent
manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8-sig'))
plugin = 'id' in manifest
folder = manifest['id'] if plugin else manifest['name']
slug = folder.lower().replace(' ', '-')
files = ['manifest.json', 'main.js', 'styles.css'] if plugin else ['manifest.json', 'theme.css']
files += [p for p in ['LICENSE', 'NOTICE.md'] if (root / p).is_file()]
if (root / 'licences').exists():
    files += [p.relative_to(root).as_posix() for p in (root / 'licences').rglob('*') if p.is_file()]
else:
    files += [p for p in ['fonts/OFL-EBGaramond.txt', 'fonts/archivo/OFL-Archivo.txt', 'fonts/nimbus/COPYING', 'fonts/nimbus/LICENSE'] if (root / p).is_file()]
output = root / 'downloads' / (slug + '.zip')
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name in sorted(files):
        info = zipfile.ZipInfo(folder + '/' + name, (1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, (root / name).read_bytes())
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == {folder + '/' + name for name in files}
    for name in files:
        assert archive.read(folder + '/' + name) == (root / name).read_bytes()
print(f'{output.name}: {output.stat().st_size:,} bytes; {len(files)} verified files')
