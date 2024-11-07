i# Log Message Filter

This project contains a function to obfuscate specified fields in log messages using regular expressions.

## Requirements
- Python 3.7
- `pycodestyle` (version 2.5)

## Usage
1. Ensure all files are executable.
2. Run `main.py` to test the `filter_datum` function.

## Example
```bash
$ ./main.py
name=egg;email=eggmin@eggsample.com;password=REDACTED;date_of_birth=REDACTED;
name=bob;email=bob@dylan.com;password=REDACTED;date_of_birth=REDACTED;
