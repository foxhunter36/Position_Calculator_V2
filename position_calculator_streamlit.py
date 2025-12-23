import streamlit as st

# Custom CSS für Neo/Matrix Look
st.markdown("""
<style>
    /* Hauptcontainer */
    .stApp {
        background-color: #000000;
    }
    
    /* Alle Text-Elemente */
    .stMarkdown, p, span, div {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Headers */
    h1 {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        text-align: center !important;
        letter-spacing: 3px;
        font-size: 2.5rem !important;
    }
    
    h2, h3 {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        letter-spacing: 2px;
    }
    
    /* Input Fields */
    .stNumberInput input {
        background-color: #0d1117 !important;
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Labels */
    label {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Button */
    .stButton button {
        background-color: #0d1117 !important;
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #00ff41 !important;
        letter-spacing: 2px;
    }
    
    .stButton button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00ff41 !important;
    }
    
    /* Success/Error boxes */
    .stSuccess, .stError {
        background-color: #0d1117 !important;
        border: 1px solid #00ff41 !important;
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        text-align: center !important;
    }
    
    /* Dividers */
    hr {
        border-color: #00ff41 !important;
        opacity: 0.3 !important;
    }
    
    /* Caption */
    .stCaption {
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        opacity: 0.7;
    }
</style>

<script>
    // Auto-focus next input on Enter
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            const inputs = Array.from(document.querySelectorAll('input[type="number"]'));
            const currentIndex = inputs.indexOf(document.activeElement);
            if (currentIndex > -1 && currentIndex < inputs.length - 1) {
                e.preventDefault();
                inputs[currentIndex + 1].focus();
            }
        }
    });
</script>
""", unsafe_allow_html=True)

st.title("POSITION CALC")

# Inputs
st.subheader("SYSTEM INPUT")
col1, col2 = st.columns(2)
with col1:
    capital = st.number_input("ACCOUNT SIZE", min_value=0.0, value=0.0, step=100.0, key="capital", format="%.2f")
with col2:
    risk_pct = st.number_input("RISK PERCENTAGE", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="risk", format="%.2f")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    entry_price = st.number_input("ENTRY PRICE", min_value=0.0, value=0.0, step=0.01, key="entry", format="%.2f")
    tp1_price = st.number_input("TARGET 1", min_value=0.0, value=0.0, step=0.01, key="tp1", format="%.2f")
    tp3_price = st.number_input("TARGET 3", min_value=0.0, value=0.0, step=0.01, key="tp3", format="%.2f")
with col2:
    sl_price = st.number_input("STOP LOSS", min_value=0.0, value=0.0, step=0.01, key="sl", format="%.2f")
    tp2_price = st.number_input("TARGET 2", min_value=0.0, value=0.0, step=0.01, key="tp2", format="%.2f")

