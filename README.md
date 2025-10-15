# pythondev

A Python project for parsing, unifying, and comparing timestamps found in various formats, including as substrings in filenames.
It includes utilities for finding files with timestamp patterns in subfolders, extracting timestamps, and matching files by unified timestamps.

## Features

- Parses timestamps from strings, numbers, and filenames.
- Supports formats like ISO, RFC, Unix epoch, `YYYY_MM_DD_HH_MM_SS`, and `DD_MM_YYYY_HH_MM_SS`.
- Recursively finds files with timestamp substrings in subfolders of a base folder.
- Matches files with identical timestamps across different subfolders.
- Provides a command-line script for demonstration and testing.
- Includes unit tests and dummy data generation.

## Usage

### Create Dummy Files

To generate dummy files for testing, run:

```bash
make create-dummy
```

### Run the Parser

To run the parser and see timestamp extraction and matching:

```bash
make run
```

### Run Tests

To run all tests (including those using dummy files):

```bash
make test
```

### Clean Up

To remove cache and all subfolders/files from the `data` folder except the dummy file generator:

```bash
make clean
```

### All-in-one

To create dummy files, run the parser, test, and clean up:

```bash
make all
```

## Project Structure

```
pythondev/
├── data/
│   ├── create_dummy_files.py
│   └── ... (generated dummy files and subfolders)
├── src/
│   ├── date_parser.py
│   └── formatter.py
├── tests/
│   └── test_date_parser.py
├── Makefile
├── requirements.txt
├── .pre-commit-config.yaml
└── README.md
```

## Development

- Code formatting and linting are handled by [Black](https://github.com/psf/black) and [Flake8](https://github.com/PyCQA/flake8) via pre-commit hooks.
- Dummy files are automatically created before running or testing.
- All timestamp logic is in `src/date_parser.py`.
- Tests are in `tests/test_date_parser.py`.

## Dependencies

Install dependencies with [uv](https://github.com/astral-sh/uv):

```bash
uv pip install -r requirements.txt
```

Or with pip:

```bash
pip install -r requirements.txt
```

## License

This project is open source and free to use.
