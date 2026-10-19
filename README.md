# python-uv-template

Starter template for Python projects with [uv](https://docs.astral.sh/uv/),
[Ruff](https://docs.astral.sh/ruff/) and [pytest](https://docs.pytest.org/).

## Using this template

1. Click **Use this template** on GitHub and create your repository.
2. Rename the project in `pyproject.toml` (`name`, `description`) and
   replace this README.
3. Set up the environment:

   ```bash
   uv sync
   ```

4. Add dependencies with `uv add <package>` and dev tools with
   `uv add --dev <package>`.

## Commands

```bash
uv run main.py              # run the program
uv run pytest               # run the tests
uv run ruff check .         # lint
uv run ruff check --fix .   # lint and fix what can be fixed
uv run ruff format .        # format
```

For hosts that need a `requirements.txt` (e.g. PythonAnywhere):

```bash
uv export --format requirements-txt --no-hashes --no-dev -o requirements.txt
```

## What's included

- Python 3.13 via `.python-version`
- Ruff: PEP 8 line length (79, docstrings 72), import sorting, bugbear,
  pyupgrade, simplify and pathlib rules
- pytest with a smoke test in `tests/`
- GitHub Actions workflow that lints, checks formatting and runs the
  tests on every push and pull request
- `.editorconfig`, `.gitignore` and `.env.example`

## License

[MIT](LICENSE)
