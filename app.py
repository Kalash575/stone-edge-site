
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stone Edge Capital", layout="centered")

# Logo and Title
st.markdown("<div style='image-align:center;'>", unsafe_allow_html=True)
st.image("logo.png", width=140)
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>STONE EDGE CAPITAL</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #2c3e50;'>Founded in 2023 by Shantanu Jha and Kalash Mendole</h4>", unsafe_allow_html=True)

# About
st.subheader("ABOUT")
st.write("""
Stone Edge Capital is an independent, employee-free hedge fund. Currently, we are managing our own money. 
Operating with a lean, high-agility structure, the fund applies a research-driven, quant-enhanced investment strategy 
targeting momentum, technical patterns, and undervalued stocks. Built for performance and precision, Stone Edge Capital 
represents a new-age approach to active equity investing, blending discipline, data, and founder conviction.
""")

# Vision
st.subheader("VISION")
st.write("The goal is to generate high returns by addressing a diverse range of assets using unique investment strategies, minimizing risk, and maximizing investor value.")

# Strategy Highlights
st.subheader("STRATEGY HIGHLIGHTS")
st.markdown("- Deep dive fundamental analysis")
st.markdown("- Proper risk management")
st.markdown("- Basic technical triggers")

# Performance
st.subheader("PERFORMANCE")
performance_data = pd.DataFrame({
    'Year': ['2023', '2024', '2025'],
    'Returns (%)': [70, 350, 40]
})
fig, ax = plt.subplots()
ax.bar(performance_data['Year'], performance_data['Returns (%)'], color='#608da2')
ax.set_ylabel('Returns (%)')
ax.set_title('Year-wise Performance')
st.pyplot(fig)

# Disclaimer
st.subheader("DISCLAIMER")
st.write("Stone Edge Capital is not a SEBI-registered entity. We are currently operating as a proprietary fund, managing our own capital.")

# Founders
st.subheader("FOUNDERS")
st.markdown("**Shantanu Jha** – Founder, Research Analyst")
st.markdown("**Kalash Mendole** – Cofounder, Managing Finances")

# Contact
st.subheader("CONTACT US")
st.markdown("📧 shantanujhajha38@gmail.com")
st.markdown("📧 primewealth1729@gmail.COM")
