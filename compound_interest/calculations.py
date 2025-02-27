"""
Calculation functions for the compound interest calculator.

This module contains the core calculation logic for determining
compound interest growth over time with regular deposits.
"""
from typing import List, Dict, Union, Any
from compound_interest.constants import INTERVALS


def calculate_compound_interest(
        initial_amount: float,
        interest_rate: float,
        years: int,
        interval: str,
        regular_deposit: float
) -> List[Dict[str, Union[int, float]]]:
    """
    Calculate compound interest with regular deposits over a period of years.

    This function simulates the growth of an investment over time, accounting for:
    - Initial principal amount
    - Regular deposits at specified intervals
    - Compound interest applied at the same intervals

    Args:
        initial_amount: The starting investment amount
        interest_rate: The annual interest rate percentage
        years: The investment time period in years
        interval: The deposit interval code ('D'=daily, 'W'=weekly, 'M'=monthly, 'Y'=yearly)
        regular_deposit: The amount deposited at each interval

    Returns:
        A list of dictionaries, each containing yearly data with keys:
        - 'Year': The year number (1-based)
        - 'Total Amount': The total value at the end of that year
        - 'Total Invested': The total amount invested by the end of that year
        - 'Interest Earned': The cumulative interest earned by the end of that year

    Examples:
        >>> # Calculate returns for $1000 initial with $100 monthly deposits at 5% for 30 years
        >>> results = calculate_compound_interest(1000, 5, 30, 'M', 100)
        >>> print(f"Final amount after 30 years: ${results[-1]['Total Amount']:,.2f}")
    """
    total_amount = initial_amount
    total_invested = initial_amount
    data = []

    # Get the number of compounding periods per year based on the interval
    intervals_per_year = INTERVALS[interval]['periods']

    # Calculate the interest rate per period
    rate_per_period = interest_rate / 100 / intervals_per_year

    # Loop through each year to calculate compound interest
    for year in range(1, years + 1):
        # Apply compound interest and deposits for each period in the year
        for _ in range(intervals_per_year):
            # Apply interest for this period
            total_amount *= (1 + rate_per_period)
            # Add the regular deposit
            total_amount += regular_deposit
            # Track the total amount invested
            total_invested += regular_deposit

        # Store the yearly data
        data.append({
            'Year': year,
            'Total Amount': round(total_amount, 2),
            'Total Invested': round(total_invested, 2),
            'Interest Earned': round(total_amount - total_invested, 2)
        })

    return data


def format_currency(value: float) -> str:
    """
    Format a numeric value as a currency string.

    Args:
        value: The numeric value to format

    Returns:
        A formatted string with currency symbol, thousands separators, and 2 decimal places

    Examples:
        >>> format_currency(1234567.89)
        '$1,234,567.89'
    """
    return f"${value:,.2f}"


def calculate_summary_statistics(data: List[Dict[str, Union[int, float]]]) -> Dict[str, Any]:
    """
    Calculate summary statistics from the compound interest data.

    Args:
        data: The list of yearly data dictionaries from calculate_compound_interest

    Returns:
        A dictionary containing various summary statistics of the investment

    Examples:
        >>> results = calculate_compound_interest(1000, 5, 30, 'M', 100)
        >>> stats = calculate_summary_statistics(results)
        >>> print(f"Total return on investment: {stats['roi_percentage']}%")
    """
    if not data:
        return {}

    final_year = data[-1]
    total_invested = final_year['Total Invested']
    total_interest = final_year['Interest Earned']
    final_amount = final_year['Total Amount']

    # Calculate return on investment
    roi = (total_interest / total_invested) * 100

    # Calculate compound annual growth rate (CAGR)
    years = len(data)
    cagr = ((final_amount / total_invested) ** (1 / years) - 1) * 100

    return {
        'total_invested': total_invested,
        'total_interest': total_interest,
        'final_amount': final_amount,
        'roi_percentage': round(roi, 2),
        'cagr_percentage': round(cagr, 2),
        'years': years,
        'interest_to_investment_ratio': round(total_interest / total_invested, 2)
    }