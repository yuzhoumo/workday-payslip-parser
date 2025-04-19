# Workday Payslip Parser

This script parses Excel payslips from Workday into a single table in CSV
format. Payslips can be exported from Workday from each Payslip page by
clicking on the "Export to Excel" icon in the top right corner.

## Usage

Install dependencies using [`uv`](https://github.com/astral-sh/uv):

```bash
uv sync
```

Once installed, you can run the script from the command line:

```bash
uv run main.py -i <input_directory> -o <output_file.csv>
```

### Options

| Argument               | Description                                               | Default           |
|------------------------|-----------------------------------------------------------|-------------------|
| `-i`, `--input-dir`    | Directory containing `.xlsx` payslip files                | Current dir (`.`) |
| `-o`, `--output-file`  | Output CSV file path                                      | `output.csv`      |
| `-q`, `--quiet`        | Do not print to console while running                     | False             |
