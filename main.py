#!/usr/bin/env python3
"""
Compound Interest Calculator

A tool for calculating the growth of investments over time with regular
deposits and visualizing the results through various graphs.

Author: Rui Pedro Gomes
License: Apache 2.0
"""
from pathlib import Path
from typing import Dict, List, Union, Any

from compound_interest.input_handlers import (
    get_float_input,
    get_int_input,
    get_interval_input,
    get_yes_no_input,
    validate_input_parameters
)
from compound_interest.calculations import (
    calculate_compound_interest,
    format_currency,
    calculate_summary_statistics
)
from compound_interest.visualization import generate_graphs
from compound_interest.file_handlers import (
    save_to_excel,
    save_to_csv,
    create_results_folder
)
from compound_interest.constants import DEFAULT_PARAMETERS


def display_results(summary: Dict[str, Any]) -> None:
    """
    Display calculation results to the user.

    Args:
        summary: A dictionary containing summary statistics
    """
    print("\n===== Investment Results =====")
    print(f"Total amount invested: {format_currency(summary['total_invested'])}")
    print(f"Total amount in interest: {format_currency(summary['total_interest'])}")
    print(f"Final Amount: {format_currency(summary['final_amount'])}")
    print(f"Return on Investment: {summary['roi_percentage']}%")
    print(f"Compound Annual Growth Rate: {summary['cagr_percentage']}%")
    print(f"For every $1 invested, you earned ${summary['interest_to_investment_ratio']} in interest")
    print("==============================")


def save_results(
        data: List[Dict[str, Union[int, float]]],
        initial_amount: float,
        interest_rate: float,
        interval: str,
        regular_deposit: float
) -> None:
    """
    Save calculation results to files and generate visualizations.

    Args:
        data: The calculation results
        initial_amount: The starting investment amount
        interest_rate: The annual interest rate percentage
        interval: The deposit interval code
        regular_deposit: The regular deposit amount
    """
    # Create a folder to save the results
    folder_path = create_results_folder(
        initial_amount,
        interest_rate,
        interval,
        regular_deposit
    )

    # Save data to files
    excel_path = save_to_excel(data, folder_path)
    csv_path = save_to_csv(data, folder_path)

    # Generate graphs
    generate_graphs(data, folder_path)

    # Inform the user
    print(f"\nData and graphs saved in folder: {folder_path.name}")
    print(f"Files generated:")
    print(f"  - {excel_path.name}")
    print(f"  - {csv_path.name}")
    print(f"  - Graphs in '{folder_path.name}/graphs/' directory")


def main() -> None:
    """
    Main function to run the compound interest calculator.

    This function handles the main program flow, collecting user inputs,
    performing calculations, displaying results, and saving data if requested.
    """
    print("===== Compound Interest Calculator =====")
    print("Welcome! This tool will help you calculate how your investments grow over time.")

    while True:
        # Collect user inputs
        print("\nPlease enter your investment details:")
        initial_amount = get_float_input("Enter the initial amount: ")
        interest_rate = get_float_input("Enter the yearly interest percentage: ")
        interval = get_interval_input()
        regular_deposit = get_float_input(f"Enter the regular deposit amount: ")
        years = get_int_input(
            "Enter the number of years: ",
            minimum=1,
            maximum=DEFAULT_PARAMETERS['max_years']
        )

        # Validate all inputs together
        if not validate_input_parameters(
                initial_amount, interest_rate, years, interval, regular_deposit
        ):
            continue

        # Calculate compound interest
        data = calculate_compound_interest(
            initial_amount, interest_rate, years, interval, regular_deposit
        )

        # Calculate summary statistics
        summary = calculate_summary_statistics(data)

        # Display results
        display_results(summary)

        # Ask if user wants to save the data
        save_data = get_yes_no_input("\nDo you want to save the data?")
        if save_data == 'y':
            save_results(data, initial_amount, interest_rate, interval, regular_deposit)

        # Ask if user wants to perform another calculation
        another_calculation = get_yes_no_input("Do you want to do another calculation?")
        if another_calculation != 'y':
            print("\nThank you for using the Compound Interest Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()