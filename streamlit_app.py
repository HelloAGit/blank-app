import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Streamlit UI
st.title("📈 Daily Sales Probability Estimator")

st.markdown("""
Estimate the expected range of your e-commerce daily sales for tomorrow and the next week based on historical averages.
""")

mean_sales = st.number_input("Mean daily sales (last 3 months)", min_value=0.0, value=5000.0, step=100.0)
std_sales = st.number_input("Standard deviation of daily sales", min_value=0.0, value=1000.0, step=100.0)
confidence_level = st.slider("Confidence Interval (%)", 50, 99, 95)
z_score = norm.ppf(1 - (1 - confidence_level / 100) / 2)

# Single-day forecast
lower_bound = mean_sales - z_score * std_sales
upper_bound = mean_sales + z_score * std_sales

st.subheader("🔍 Next Day Sales Estimate")
st.write(f"With {confidence_level}% confidence, tomorrow's sales are expected to be between **${lower_bound:,.2f}** and **${upper_bound:,.2f}**.")

simulated_sales = np.random.normal(loc=mean_sales, scale=std_sales, size=10000)
weekly_projection = [np.random.choice(simulated_sales, size=7).sum() for _ in range(10000)]

st.subheader("📊 7-Day Sales Projection")
st.write(f"Estimated total sales over the next 7 days (based on simulations):")
st.write(f"- **Mean:** ${np.mean(weekly_projection):,.2f}")
st.write(f"- **{confidence_level}% Confidence Interval:** ${np.percentile(weekly_projection, (100 - confidence_level) / 2):,.2f} to ${np.percentile(weekly_projection, 100 - (100 - confidence_level) / 2):,.2f}")

# Plotting the 7-day projection distribution
fig, ax = plt.subplots()
ax.hist(weekly_projection, bins=50, color='skyblue', edgecolor='black')
ax.axvline(np.mean(weekly_projection), color='red', linestyle='dashed', linewidth=1.5, label='Mean')
ax.set_title("Simulated 7-Day Sales Distribution")
ax.set_xlabel("Total Sales ($)")
ax.set_ylabel("Frequency")
ax.legend()

st.pyplot(fig)
