# pythondev

A simple Python project for formatting file sizes into human-readable strings.

## Features

- Converts file sizes in bytes to KB, MB, GB, or TB.
- Provides a command-line interface for formatting file sizes.
- Includes unit tests for reliability.

## Usage

Run the main script with a file size in bytes as an argument:

```bash
python main.py <size_in_bytes>
```

Example:

```bash
python main.py 1048576
# Output: 1.00 MB
```

## Testing with pytest

This project uses [pytest](https://pytest.org/) for unit testing.
To run the tests, execute:

```bash
pytest
```

## Installing dependencies with uv

You can use [uv](https://github.com/astral-sh/uv) for fast Python package management.
To install dependencies:

```bash
uv pip install -r requirements.txt
```
## Folder Structure
```

../pythondev/
├── data
│   └── create_dummy_files.py
├── main.py
├── Makefile
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│   ├── date_parser.py
│   ├── formatter.py
│   └── __init__.py
├── tests
│   ├── __init__.py
│   ├── test_date_parser.py
│   └── test_format_file_size.py
└── uv.lock


```
