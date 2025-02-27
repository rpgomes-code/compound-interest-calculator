"""
Constants used throughout the compound interest calculator.

This module contains all constants and configuration values
used by the compound interest calculator to ensure consistency
and ease of modification across the application.
"""
from typing import Dict, List, Tuple

# Deposit interval definitions
INTERVALS: Dict[str, Dict[str, any]] = {
    'D': {'name': 'Daily', 'periods': 365},
    'W': {'name': 'Weekly', 'periods': 52},
    'M': {'name': 'Monthly', 'periods': 12},
    'Y': {'name': 'Yearly', 'periods': 1}
}

# Interval options for user selection
INTERVAL_OPTIONS: List[str] = ['Daily', 'Weekly', 'Monthly', 'Yearly']
INTERVAL_CODES: List[str] = ['D', 'W', 'M', 'Y']

# Chart colors
COLORS: Dict[str, str] = {
    'interest': '#55a630',  # Green
    'invested': '#e09f3e',  # Orange/Gold
    'total': '#0096c7'      # Blue
}

# Default parameters
DEFAULT_PARAMETERS: Dict[str, any] = {
    'min_amount': 0,
    'max_years': 100,
    'min_interest_rate': 0,
    'max_interest_rate': 100
}