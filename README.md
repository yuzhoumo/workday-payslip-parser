# Workday Payslip Parser

This script parses Excel payslips from Workday into a single table in either
JSON or CSV format. Payslips can be exported from Workday from each Payslip
page by clicking on the "Export to Excel" icon in the top right corner.

Refer to the included [guide](payslip-automation-guide.md) on how to
automatically download all of your payslips.

## Web Usage

For convenience, I've also created a web tool:

- Drag-and-Drop Web Tool: [payslips.joemo.dev](https://payslips.joemo.dev)

All file processing happens locally. The web tool is a single self-contained
`index.html` file that can be found on the `gh-pages` branch. The source for
this tool is in `/web`.

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
