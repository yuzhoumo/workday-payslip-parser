# Workday Payslip Parser

This script parses Excel payslips from Workday into a single table in either
JSON or CSV format. Payslips can be exported from Workday from each Payslip
page by clicking on the "Export to Excel" icon in the top right corner.

## Web Usage

For convenience, I've created a web version of the script, along with a
dashboard available here:

- Web Converter: [payslips.joemo.dev/converter](https://payslips.joemo.dev/converter)
- Drag-and-Drop Dashboard: [payslips.joemo.dev](https://payslips.joemo.dev/converter)

These are static webpages with the python scripts embedded as WASM using
Pyodide, so all file processing happens locally. The source code for these
pages can be found in the `/web` directory.

## Script Usage

Install dependencies using [`uv`](https://github.com/astral-sh/uv):

```bash
uv sync
```

Once installed, you can run the script from the command line:

```bash
uv run main.py -i <input_directory> -o <output_file>
```

### Options

| Argument               | Description                                               | Default           |
|------------------------|-----------------------------------------------------------|-------------------|
| `-i`, `--input-dir`    | Directory containing `.xlsx` payslip files                | Current dir (`.`) |
| `-f`, `--format`       | Format of the output file (either `json` or `csv`)        | `json`            |
| `-o`, `--output-file`  | Output file name                                          | `output`          |
| `-q`, `--quiet`        | Do not print to console while running                     | False             |
