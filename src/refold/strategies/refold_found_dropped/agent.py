"""refold-found with found_keep off: FOUND is asked for and recorded, never put in a note."""

from __future__ import annotations

from refold.strategies.refold_found.agent import ReFoldFoundAgent, ReFoldFoundConfig


class ReFoldFoundDroppedConfig(ReFoldFoundConfig):
    found_keep: bool = False


class ReFoldFoundDroppedAgent(ReFoldFoundAgent):
    config_class = ReFoldFoundDroppedConfig