# Calculate Button
if st.button("EXECUTE CALCULATION", type="primary", use_container_width=True):
    
    # Check if all fields are filled
    if capital == 0.0 or risk_pct == 0.0 or entry_price == 0.0 or sl_price == 0.0 or tp1_price == 0.0 or tp2_price == 0.0 or tp3_price == 0.0:
        st.error("ERROR: INCOMPLETE DATA")
        st.stop()
    
    # Erkenne ob Long oder Short
    if tp3_price > entry_price:
        trade_direction = "LONG"
        is_long = True
    elif tp3_price < entry_price:
        trade_direction = "SHORT"
        is_long = False
    else:
        st.error("ERROR: INVALID TARGET CONFIGURATION")
        st.stop()
    
    # Validiere SL Position
    if is_long and sl_price >= entry_price:
        st.error("ERROR: INVALID STOP LOSS FOR LONG POSITION")
        st.stop()
    elif not is_long and sl_price <= entry_price:
        st.error("ERROR: INVALID STOP LOSS FOR SHORT POSITION")
        st.stop()
    
    # Validiere TP Reihenfolge
    if is_long:
        if tp1_price <= entry_price or tp2_price <= entry_price or tp3_price <= entry_price:
            st.error("ERROR: TARGETS MUST EXCEED ENTRY FOR LONG")
            st.stop()
        if not (tp1_price < tp2_price < tp3_price):
            st.error("ERROR: TARGETS MUST BE IN ORDER: TP1 < TP2 < TP3")
            st.stop()
    else:
        if tp1_price >= entry_price or tp2_price >= entry_price or tp3_price >= entry_price:
            st.error("ERROR: TARGETS MUST BE BELOW ENTRY FOR SHORT")
            st.stop()
        if not (tp1_price > tp2_price > tp3_price):
            st.error("ERROR: TARGETS MUST BE IN ORDER: TP1 > TP2 > TP3")
            st.stop()
    
    # Berechne SL und TP in Prozent
    sl_distance = abs((entry_price - sl_price) / entry_price) * 100
    tp1_distance = abs((tp1_price - entry_price) / entry_price) * 100
    tp2_distance = abs((tp2_price - entry_price) / entry_price) * 100
    tp3_distance = abs((tp3_price - entry_price) / entry_price) * 100
    
    # ECHTES Risk/Reward mit 33/33/33 Split
    tp1_profit_pct = tp1_distance * 0.33
    tp2_profit_pct = tp2_distance * 0.33
    tp3_profit_pct = tp3_distance * 0.33
    
    # Echtes R/R
    risk_reward_tp1 = tp1_profit_pct / sl_distance
    risk_reward_tp2 = tp2_profit_pct / sl_distance
    risk_reward_tp3 = tp3_profit_pct / sl_distance
    
    # Position Size Berechnung
    risk_amount = capital * (risk_pct / 100)
    position_size = risk_amount / (sl_distance / 100)
    
    # Berechne benötigte Margin und Leverage
    if position_size <= capital:
        margin = position_size
        leverage = 1.0
    else:
        margin = capital
        leverage = position_size / capital
    
    # Potentielle Gewinne/Verluste
    potential_loss = risk_amount
    profit_at_tp1 = (position_size * 0.33) * (tp1_distance / 100)
    profit_at_tp2 = (position_size * 0.33) * (tp2_distance / 100)
    profit_at_tp3 = (position_size * 0.34) * (tp3_distance / 100)  # 0.34 wegen rounding
    potential_profit_total = profit_at_tp1 + profit_at_tp2 + profit_at_tp3
    avg_risk_reward = (risk_reward_tp1 + risk_reward_tp2 + risk_reward_tp3) / 3
    
    # Output
    st.markdown("---")
    
    # Trade Analysis mit Direction rechts
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**TRADE ANALYSIS**")
    with col2:
        st.markdown(f"**DIRECTION: {trade_direction}**")
    
    # Entry und SL in 2 Spalten
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"ENTRY: `${entry_price:.2f}`")
    with col2:
        st.markdown(f"SL: `${sl_price:.2f} ({sl_distance:.2f}%)`")
    
    # Target 1, 2, 3 in 3 Spalten
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"TARGET 1 [33%]: `${tp1_price:.2f} ({tp1_distance:.2f}%)`")
        st.markdown(f"RR: `1:{risk_reward_tp1:.2f}`")
    with col2:
        st.markdown(f"TARGET 2 [33%]: `${tp2_price:.2f} ({tp2_distance:.2f}%)`")
        st.markdown(f"RR: `1:{risk_reward_tp2:.2f}`")
    with col3:
        st.markdown(f"TARGET 3 [34%]: `${tp3_price:.2f} ({tp3_distance:.2f}%)`")
        st.markdown(f"RR: `1:{risk_reward_tp3:.2f}`")
    
    st.markdown(f"**AVERAGE RISK/REWARD: `1:{avg_risk_reward:.2f}`**")
    
    st.markdown("---")
    
    # Position Details
    st.markdown("**POSITION CONFIGURATION**")
    st.markdown(f"MARGIN: `${margin:.2f}` | LEVERAGE: `{leverage:.2f}x` | POSITION SIZE: `${position_size:.2f}`")
    
    st.markdown("---")
    
    # P&L
    st.markdown("**PROFIT & LOSS PROJECTION**")
    st.markdown(f"MAX LOSS: `${potential_loss:.2f}` | TP1: `${profit_at_tp1:.2f}` | TP2: `${profit_at_tp2:.2f}` | TP3: `${profit_at_tp3:.2f}`")
    st.markdown(f"TOTAL PROFIT: `${potential_profit_total:.2f}`")
    
    # Warnings kompakt
    warnings = []
    if avg_risk_reward < 2:
        warnings.append("WARNING: SUBOPTIMAL RISK/REWARD RATIO")
    if leverage > 10:
        warnings.append("WARNING: EXCESSIVE LEVERAGE DETECTED")
    if leverage > 1:
        warnings.append(f"INFO: LEVERAGE ACTIVE [{leverage:.2f}x]")
    
    if warnings:
        st.markdown("---")
        st.caption(" | ".join(warnings))
    
    # TRADE RECOMMENDATION
    st.markdown("---")
    
    if avg_risk_reward >= 2:
        st.success("STATUS: TRADE APPROVED - PROCEED WITH EXECUTION")
    else:
        st.error(f"STATUS: TRADE REJECTED - INSUFFICIENT RISK/REWARD [1:{avg_risk_reward:.2f}]")