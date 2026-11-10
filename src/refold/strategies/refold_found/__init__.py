"""ReFold with a FOUND line (experiment): ReFold's protocol plus a third reply line that
records the concrete result a tool output taught, kept in the fold note of the step it
describes. `refold` itself is unchanged."""

from refold.registry import StrategySpec, register_strategy

register_strategy(StrategySpec(
    name="refold-found",
    agent="refold.strategies.refold_found.agent.ReFoldFoundAgent",
    summary="refold, plus a FOUND line per reply that fold notes keep",
))
