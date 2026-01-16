"""I/O helpers for EOD Analyzer (skeleton)."""

from __future__ import annotations

from pathlib import Path
from datetime import date as date_type, timedelta
import sys
from typing import Mapping

DEFAULT_INPUT_FILENAME = "eod_candles.json"
DEFAULT_OUTPUT_FILENAME = "eod_state.json"

Candle = Mapping[str, object]


def load_eod_for_date(trade_date: str) -> Candle:
    """Load raw EOD candle data for a single date."""
    year, month, day = trade_date.split("-")
    input_path = f"input/{year}/{month}/{day}/eod_candles.json"
    _ = input_path
    raise NotImplementedError("EOD Analyzer I/O is not implemented.")


def analyze_eod(eod_candle: Candle) -> Mapping[str, object]:
    """Analyze a single EOD candle and return state payload."""
    raise NotImplementedError("EOD Analyzer core logic is not implemented.")


def write_eod_state(trade_date: str, state: Mapping[str, object]) -> None:
    """Write EOD_STATE.v0 for a single date."""
    year, month, day = trade_date.split("-")
    output_path = f"history/{year}/{month}/{day}/eod_state.json"
    _ = (output_path, state)
    raise NotImplementedError("EOD Analyzer I/O is not implemented.")


def analyze_date(trade_date: str) -> None:
    """Analyze one date and write one output file."""
    eod_candle = load_eod_for_date(trade_date)
    state = analyze_eod(eod_candle)
    write_eod_state(trade_date, state)


def analyze_dates(start_date: str, end_date: str) -> None:
    """Analyze dates in range (inclusive); skip failures."""
    start = date_type.fromisoformat(start_date)
    end = date_type.fromisoformat(end_date)
    if end < start:
        raise ValueError("end_date must be >= start_date")

    current = start
    while current <= end:
        trade_date = current.isoformat()
        try:
            analyze_date(trade_date)
        except Exception as exc:
            print(f"Failed {trade_date}: {exc}", file=sys.stderr)
        current += timedelta(days=1)


def _date_to_path(root: Path, date: str, filename: str) -> Path:
    year, month, day = date.split("-")
    return root / year / month / day / filename
