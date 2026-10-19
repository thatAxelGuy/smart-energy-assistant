# Smart Energy Assistant

A smart home energy assistant that turns meter readings and real German wholesale prices into clear costs, and uses AI to explain your bill and tell you when to use energy most cheaply.

**Status:** Work in progress. Currently building the backend foundation (Django REST API, Postgres, price data import). AI features follow in later stages.

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

## License

[MIT](LICENSE)
