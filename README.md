# Compound Interest Calculator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

A powerful and user-friendly compound interest calculator built with Python. This tool helps you calculate the growth of your investments over time, taking into account regular deposits and compound interest.

## 🌟 Features

- Calculate compound interest with customizable parameters
- Support for different deposit intervals (Daily, Weekly, Monthly, Yearly)
- Generate visualizations of your investment growth
- Export results to Excel and CSV formats
- Interactive command-line interface

## 📊 Visualizations

The calculator generates three types of graphs:

1. **Line Chart**: Shows the growth of Total Amount, Total Invested, and Interest Earned over time.
2. **Pie Chart**: Displays the breakdown of the final amount (Invested Amount vs. Interest Earned).
3. **Stacked Bar Chart**: Illustrates the yearly breakdown of Invested Amount and Interest Earned.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/rpgomes-code/compound-interest-calculator.git
   cd compound-interest-calculator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## 💻 Usage

Run the calculator with the following command:

```
python main.py
```

Follow the prompts to input your investment details:

- Initial amount
- Yearly interest percentage
- Regular deposit interval
- Regular deposit amount
- Number of years

The calculator will display the results and offer to save the data and generate graphs.

## 📁 Output

When you choose to save the data, the calculator creates a new folder with:

- An Excel file (`compound_interest_data.xlsx`)
- A CSV file (`compound_interest_data.csv`)
- A `graphs` subfolder containing:
  - Line chart (`compound_interest_line_chart.png`)
  - Pie chart (`compound_interest_pie_chart.png`)
  - Stacked bar chart (`compound_interest_stacked_bar_chart.png`)

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/) for data visualization
- [Pandas](https://pandas.pydata.org/) for data manipulation and Excel export

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/rpgomes-code/compound-interest-calculator/issues).

## 👨‍💻 Author

**Rui Gomes**

- GitHub: [@rpgomes](https://github.com/rpgomes-code)
- LinkedIn: [Rui Gomes](www.linkedin.com/in/rpgomes-lk)

---

⭐️ If you find this project useful, please consider giving it a star on GitHub! ⭐️
