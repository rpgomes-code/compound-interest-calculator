"""
Visualization functions for the compound interest calculator.

This module contains functions for generating and saving various
types of visualizations for compound interest data.
"""
from typing import List, Dict, Union, Any, Optional
from pathlib import Path
import matplotlib.pyplot as plt

from compound_interest.constants import COLORS


def generate_graphs(
        data: List[Dict[str, Union[int, float]]],
        folder_path: Path
) -> None:
    """
    Generate and save visualization graphs based on the calculated data.

    This function creates three visualizations:
    1. Line chart showing growth over time
    2. Pie chart showing the breakdown of final amount
    3. Stacked bar chart showing yearly breakdown

    Args:
        data: The list of yearly data dictionaries from calculate_compound_interest
        folder_path: The folder path where graphs should be saved

    Returns:
        None

    Examples:
        >>> results = calculate_compound_interest(1000, 5, 30, 'M', 100)
        >>> graphs_folder = Path.cwd() / "investment_graphs"
        >>> generate_graphs(results, graphs_folder)
    """
    if not data:
        return

    # Extract data for plotting
    years = [entry['Year'] for entry in data]
    total_amounts = [entry['Total Amount'] for entry in data]
    total_invested = [entry['Total Invested'] for entry in data]
    interest_earned = [entry['Interest Earned'] for entry in data]

    # Create a folder to save the graphs
    graphs_folder = folder_path / 'graphs'
    graphs_folder.mkdir(exist_ok=True)

    # Generate and save line chart
    generate_line_chart(
        years,
        total_amounts,
        total_invested,
        interest_earned,
        graphs_folder / 'compound_interest_line_chart.png'
    )

    # Generate and save pie chart
    generate_pie_chart(
        total_invested[-1],
        interest_earned[-1],
        graphs_folder / 'compound_interest_pie_chart.png'
    )

    # Generate and save stacked bar chart
    generate_stacked_bar_chart(
        years,
        total_invested,
        interest_earned,
        graphs_folder / 'compound_interest_stacked_bar_chart.png'
    )


def generate_line_chart(
        years: List[int],
        total_amounts: List[float],
        total_invested: List[float],
        interest_earned: List[float],
        file_path: Path
) -> None:
    """
    Generate and save a line chart showing investment growth over time.

    Args:
        years: List of year numbers
        total_amounts: List of total amounts for each year
        total_invested: List of total invested amounts for each year
        interest_earned: List of interest earned for each year
        file_path: Where to save the chart

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.plot(years, total_amounts, label='Total Amount', color=COLORS['total'])
    plt.plot(years, total_invested, label='Total Invested', color=COLORS['invested'])
    plt.plot(years, interest_earned, label='Interest Earned', color=COLORS['interest'])
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Compound Interest Growth')
    plt.legend()
    plt.grid(True)
    plt.savefig(file_path)
    plt.close()


def generate_pie_chart(
        total_invested: float,
        interest_earned: float,
        file_path: Path
) -> None:
    """
    Generate and save a pie chart showing the breakdown of the final amount.

    Args:
        total_invested: The total amount invested
        interest_earned: The total interest earned
        file_path: Where to save the chart

    Returns:
        None
    """
    plt.figure(figsize=(8, 8))
    plt.pie(
        [total_invested, interest_earned],
        labels=['Invested Amount', 'Interest Earned'],
        autopct='%1.1f%%',
        colors=[COLORS['invested'], COLORS['interest']]
    )
    plt.title('Breakdown of Final Amount')
    plt.savefig(file_path)
    plt.close()


def generate_stacked_bar_chart(
        years: List[int],
        total_invested: List[float],
        interest_earned: List[float],
        file_path: Path
) -> None:
    """
    Generate and save a stacked bar chart showing yearly breakdown.

    Args:
        years: List of year numbers
        total_invested: List of total invested amounts for each year
        interest_earned: List of interest earned for each year
        file_path: Where to save the chart

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.bar(years, total_invested, label='Invested Amount', color=COLORS['invested'])
    plt.bar(years, interest_earned, bottom=total_invested, label='Interest Earned', color=COLORS['interest'])
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Compound Interest Growth (Stacked)')
    plt.legend()
    plt.savefig(file_path)
    plt.close()