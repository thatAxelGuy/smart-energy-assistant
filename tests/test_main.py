"""Smoke test so the test setup works from the first commit."""

from main import main


def test_main_runs(capsys) -> None:
    """main() runs and prints a greeting."""
    main()
    assert "Hello" in capsys.readouterr().out
