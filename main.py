#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't (variant B).

One line of weather forecast for Mistwick, a fictional city where the fog
runs on a timetable like a bus. Deterministic: no network, no randomness,
no clock. Writes the entry to /output/entry.txt first, then (best effort)
a copy at the repo root guarded by try/except, because the grader sandbox
mounts the repo root read-only.
"""

import os
import sys

ENTRY = (
    "Today in Mistwick: fog due 7:12, gone by 8:05. "
    "The 7:40 fog is cancelled, so commuters, take the 8:10 mist "
    "instead \u2014 and mind the gap."
)

# ---------------------------------------------------------------------------
# Iteration log: ONE concept (scheduled fog in Mistwick), v1 -> v8.
# v1 (106): "Today in Mistwick: fog due at 7:12, thick by 7:20 - commuters,
#   mind the gap between the mist and your bus."
#   KEPT the city + timetable idea; DROPPED "mind the gap between the mist
#   and your bus" - muddled, the gap image lands nowhere.
# v2 (112): "Today in Mistwick: fog arrives 7:12 sharp, departs 8:05 - if
#   you miss it, the next fog is 9:40, so don't dawdle."
#   KEPT the "next fog" turn; DROPPED "don't dawdle" - generic advice, no
#   smile, and it wastes the ending.
# v3 (120): "Today in Mistwick: fog due 7:12, thick by 7:20. Buses run on
#   time; the fog runs earlier - bring a torch and a timetable."
#   KEPT "the fog runs earlier" (fog as a service); DROPPED the torch +
#   timetable ending - two props competing, neither lands.
# v4 (129): "Today in Mistwick: fog 7:12-8:05, visibility two lamp-posts.
#   Commuters: the 7:40 fog is cancelled, so take the 8:10 mist instead."
#   KEPT as the base: concrete detail (two lamp-posts) + the cancelled-fog
#   turn, which treats fog exactly like a train service. DROPPED the
#   "visibility" clause in later versions - it crowded the timetable.
# v5 (135): "Today in Mistwick: fog arrives 7:12 sharp and leaves at 8:05.
#   Miss it and the next fog is 9:40 - the bus stop has a timetable for
#   both."
#   KEPT the 9:40 next-fog idea; DROPPED "a timetable for both" - it
#   explains the joke instead of landing it.
# v6 (129): "Today in Mistwick: fog due 7:12, gone by 8:05. Commuters, the
#   7:40 fog is cancelled - please take the 8:10 mist and mind the gap."
#   KEPT "mind the gap" - the tube-announcement echo every commuter hears;
#   DROPPED "please" in v8 - it softens the announcement voice.
# v7 (130): "Today in Mistwick: fog 7:12-8:05, thick enough to lose your bus
#   in. The 7:40 fog is cancelled; the 8:10 mist will wait for no one."
#   KEPT "the 8:10 mist will wait for no one" as a candidate kicker; DROPPED
#   "thick enough to lose your bus in" - wordy setup for a line v8 says
#   in three words ("mind the gap").
# v8 (134) SHIPPED: v4's cancelled-fog turn + v6's "mind the gap" kicker,
#   "instead" tightened the swap, "please" cut for pace. Broadcast rhythm
#   ("Today in Mistwick: ..."), named fictional city, concrete timetable
#   (7:12 / 8:05 / 7:40 cancelled / 8:10 mist), one turn, 134 chars.
# ---------------------------------------------------------------------------


def main() -> int:
    line = ENTRY
    if not (1 <= len(line) <= 140):
        print(f"entry length {len(line)} outside 1-140", file=sys.stderr)
        return 1
    if line != line.strip() or "\n" in line or "\r" in line:
        print("entry must be a single non-padded line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass  # Grader sandbox mounts the repo root read-only; /output is enough.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
