import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from processor import auto_categorize

logo_path = os.path.join("src", "logo.svg")

st.set_page_config(
    page_title="Sahed's Expense Tracker",
    page_icon=logo_path if os.path.exists(logo_path) else ""
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if os.path.exists(logo_path):
    st.image(logo_path, width=100)

csv_file = "expense.csv"
if os.path.exists(csv_file):
    data = pd.read_csv(csv_file)
else:
    data = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

# Main Interface
st.title("Visualization Expense Tracker")

with st.form("expense_form"):
    st.write("### Add New Transaction")
    date = st.date_input("Date")
    description = st.text_input("Description (e.g., Netflix, Shawarma)")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    # Use the logic from processor.py to predict category
    predicted_category = ""
    if description:
        predicted_category = auto_categorize(description)

    category = st.text_input(
        "Category (auto-predicted, but you can edit)", 
        value=predicted_category
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = {
            "Date": date,
            "Category": category,
            "Amount": amount,  
            "Description": description
        }
        # Use concat for Pandas
        data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
        data.to_csv(csv_file, index=False)
        st.success(f"Successfully added: {description}")

# Data Table
st.subheader("All Expenses")
st.dataframe(data)

# Charts
if not data.empty:
    st.subheader("Expense Breakdown by Category")

    category_totals = data.groupby("Category")["Amount"].sum()

    # Bar Chart
    fig, ax = plt.subplots()
    category_totals.plot(kind="bar", ax=ax)
    ax.set_ylabel("Amount")
    st.pyplot(fig)

    # Pie Chart
    st.subheader("Category Distribution")
    fig2, ax2 = plt.subplots()
    category_totals.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    plt.ylabel("")
    st.pyplot(fig2)

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: grey;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #e6e6e6;
    }
    </style>
    <div class="footer">
        <p>© 2026 Saad</p>
    </div>
    """, unsafe_allow_html=True)