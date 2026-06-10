"""Build a deterministic runtime-only skill zip."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


SKILL_ROOT = "apple-hig"
DEFAULT_OUTPUT = Path("release") / "apple-hig.zip"
RUNTIME_FILES = ("SKILL.md", "README.md", "routing-index.md")
FORBIDDEN_CHARS = set('<>:"|?*')
CONTROL_CHAR = re.compile(r"[\x00-\x1f]")


def validate_archive_path(path: str) -> None:
    if "\\" in path:
        raise ValueError(f"backslash path separator: {path}")
    if path.startswith("/") or re.match(r"^[A-Za-z]:", path):
        raise ValueError(f"absolute path: {path}")
    if any(part in {"", ".", ".."} for part in path.split("/")):
        raise ValueError(f"unsafe path segment: {path}")
    if any(char in FORBIDDEN_CHARS for char in path):
        raise ValueError(f"forbidden filename character: {path}")
    if CONTROL_CHAR.search(path):
        raise ValueError(f"control character in path: {path!r}")
    if "__MACOSX" in path.split("/"):
        raise ValueError(f"macOS resource fork path: {path}")
    if any(part.startswith(".") for part in path.split("/")):
        raise ValueError(f"hidden path segment: {path}")
    if any(part.startswith("Icon") for part in path.split("/")):
        raise ValueError(f"macOS icon metadata path: {path}")


def add_file(zip_file: zipfile.ZipFile, source: Path, archive_path: str) -> None:
    validate_archive_path(archive_path)
    info = zipfile.ZipInfo(archive_path)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.date_time = (2026, 6, 9, 0, 0, 0)
    info.external_attr = 0o644 << 16
    zip_file.writestr(info, source.read_bytes())


def build_zip(repo_root: Path, output: Path) -> None:
    distilled = sorted((repo_root / "distilled").glob("*.md"))
    if len(distilled) != 156:
        raise RuntimeError(f"expected 156 distilled files, found {len(distilled)}")

    for relative in RUNTIME_FILES:
        if not (repo_root / relative).is_file():
            raise FileNotFoundError(relative)

    output.parent.mkdir(parents=True, exist_ok=True)
    temp_output = output.with_suffix(output.suffix + ".tmp")
    if temp_output.exists():
        temp_output.unlink()

    with zipfile.ZipFile(temp_output, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for relative in RUNTIME_FILES:
            add_file(zip_file, repo_root / relative, f"{SKILL_ROOT}/{relative}")
        for source in distilled:
            add_file(zip_file, source, f"{SKILL_ROOT}/distilled/{source.name}")

    if output.exists():
        output.unlink()
    temp_output.replace(output)


def inspect_zip(output: Path) -> dict[str, object]:
    with zipfile.ZipFile(output) as zip_file:
        names = zip_file.namelist()

    for name in names:
        validate_archive_path(name)

    top_level = sorted({name.split("/")[0] for name in names})
    distilled_count = sum(
        1
        for name in names
        if name.startswith(f"{SKILL_ROOT}/distilled/") and name.endswith(".md")
    )
    forbidden_prefixes = (
        f"{SKILL_ROOT}/sources/",
        f"{SKILL_ROOT}/scripts/",
        f"{SKILL_ROOT}/.git/",
    )
    forbidden_exact = {
        f"{SKILL_ROOT}/process.md",
        f"{SKILL_ROOT}/.gitignore",
    }
    forbidden = [
        name
        for name in names
        if name in forbidden_exact or any(name.startswith(prefix) for prefix in forbidden_prefixes)
    ]

    return {
        "entries": len(names),
        "top_level": top_level,
        "distilled_count": distilled_count,
        "forbidden": forbidden,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"zip path to write; default: {DEFAULT_OUTPUT}",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    output = (repo_root / args.output).resolve() if not args.output.is_absolute() else args.output

    build_zip(repo_root, output)
    summary = inspect_zip(output)

    if summary["top_level"] != [SKILL_ROOT]:
        raise RuntimeError(f"unexpected top-level entries: {summary['top_level']}")
    if summary["distilled_count"] != 156:
        raise RuntimeError(f"unexpected distilled count: {summary['distilled_count']}")
    if summary["forbidden"]:
        raise RuntimeError(f"forbidden paths included: {summary['forbidden']}")

    print(f"wrote {output}")
    print(f"entries: {summary['entries']}")
    print(f"top-level: {', '.join(summary['top_level'])}")
    print(f"distilled files: {summary['distilled_count']}")
    print("forbidden paths: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
