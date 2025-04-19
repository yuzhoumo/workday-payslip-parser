import os
import csv
import argparse
from openpyxl import load_workbook

from io import TextIOWrapper
from openpyxl.worksheet.worksheet import Worksheet
from typing import Any


def parse_table_single_row(ws: Worksheet, start_row: Any, output: dict):
    """
    Parses a single-row style table from the worksheet.

    The format is expected to be:
    - Title in the first column at `start_row`
    - Labels in the row `start_row + 1`
    - Values in the row `start_row + 2`

    Each key is constructed as: "<Title> - <Label>"

    Args:
        ws (Worksheet): The worksheet to parse.
        start_row (Any): The row index where the table starts.
        output (dict): Dictionary to store parsed key-value pairs.
    """
    key_prefix = ws.cell(start_row, 1).value
    label_row = start_row + 1
    data_row = start_row + 2
    col = 1
    while ws.cell(label_row, col).value is not None:
        key_suffix = ws.cell(label_row, col).value
        key = f'{key_prefix} - {key_suffix}'
        val = ws.cell(data_row, col).value
        output[key] = val
        col += 1


def parse_table_grid(ws: Worksheet, start_row: Any, output: dict):
    """
    Parses a grid-style table from the worksheet.

    The format is expected to be:
    - Title in the first column at `start_row`
    - Column headers in row `start_row + 1`
    - Row headers in column A starting at `start_row + 2`
    - Data values in the grid formed by headers

    Each key is constructed as: "<Title> - <Row Header> - <Column Header>"

    Args:
        ws (Worksheet): The worksheet to parse.
        start_row (Any): The row index where the table starts.
        output (dict): Dictionary to store parsed key-value pairs.
    """
    key_prefix = ws.cell(start_row, 1).value
    label_row = start_row + 1
    data_row = start_row + 2
    while ws.cell(data_row, 2).value is not None:
        col = 2
        key_suffix_1 = ws.cell(data_row, 1).value
        while ws.cell(label_row, col).value is not None:
            key_suffix_2 = ws.cell(label_row, col).value
            val = ws.cell(data_row, col).value
            key = f'{key_prefix} - {key_suffix_1} - {key_suffix_2}'
            output[key] = val
            col += 1
        data_row += 1


def parse_payslip(filename: str) -> dict:
    """
    Parses a payslip Excel file and extracts relevant information
    based on section headers.

    Args:
        filename (str): Path to the Excel (.xlsx) file.

    Returns:
        dict: A dictionary with keys as constructed from table headers
              and values as extracted data.
    """
    ws = load_workbook(filename).active
    if not ws:
        raise Exception(f"failed to load workbook: {filename}")

    payslip_data = {}
    for cell in ws['A']:
        match cell.value:
            case 'Company Information':
                parse_table_single_row(ws, cell.row, payslip_data)
            case 'Payslip Information':
                parse_table_single_row(ws, cell.row, payslip_data)
            case 'Current and YTD Totals':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Earnings':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Employee Taxes':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Pre Tax Deductions':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Post Tax Deductions':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Employer Paid Benefits':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Taxable Wages':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Withholding':
                parse_table_grid(ws, cell.row, payslip_data)
            case 'Payment Information':
                parse_table_single_row(ws, cell.row, payslip_data)

    return payslip_data


def convert_to_csv_file(dir: str, out: TextIOWrapper, verbose: bool = False):
    """
    Converts all .xlsx payslip files in the given directory to a CSV file.

    Args:
        dir (str): Path to the directory containing Excel files.
        out (TextIOWrapper): Output file handle to write the CSV data.
        verbose (bool): Whether to print progress messages.
    """
    keys, rows = [], []
    for filename in os.listdir(dir):
        if filename.endswith('.xlsx'):
            full_path = os.path.join(dir, filename)
            if verbose:
                print(f'Parsing {filename}...')
            row = parse_payslip(full_path)
            rows.append(row)
            keys.extend(row.keys())

    writer = csv.DictWriter(out, fieldnames=keys)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)


def main():
    """
    Entry point of the script. Parses CLI arguments and runs the conversion.
    """
    parser = argparse.ArgumentParser(
        description='Convert payslip Excel files to a single CSV file.'
    )
    parser.add_argument(
        '-i', '--input-dir', type=str, default='.',
        help='Directory containing .xlsx files (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output-file', type=str, default='output.csv',
        help='Output CSV file path (default: output.csv)'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    with open(args.output_file, 'w', newline='') as f:
        convert_to_csv_file(args.input_dir, f, verbose=args.verbose)


if __name__ == '__main__':
    main()
