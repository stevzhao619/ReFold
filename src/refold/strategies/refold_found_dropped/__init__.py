"""Control for refold-found: the same prompt and the same FOUND line, but the fold notes
do not keep it (PROGRESS only, as in ReFold)."""

from refold.registry import StrategySpec, register_strategy

register_strategy(StrategySpec(
    name="refold-found-dropped",
    agent="refold.strategies.refold_found_dropped.agent.ReFoldFoundDroppedAgent",
    summary="refold-found, but fold notes drop the FOUND lines (written, not kept)",
))
