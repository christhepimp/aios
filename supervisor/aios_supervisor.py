#!/usr/bin/env python3
"""AIOS supervisor prototype.

Host-side control plane. Talks to a rooted emulator over adb later.
This file is a structured loop, not a kernel.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class Observation:
    timestamp: str
    source: str
    note: str


@dataclass
class Action:
    kind: str
    payload: dict


class Supervisor:
    def __init__(self, dry_run: bool = True) -> None:
        self.dry_run = dry_run
        self.memory: list[dict] = []

    def perceive(self) -> Observation:
        return Observation(
            timestamp=datetime.now(timezone.utc).isoformat(),
            source="stub",
            note="No emulator attached. Wire adb shell dumpsys and screencap next.",
        )

    def plan(self, obs: Observation) -> Action:
        return Action(
            kind="announce",
            payload={
                "message": "AIOS supervisor alive",
                "observation": asdict(obs),
                "next": ["attach adb", "require su", "replace launcher not kernel"],
            },
        )

    def act(self, action: Action) -> None:
        record = {"action": asdict(action), "dry_run": self.dry_run}
        self.memory.append(record)
        print(json.dumps(record, indent=2))

    def loop_once(self) -> None:
        self.act(self.plan(self.perceive()))


def main() -> None:
    parser = argparse.ArgumentParser(description="AIOS supervisor")
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()
    Supervisor(dry_run=args.dry_run).loop_once()


if __name__ == "__main__":
    main()
