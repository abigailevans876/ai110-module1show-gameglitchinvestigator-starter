# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

Tool: Claude (Claude Code in VS Code).

Prompts used: "guide me in making all the necessary changes", followed by "can you add these changes?", after sharing the grading rubric. Claude suggested `parse_guess` edge-case tests and then added them to `tests/test_game_logic.py`.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Empty input | "guide me in making all the necessary changes" | `test_empty_input`: `parse_guess("")` returns `ok=False` and "Enter a guess." | Yes | Players can click Submit without typing anything. That should show a message, not count as a guess or crash. |
| Non-numeric text | same | `test_non_numeric_input`: `parse_guess("abc")` returns `ok=False` and "That is not a number." | Yes | `int("abc")` raises an error. This checks that the `try/except` catches it and shows a friendly message. |
| Negative number | same | `test_negative_number`: `parse_guess("-5")` returns `ok=True, value=-5` | Yes | Checks that the minus sign is parsed correctly. It also documents that the game accepts guesses outside the range instead of rejecting them. |
| Decimal | same | `test_decimal_is_truncated`: `parse_guess("3.7")` returns `ok=True, value=3` | Yes | The `"." in raw` branch is a separate code path. This confirms that decimals are cut down to a whole number rather than rounded. |
