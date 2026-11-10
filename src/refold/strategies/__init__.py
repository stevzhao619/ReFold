"""The built-in strategies. Importing this package registers them.

    base     nothing is removed (mini-swe-agent's own append-only loop)
    compact  an extra model call summarises old history at 75% of the budget
    refold   deduplication and folding at the rendering layer
    refold-found  refold plus a FOUND line kept in fold notes (experiment)
    refold-found-dropped  the same, but fold notes drop the FOUND lines (control)

`--compact` runs ReFold beneath compaction (compact + ReFold).
"""

from refold.strategies import base, compact, refold, refold_found, refold_found_dropped  # noqa: F401
