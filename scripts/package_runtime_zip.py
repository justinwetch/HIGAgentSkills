"""Build and inspect a deterministic runtime ZIP from a hash-bound approved manifest."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import stat
import tempfile
import zipfile
from pathlib import Path

SKILL_ROOT = 'apple-hig'
DEFAULT_OUTPUT = Path('release/apple-hig.zip')
DEFAULT_MANIFEST = Path('sources/apple-hig-2026-09-12/verification/shipping-manifest-2026-09-27.json')
CORE = {'SKILL.md', 'README.md', 'routing-index.md'}
ENFORCE = 'references/enforce.md'
ENFORCE_SUPPORT = {'references/enforce-format.md', 'scripts/hig_enforce.py', 'scripts/hig_route.py'}
DUO = {'references/duo.md', 'references/duo-checklist.md', 'commands/duo.md'}
REFERENCE_DIR = 'references/hig'
FORBIDDEN_CHARS = set('<>:"|?*')


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_archive_path(path: str) -> None:
    if not isinstance(path, str) or not path or '\\' in path:
        raise ValueError(f'invalid archive path: {path!r}')
    for part in path.split('/'):
        if (part in {'', '.', '..', '__MACOSX'} or part.startswith('.')
                or part.endswith(('.', ' ')) or any(c in FORBIDDEN_CHARS or ord(c) < 32 for c in part)
                or re.fullmatch(r'(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', part)):
            raise ValueError(f'unsafe archive path: {path}')


def read_manifest(path: Path) -> dict:
    manifest = json.loads(path.read_text(encoding='utf-8-sig'))
    if manifest.get('schema_version') != 1 or manifest.get('approval') != 'approved-for-packaging':
        raise ValueError('manifest must be schema 1 and explicitly approved-for-packaging')
    topics = manifest.get('topics', [])
    if not topics or len(set(topics)) != len(topics):
        raise ValueError('manifest needs unique approved topic identities')
    if any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in topics):
        raise ValueError('invalid topic identity')
    expected = CORE | {ENFORCE} | ENFORCE_SUPPORT | DUO | {f'{REFERENCE_DIR}/{t}.md' for t in topics}
    files = manifest.get('files', [])
    paths = [f['path'] for f in files]
    for relative in paths:
        validate_archive_path(relative)
    if len(paths) != len(set(p.casefold() for p in paths)):
        raise ValueError('duplicate or case-colliding manifest paths')
    if set(paths) != expected:
        raise ValueError(f'manifest membership mismatch: missing={sorted(expected-set(paths))}; extra={sorted(set(paths)-expected)}')
    for record in files:
        if not re.fullmatch(r'[0-9a-f]{64}', record.get('sha256', '')):
            raise ValueError(f"missing or invalid hash: {record['path']}")
    return manifest


def build_zip(repo_root: Path, output: Path, manifest: dict) -> None:
    root = repo_root.resolve()
    payload = {}
    output = output.resolve()
    protected = {(root / f['path']).resolve() for f in manifest['files']}
    if output in protected:
        raise ValueError('output would overwrite an approved runtime file')
    # Read and hash every approved byte before writing.
    for record in manifest['files']:
        relative = record['path']
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f'missing or escaped runtime file: {relative}')
        data = path.read_bytes()
        if digest(data) != record['sha256']:
            raise ValueError(f'changed since manifest approval: {relative}')
        payload[f'{SKILL_ROOT}/{relative}'] = data
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=output.name + '.', suffix='.tmp', dir=output.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'w+b') as stream:
            with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for name, data in sorted(payload.items()):
                    info = zipfile.ZipInfo(name, date_time=(2026, 9, 12, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.create_system = 3
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        inspect_zip(temporary, manifest)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)


def inspect_zip(output: Path, manifest: dict) -> dict:
    expected = {f"{SKILL_ROOT}/{f['path']}": f['sha256'] for f in manifest['files']}
    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        for name in names:
            validate_archive_path(name)
        if len(names) != len(set(n.casefold() for n in names)):
            raise ValueError('duplicate or case-colliding ZIP members')
        if set(names) != set(expected):
            raise ValueError('ZIP membership differs from approved manifest')
        for info in archive.infolist():
            if info.create_system != 3 or not stat.S_ISREG(info.external_attr >> 16):
                raise ValueError(f'ZIP member is not an explicit regular file: {info.filename}')
        for name in names:
            if digest(archive.read(name)) != expected[name]:
                raise ValueError(f'ZIP hash mismatch: {name}')
        if archive.testzip() is not None:
            raise ValueError('ZIP CRC failure')
    return {'entries': len(names), 'distilled_count': len(manifest['topics']),
            'sha256': digest(output.read_bytes()), 'membership_and_hashes': 'pass'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--manifest', type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    manifest_path = args.manifest if args.manifest.is_absolute() else root / args.manifest
    output = args.output if args.output.is_absolute() else root / args.output
    if manifest_path.resolve() in {output.resolve(), output.with_suffix(output.suffix + '.tmp').resolve()}:
        raise ValueError('output would overwrite the approved manifest')
    manifest = read_manifest(manifest_path)
    build_zip(root, output, manifest)
    print(json.dumps({'output': str(output), 'manifest_sha256': digest(manifest_path.read_bytes()),
                      **inspect_zip(output, manifest)}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
