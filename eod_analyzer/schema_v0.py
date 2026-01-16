"""EOD_STATE v0 schema definition."""

EOD_STATE_SCHEMA_VERSION = "EOD_STATE.v0"

# The v0 schema is treated as immutable. Changes require a new version.
EOD_STATE_V0_FIELDS = (
    "schema",
    "date",
    "universe",
    "candles",
)

EOD_STATE_V0_UNIVERSE_FIELDS = (
    "count",
    "symbols",
)

EOD_STATE_V0_CANDLE_FIELDS = (
    "open",
    "high",
    "low",
    "close",
    "volume",
    "range",
    "body",
    "upper_wick",
    "lower_wick",
)
