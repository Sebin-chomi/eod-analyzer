"""Pure analysis logic for EOD Analyzer (skeleton)."""

from __future__ import annotations

from typing import Iterable, Mapping


class CandleValidationError(ValueError):
    """Raised when input candles are invalid or inconsistent."""


def compute_eod_state_v0(
    date: str,
    candles: Iterable[Mapping[str, object]],
) -> dict[str, object]:
    """Compute EOD_STATE v0 for a single date from EOD candles."""
    raise NotImplementedError("EOD Analyzer core logic is not implemented.")
