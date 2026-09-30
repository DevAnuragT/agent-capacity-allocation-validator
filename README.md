# Capacity Allocation Validator

Sums assignments by named resource and compares each total with its explicit capacity. It reports over-allocation evidence without rebalancing work.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-capacity-allocation-validator.py examples/good-input.json
```

## Limitations

This arithmetic check cannot assess skill fit, scheduling conflicts, time zones, concurrency, or whether capacity estimates are realistic. It does not move, reject, or approve assignments.
