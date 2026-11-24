"""Check a packaged LÖVE game without extracting or running it."""
import argparse
from pathlib import PurePosixPath
from zipfile import BadZipFile, ZipFile


def check(filename):
    with ZipFile(filename) as archive:
        entries = [entry.filename for entry in archive.infolist() if not entry.is_dir()]
        if "main.lua" not in entries:
            raise ValueError("main.lua must be at the archive root")
        if len(set(entries)) != len(entries):
            raise ValueError("duplicate file names")
        for name in entries:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or "\\" in name:
                raise ValueError(f"non-portable path: {name}")
        broken = archive.testzip()
        if broken:
            raise ValueError(f"CRC failure: {broken}")
        return len(entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    args = parser.parse_args()
    try:
        count = check(args.archive)
    except (OSError, BadZipFile, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"OK: {count} files, main.lua at root")
