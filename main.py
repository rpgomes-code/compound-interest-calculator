import datetime
import os
import matplotlib.pyplot as plt
import pandas as pd
import csv

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_interval_input():
    options = [
        "Daily",
        "Weekly",
        "Monthly",
        "Yearly"
    ]
    while True:
        print("\nSelect the regular deposit interval:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return ['D', 'W', 'M', 'Y'][choice - 1]
            else:
                print("Error: Please enter a number between 1 and 4.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_yes_no_input(prompt):
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Error: Please enter 'y' for Yes or 'n' for No.")

def calculate_compound_interest(initial_amount, interest_rate, years, interval, regular_deposit):
    total_amount = initial_amount
    total_invested = initial_amount
    data = []
    
    intervals_per_year = {
        'D': 365,
        'W': 52,
        'M': 12,
        'Y': 1
    }
    
    for year in range(1, years + 1):
        for _ in range(intervals_per_year[interval]):
            total_amount *= (1 + interest_rate / 100 / intervals_per_year[interval])
            total_amount += regular_deposit
            total_invested += regular_deposit
        
        data.append({
            'Year': year,
            'Total Amount': round(total_amount, 2),
            'Total Invested': round(total_invested, 2),
            'Interest Earned': round(total_amount - total_invested, 2)
        })
    
    return data

def generate_graphs(data, folder_path):
    years = [entry['Year'] for entry in data]
    total_amounts = [entry['Total Amount'] for entry in data]
    total_invested = [entry['Total Invested'] for entry in data]
    interest_earned = [entry['Interest Earned'] for entry in data]

    # Color scheme with specified hex codes
    color_interest = '#55a630'
    color_invested = '#e09f3e'
    color_total = '#0096c7'

    # Create graphs folder
    graphs_folder = os.path.join(folder_path, 'graphs')
    os.makedirs(graphs_folder, exist_ok=True)

    # Line chart
    plt.figure(figsize=(12, 6))
    plt.plot(years, total_amounts, label='Total Amount', color=color_total)
    plt.plot(years, total_invested, label='Total Invested', color=color_invested)
    plt.plot(years, interest_earned, label='Interest Earned', color=color_interest)
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Compound Interest Growth')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(graphs_folder, 'compound_interest_line_chart.png'))
    plt.close()

    # Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie([total_invested[-1], interest_earned[-1]], 
            labels=['Invested Amount', 'Interests Earned'], 
            autopct='%1.1f%%', 
            colors=[color_invested, color_interest])
    plt.title('Breakdown of Final Amount')
    plt.savefig(os.path.join(graphs_folder, 'compound_interest_pie_chart.png'))
    plt.close()

    # Stacked bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(years, total_invested, label='Invested Amount', color=color_invested)
    plt.bar(years, interest_earned, bottom=total_invested, label='Interests Earned', color=color_interest)
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Compound Interest Growth (Stacked)')
    plt.legend()
    plt.savefig(os.path.join(graphs_folder, 'compound_interest_stacked_bar_chart.png'))
    plt.close()

def save_to_excel(data, folder_path):
    df = pd.DataFrame(data)
    df.to_excel(os.path.join(folder_path, 'compound_interest_data.xlsx'), index=False)

def save_to_csv(data, folder_path):
    csv_path = os.path.join(folder_path, 'compound_interest_data.csv')
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Year', 'Total Amount', 'Total Invested', 'Interest Earned']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def format_currency(value):
    return f"${value:,.2f}"

def main():
    while True:
        initial_amount = get_float_input("Enter the initial amount: ")
        interest_rate = get_float_input("Enter the yearly interest percentage: ")
        interval = get_interval_input()
        regular_deposit = get_float_input("Enter the regular deposit amount: ")
        years = get_int_input("Enter the number of years: ")

        data = calculate_compound_interest(initial_amount, interest_rate, years, interval, regular_deposit)

        total_invested = data[-1]['Total Invested']
        total_interest = data[-1]['Interest Earned']
        final_amount = data[-1]['Total Amount']

        print(f"\nTotal amount invested: {format_currency(total_invested)}")
        print(f"Total amount in interest: {format_currency(total_interest)}")
        print(f"Final Amount: {format_currency(final_amount)}")

        save_data = get_yes_no_input("\nDo you want to save the data?")

        if save_data == 'y':
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            folder_name = f"{initial_amount}_{interest_rate}_{interval}_{regular_deposit}_{timestamp}"
            folder_path = os.path.join(os.getcwd(), folder_name)
            os.makedirs(folder_path, exist_ok=True)

            generate_graphs(data, folder_path)
            save_to_excel(data, folder_path)
            save_to_csv(data, folder_path)
            print(f"Data and graphs saved in folder: {folder_name}")
            print(f"Files generated: compound_interest_data.xlsx, compound_interest_data.csv, and graph images")

        another_calculation = get_yes_no_input("Do you want to do another calculation?")
        if another_calculation != 'y':
            print("Thank you for using the Compound Interest Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()