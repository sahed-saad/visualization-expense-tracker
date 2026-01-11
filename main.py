import pandas as pd

# DataFrame is the primary object to store data similar to a programmable spreadsheet
df = pd.read_csv("C:/Users/sahed/Documents/expense_data_1.csv")

# Select only the necessary columns from the DataFrame
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]

def add_expense(date, category, note, amount, exp_type="Expense"):
    global data
    # 1. Create a tiny DataFrame for the new row
    new_entry = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Note": note,
        "Amount": amount,
        "Income/Expense": exp_type
    }])
    
    # 2. Use concat to glue the new_entry to the existing data
    data = pd.concat([data, new_entry], ignore_index=True)
    
    print(f" Added: {note} - {amount} ({category})")

add_expense("2025-08-22 19:30", "Food", "Shawarma", 2500, "Expense")
add_expense("2025-08-23 08:00", "Subscriptions", "Netflix Monthly Plan", 4500, "Expense")
add_expense("2025-08-24 14:00", "Entertainment", "Outdoor Games with friends", 7000, "Expense")

def view_expenses(n=5):
    return data.tail(n)
print(view_expenses(5))
add_expense("2026-01-10 14:00", "Entertainment", "Outdoor Games with friends", 7000, "Expense")

print(view_expenses(5))