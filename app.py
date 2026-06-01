import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Study Abroad Budget Planner", page_icon="✈️", layout="centered")
st.title("✈️ Study Abroad Daily Budget Planner")
st.write("Manage your home budget while living and spending overseas.")

# --- Sidebar Workflow ---

# Step 1: Destination Selection
st.sidebar.header("🌍 Step 1: Destination")
country_currency_map = {
    "United States": "USD",
    "United Kingdom": "GBP",
    "France": "EUR",
    "Germany": "EUR",
    "Spain": "EUR",
    "Italy": "EUR",
    "Japan": "JPY",
    "South Korea": "KRW",
    "Vietnam": "VND",
    "Singapore": "SGD",
    "Australia": "AUD",
    "Canada": "CAD",
    "China": "CNY",
    "India": "INR",
    "Kazakhstan": "KZT",
    "Mongolia": "MNT"
}
destination_country = st.sidebar.selectbox("Where are you studying?", list(country_currency_map.keys()))
# Auto-detect expense currency
expense_currency = country_currency_map[destination_country]

# Step 2: Financial Setup
st.sidebar.header("🎛️ Step 2: Financial Setup")
# Added KZT and MNT here as requested
budget_currency = st.sidebar.selectbox("Your Home Budget Currency", ["KRW", "USD", "EUR", "GBP", "JPY", "SGD", "AUD", "CAD", "CHF", "CNY", "INR", "NZD", "HKD", "KZT", "MNT"])
total_budget = st.sidebar.number_input(f"Total Budget Amount ({budget_currency})", min_value=1.0, value=1000.0, step=50.0)

# Show detected currency
st.sidebar.info(f"📍 Currency for {destination_country}: **{expense_currency}**")

# Step 3: Timeline
st.sidebar.header("📅 Step 3: Timeline")
col_qty, col_unit = st.sidebar.columns([1, 1])
with col_qty:
    timeline_qty = st.number_input("Duration", min_value=1, value=1)
with col_unit:
    timeline_unit = st.selectbox("Unit", ["Days", "Weeks", "Months", "Years"])

if timeline_unit == "Days":
    total_days = timeline_qty
elif timeline_unit == "Weeks":
    total_days = timeline_qty * 7
elif timeline_unit == "Months":
    total_days = timeline_qty * 30
else: # Years
    total_days = timeline_qty * 365

# --- Calculations ---

@st.cache_data
def get_exchange_rate(base, target):
    if base == target:
        return 1.0
    try:
        url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
        response = requests.get(url)
        return response.json()["rates"][target]
    except:
        return None

rate = get_exchange_rate(budget_currency, expense_currency)

if rate is None:
    st.warning(f"Live rates for {expense_currency} are currently unavailable on this API. Using a mock conversion rate of 1.0 for demonstration.")
    rate = 1.0

total_budget_in_expense_currency = total_budget * rate
daily_allowance_expense_curr = total_budget_in_expense_currency / total_days

def fmt(amount, currency):
    if currency in ["KRW", "JPY", "VND", "INR", "CNY", "KZT", "MNT"]:
        return f"{int(amount):,}" + f" {currency}"
    return f"{amount:,.2f} {currency}"

st.markdown("---")
st.header(f"📊 Daily Allowance in {destination_country}")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Value Overseas", fmt(total_budget_in_expense_currency, expense_currency))
    st.caption(f"From {fmt(total_budget, budget_currency)} over {total_days} days")
with col2:
    st.metric("👉 Daily Max", fmt(daily_allowance_expense_curr, expense_currency))
    st.caption(f"Your target budget in {expense_currency}")

st.markdown("---")
st.header("💡 Recommended Daily Targets")

food_target = daily_allowance_expense_curr * 0.40
leisure_target = daily_allowance_expense_curr * 0.20
transport_target = daily_allowance_expense_curr * 0.15
savings_target = daily_allowance_expense_curr * 0.25

c1, c2, c3, c4 = st.columns(4)
c1.metric("🍏 Food", fmt(food_target, expense_currency))
c2.metric("🚌 Transport", fmt(transport_target, expense_currency))
c3.metric("🎉 Leisure", fmt(leisure_target, expense_currency))
c4.metric("🛡️ Buffer", fmt(savings_target, expense_currency))

st.markdown("---")
st.header("📌 Smart Ways to Save Abroad")

tabs = st.tabs(["🎓 Student Perks", "🛒 Food & Grocery", "💳 Banking & FX"])

with tabs[0]:
    st.markdown("**Get an ISIC Card:** Apply for an International Student Identity Card for discounts in your host country.")

with tabs[1]:
    st.markdown("**Local Markets:** Shop at local bazaars or markets for the best prices on fresh produce.")
    st.markdown(f"**Cook in Bulk:** Eating out in {expense_currency} is expensive!")

with tabs[2]:
    st.markdown(f"**Pay in Local Currency:** Always choose {expense_currency} on card machines to avoid bad conversion rates.")
    st.markdown("**Travel Cards:** Use digital banks like Wise or Revolut for better FX rates.")

st.success(f"💪 **Emergency Buffer:** By saving your buffer daily, you'll have **{fmt(savings_target * total_days, expense_currency)}** extra by the end!")
