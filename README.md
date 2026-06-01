# ✈️ Study Abroad Daily Budget Planner

A smart, interactive web application built with Python to help international and exchange students manage their finances. This tool solves a common problem: tracking an overall budget in a home currency (e.g., KRW) while dynamically converting it to a local host currency (e.g., USD, JPY, EUR) for daily spending.

It breaks down your total funds over a custom timeline (days, weeks, semesters) to provide a strict **maximum daily allowance** alongside realistic, student-focused spending recommendations.

---

## 🚀 Key Features

- **Multi-Currency Support:** Input your total budget in your home currency and see your daily allowance calculated in your destination country's currency.
- **Live Exchange Rates:** Integrates with the free, open-source **Frankfurter API** to fetch accurate, real-time currency conversion rates.
- **Flexible Timelines:** Supports customizable tracking periods, from a few weekend days to a full academic semester or year.
- **Smart Student Allocations:** Automatically splits your daily allowance into crucial categories (40% Food/Drinks, 15% Transport, 20% Leisure, and a 25% Emergency Savings Buffer).
- **Interactive Cloud Execution:** Optimized to run seamlessly in the cloud using **Google Colab** paired with secure tunneling tools.

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Web Framework:** [Streamlit](https://streamlit.io/) (for building the interactive frontend dashboard)
- **API Requests:** `requests` library (for communicating with external REST APIs)
- **Data Source:** [Frankfurter API](https://www.frankfurter.app/) (Currency exchange rates)
- **Deployment/Tunneling:** [Ngrok](https://ngrok.com/) or Localtunnel (for exposing the local Streamlit port via Google Colab)

---

## 🏃‍♂️ How to Run the Project

This project is fully optimized to run inside a **Google Colab Notebook**. Follow these steps to launch it:

### Prerequisite: Get a Free Ngrok Token
1. Sign up for a free account at [ngrok.com](https://ngrok.com/).
2. Copy your unique **Authtoken** from your Ngrok dashboard.

### Execution Steps
Execute the following steps inside separate cells in your Colab environment:

1. **Install required packages:**
   ```bash
   !pip install streamlit requests pyngrok
