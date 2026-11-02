import argparse
import os
import sys
from pathlib import Path


ZONE_IDENTIFIER_SUFFIX = ":Zone.Identifier"


def delete_zone_identifier_files(directory: Path, dry_run: bool = False) -> int:
    if not directory.is_dir():
        raise NotADirectoryError(f"{directory} is not a directory")

    deleted_count = 0

    def raise_walk_error(error: OSError) -> None:
        raise error

    for root, _, files in os.walk(directory, onerror=raise_walk_error):
        for filename in files:
            if filename != "Zone.Identifier" and not filename.endswith(
                ZONE_IDENTIFIER_SUFFIX
            ):
                continue

            file_path = Path(root) / filename
            try:
                if dry_run:
                    print(f"Would delete {file_path}")
                else:
                    file_path.unlink()
                    print(f"Deleted {file_path}")
                deleted_count += 1
            except OSError as error:
                print(f"Error deleting {file_path}: {error}", file=sys.stderr)

    return deleted_count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Delete Windows zone identifier sidecar files."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="directory to scan (defaults to the directory containing this script)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="list matching files without deleting them",
    )
    args = parser.parse_args()

    try:
        delete_zone_identifier_files(args.directory, dry_run=args.dry_run)
    except OSError as error:
        print(f"Error scanning {args.directory}: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
