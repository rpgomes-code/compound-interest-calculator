"""
Input handlers for the compound interest calculator.

This module contains functions for user input validation and collection,
ensuring that user inputs meet the requirements for calculations.
"""
from typing import Union, Callable, TypeVar, Any, List

from compound_interest.constants import INTERVAL_OPTIONS, INTERVAL_CODES

T = TypeVar('T')  # Generic type for return values


def get_float_input(prompt: str, minimum: float = 0.0) -> float:
    """
    Get a valid float input from the user that is not less than the minimum value.

    Args:
        prompt: The message to display to the user
        minimum: The minimum acceptable value (default: 0.0)

    Returns:
        A valid float value entered by the user

    Examples:
        >>> # This will prompt the user until they enter a valid non-negative float
        >>> initial_amount = get_float_input("Enter the initial amount: ")
    """
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print(f"Error: Please enter a number not less than {minimum}.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")


def get_int_input(prompt: str, minimum: int = 1, maximum: int = None) -> int:
    """
    Get a valid integer input from the user within the specified range.

    Args:
        prompt: The message to display to the user
        minimum: The minimum acceptable value (default: 1)
        maximum: The maximum acceptable value (default: None)

    Returns:
        A valid integer value entered by the user

    Examples:
        >>> # This will prompt the user until they enter a positive integer
        >>> years = get_int_input("Enter the number of years: ")
    """
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Error: Please enter a number not less than {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Error: Please enter a number not greater than {maximum}.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_interval_input() -> str:
    """
    Get the deposit interval selection from the user.

    Returns:
        A single character code representing the selected interval:
        'D' for Daily, 'W' for Weekly, 'M' for Monthly, 'Y' for Yearly

    Examples:
        >>> # This will prompt the user to select from a list of intervals
        >>> interval = get_interval_input()
    """
    while True:
        print("\nSelect the regular deposit interval:")
        for i, option in enumerate(INTERVAL_OPTIONS, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return INTERVAL_CODES[choice - 1]
            else:
                print("Error: Please enter a number between 1 and 4.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_yes_no_input(prompt: str) -> str:
    """
    Get a yes or no response from the user.

    Args:
        prompt: The question to ask the user

    Returns:
        'y' for yes or 'n' for no

    Examples:
        >>> # This will prompt the user until they enter 'y' or 'n'
        >>> save_data = get_yes_no_input("Do you want to save the data?")
    """
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Error: Please enter 'y' for Yes or 'n' for No.")


def validate_input_parameters(
        initial_amount: float,
        interest_rate: float,
        years: int,
        interval: str,
        regular_deposit: float
) -> bool:
    """
    Validate that all input parameters are within acceptable ranges.

    Args:
        initial_amount: The starting investment amount
        interest_rate: The annual interest rate percentage
        years: The investment time period in years
        interval: The deposit interval code
        regular_deposit: The regular deposit amount

    Returns:
        True if all parameters are valid, False otherwise

    Examples:
        >>> valid = validate_input_parameters(1000, 5.5, 30, 'M', 100)
    """
    if initial_amount < 0:
        print("Error: Initial amount cannot be negative.")
        return False

    if interest_rate < 0 or interest_rate > 100:
        print("Error: Interest rate must be between 0 and 100.")
        return False

    if years <= 0 or years > 100:
        print("Error: Years must be between 1 and 100.")
        return False

    if interval not in INTERVAL_CODES:
        print("Error: Invalid interval code.")
        return False

    if regular_deposit < 0:
        print("Error: Regular deposit cannot be negative.")
        return False

    return True