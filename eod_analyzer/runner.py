"""CLI runner for EOD Analyzer (skeleton)."""

from __future__ import annotations

import argparse
import sys
from datetime import date as date_type
from pathlib import Path

from .io import analyze_date, analyze_dates


def _parse_date(value: str) -> str:
    try:
        year, month, day = (int(part) for part in value.split("-"))
        parsed = date_type(year, month, day)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid date: {value}") from exc
    return parsed.isoformat()


def _run_single_date(input_root: Path, output_root: Path, date: str) -> int:
    try:
        analyze_date(date)
    except Exception as exc:
        sys.stderr.write(f"Failed {date}: {exc}\n")
        return 1
    return 0


def _run_date_range(input_root: Path, output_root: Path, start_date: str, end_date: str) -> int:
    try:
        analyze_dates(start_date, end_date)
    except Exception as exc:
        sys.stderr.write(f"Failed {start_date}..{end_date}: {exc}\n")
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run EOD Analyzer.")
    parser.add_argument(
        "--input-root",
        default="input",
        help="Root folder containing YYYY/MM/DD/eod_candles.json",
    )
    parser.add_argument(
        "--output-root",
        default="history",
        help="Root folder for history/YYYY/MM/DD/eod_state.json",
    )
    parser.add_argument("--date", type=_parse_date, help="Single date YYYY-MM-DD")
    parser.add_argument("--start-date", type=_parse_date, help="Range start YYYY-MM-DD")
    parser.add_argument("--end-date", type=_parse_date, help="Range end YYYY-MM-DD")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_root = Path(args.input_root)
    output_root = Path(args.output_root)

    if args.date and (args.start_date or args.end_date):
        sys.stderr.write("Use either --date or --start-date/--end-date\n")
        return 2

    if (args.start_date and not args.end_date) or (args.end_date and not args.start_date):
        sys.stderr.write("Both --start-date and --end-date are required\n")
        return 2

    if args.date:
        return _run_single_date(input_root, output_root, args.date)

    if args.start_date and args.end_date:
        return _run_date_range(input_root, output_root, args.start_date, args.end_date)

    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
