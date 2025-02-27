"""
File handling functions for the compound interest calculator.

This module contains functions for saving calculated data
to various file formats for later reference.
"""
from typing import List, Dict, Union, Any
from pathlib import Path
import csv
import pandas as pd


def save_to_excel(
        data: List[Dict[str, Union[int, float]]],
        folder_path: Path
) -> Path:
    """
    Save compound interest data to an Excel file.

    Args:
        data: The list of yearly data dictionaries from calculate_compound_interest
        folder_path: The folder path where the file should be saved

    Returns:
        The path to the saved Excel file

    Examples:
        >>> results = calculate_compound_interest(1000, 5, 30, 'M', 100)
        >>> folder = Path.cwd() / "investment_data"
        >>> excel_path = save_to_excel(results, folder)
        >>> print(f"Data saved to {excel_path}")
    """
    file_path = folder_path / 'compound_interest_data.xlsx'
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return file_path


def save_to_csv(
        data: List[Dict[str, Union[int, float]]],
        folder_path: Path
) -> Path:
    """
    Save compound interest data to a CSV file.

    Args:
        data: The list of yearly data dictionaries from calculate_compound_interest
        folder_path: The folder path where the file should be saved

    Returns:
        The path to the saved CSV file

    Examples:
        >>> results = calculate_compound_interest(1000, 5, 30, 'M', 100)
        >>> folder = Path.cwd() / "investment_data"
        >>> csv_path = save_to_csv(results, folder)
        >>> print(f"Data saved to {csv_path}")
    """
    file_path = folder_path / 'compound_interest_data.csv'

    with open(file_path, 'w', newline='') as csvfile:
        if not data:
            return file_path

        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return file_path


def create_results_folder(
        initial_amount: float,
        interest_rate: float,
        interval: str,
        regular_deposit: float,
        base_path: Path = None
) -> Path:
    """
    Create a uniquely named folder for saving calculation results.

    Args:
        initial_amount: The starting investment amount
        interest_rate: The annual interest rate percentage
        interval: The deposit interval code
        regular_deposit: The regular deposit amount
        base_path: The base directory path (defaults to current working directory)

    Returns:
        Path object pointing to the created folder

    Examples:
        >>> folder = create_results_folder(1000, 5, 'M', 100)
        >>> print(f"Results will be saved to {folder}")
    """
    import datetime

    # Create a timestamp string for uniqueness
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create a folder name based on the parameters
    folder_name = f"{initial_amount}_{interest_rate}_{interval}_{regular_deposit}_{timestamp}"

    # Determine the base path
    if base_path is None:
        base_path = Path.cwd()

    # Create the full folder path
    folder_path = base_path / folder_name

    # Create the folder
    folder_path.mkdir(exist_ok=True)

    return folder_path