"""ReFold's mini-swe-agent adapter with FOUND switched on by default."""

from __future__ import annotations

from refold.strategies.refold.agent import ReFoldAgent, ReFoldConfig


class ReFoldFoundConfig(ReFoldConfig):
    found: bool = True


class ReFoldFoundAgent(ReFoldAgent):
    config_class = ReFoldFoundConfig
