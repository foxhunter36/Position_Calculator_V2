import streamlit as st

st.title("Trading Position Size Calculator")

capital = st.number_input("Account Size", min_value=0.0, value=3000.0, step=100.0)
risk_pct = st.number_input("Accepted Risk in %", min_value=0.0, value=5.0, step=0.5)
sl_pct = st.number_input("Trade SL in %", min_value=0.01, value=0.5, step=0.1)

margin = capital
leverage = risk_pct / sl_pct if sl_pct != 0 else 0
position_size = margin * leverage

st.subheader("Position Size")
st.write(f"Margin: **{margin:.2f}**")
st.write(f"Leverage: **{leverage:.2f}**")
st.write(f"Position Size: **{position_size:.2f}**")
