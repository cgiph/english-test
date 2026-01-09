# English Test — Diagnostic (A1–A2)

This repository contains a diagnostic English test for A1–A2 learners covering:
- Grammar (10 items: multiple-choice and gap-fill)
- Listening (2 items; summary-style)
- Reading (1 passage with 5 multiple-choice + 5 short-answer)
- Mini-essay (1 prompt; holistic 1–10 rubric with CEFR equivalents)

Structure
- tests/
  - grammar/
  - listening/
  - reading/
  - writing/
- tools/
  - score.py — automatic scorer for objective items (Python)
- sample_answers/
- LICENSE (CC BY-SA 4.0)

How to use
1. Place listening MP3s in `tests/listening/audio/` with filenames matching the manifest.
2. Collect examinee answers in `answers.json` (format shown in `tools/score.py` usage).
3. Run:
```
python3 tools/score.py --answers answers.json --key tests/keys/all_keys.json
```
This scores objective sections (grammar, listening multiple-choice, reading multiple-choice & short answers) and accepts a manual essay score input (1–10).

License: CC BY-SA 4.0 (for test content)
