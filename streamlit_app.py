import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Streamlit UI
st.title("📈 Daily Sales Probability Estimator")

st.markdown("""
Estimate the expected range of your e-commerce daily sales for tomorrow and the next week based on historical averages.
""")
