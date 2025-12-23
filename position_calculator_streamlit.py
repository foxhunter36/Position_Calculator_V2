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

# TP Level Selection
tp_count = st.selectbox("NUMBER OF TAKE-PROFIT LEVELS", options=[2, 3, 4], index=1, key="tp_count")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    entry_price = st.number_input("ENTRY PRICE", min_value=0.0, value=0.0, step=0.01, key="entry", format="%.2f")
with col2:
    sl_price = st.number_input("STOP LOSS", min_value=0.0, value=0.0, step=0.01, key="sl", format="%.2f")

# Dynamic TP inputs based on selection
st.markdown("---")
st.subheader("TARGET LEVELS")

if tp_count == 2:
    col1, col2 = st.columns(2)
    with col1:
        tp1_price = st.number_input("TARGET 1 [50%]", min_value=0.0, value=0.0, step=0.01, key="tp1", format="%.2f")
    with col2:
        tp2_price = st.number_input("TARGET 2 [50%]", min_value=0.0, value=0.0, step=0.01, key="tp2", format="%.2f")
    tp3_price = None
    tp4_price = None
elif tp_count == 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        tp1_price = st.number_input("TARGET 1 [33%]", min_value=0.0, value=0.0, step=0.01, key="tp1", format="%.2f")
    with col2:
        tp2_price = st.number_input("TARGET 2 [33%]", min_value=0.0, value=0.0, step=0.01, key="tp2", format="%.2f")
    with col3:
        tp3_price = st.number_input("TARGET 3 [34%]", min_value=0.0, value=0.0, step=0.01, key="tp3", format="%.2f")
    tp4_price = None
else:  # tp_count == 4
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        tp1_price = st.number_input("TARGET 1 [25%]", min_value=0.0, value=0.0, step=0.01, key="tp1", format="%.2f")
    with col2:
        tp2_price = st.number_input("TARGET 2 [25%]", min_value=0.0, value=0.0, step=0.01, key="tp2", format="%.2f")
    with col3:
        tp3_price = st.number_input("TARGET 3 [25%]", min_value=0.0, value=0.0, step=0.01, key="tp3", format="%.2f")
    with col4:
        tp4_price = st.number_input("TARGET 4 [25%]", min_value=0.0, value=0.0, step=0.01, key="tp4", format="%.2f")

# Calculate Button
if st.button("EXECUTE CALCULATION", type="primary", use_container_width=True):

    # Build TP list based on count
    tp_prices = [tp1_price, tp2_price]
    if tp_count >= 3:
        tp_prices.append(tp3_price)
    if tp_count == 4:
        tp_prices.append(tp4_price)

    # Check if all fields are filled
    if capital == 0.0 or risk_pct == 0.0 or entry_price == 0.0 or sl_price == 0.0:
        st.error("ERROR: INCOMPLETE DATA")
        st.stop()

    for i, tp in enumerate(tp_prices, 1):
        if tp == 0.0:
            st.error(f"ERROR: TARGET {i} NOT SET")
            st.stop()

    # Erkenne ob Long oder Short (use last TP for direction)
    last_tp = tp_prices[-1]
    if last_tp > entry_price:
        trade_direction = "LONG"
        is_long = True
    elif last_tp < entry_price:
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
        for tp in tp_prices:
            if tp <= entry_price:
                st.error("ERROR: TARGETS MUST EXCEED ENTRY FOR LONG")
                st.stop()
        # Check ascending order
        for i in range(len(tp_prices) - 1):
            if tp_prices[i] >= tp_prices[i + 1]:
                st.error(f"ERROR: TARGETS MUST BE IN ASCENDING ORDER")
                st.stop()
    else:
        for tp in tp_prices:
            if tp >= entry_price:
                st.error("ERROR: TARGETS MUST BE BELOW ENTRY FOR SHORT")
                st.stop()
        # Check descending order
        for i in range(len(tp_prices) - 1):
            if tp_prices[i] <= tp_prices[i + 1]:
                st.error(f"ERROR: TARGETS MUST BE IN DESCENDING ORDER")
                st.stop()
    
    # Calculate percentage splits based on TP count
    if tp_count == 2:
        tp_splits = [0.50, 0.50]
    elif tp_count == 3:
        tp_splits = [0.33, 0.33, 0.34]
    else:  # tp_count == 4
        tp_splits = [0.25, 0.25, 0.25, 0.25]

    # Berechne SL und TP in Prozent
    sl_distance = abs((entry_price - sl_price) / entry_price) * 100

    tp_distances = []
    tp_profit_pcts = []
    risk_rewards = []

    for i, tp_price in enumerate(tp_prices):
        tp_distance = abs((tp_price - entry_price) / entry_price) * 100
        tp_distances.append(tp_distance)

        tp_profit_pct = tp_distance * tp_splits[i]
        tp_profit_pcts.append(tp_profit_pct)

        risk_reward = tp_profit_pct / sl_distance
        risk_rewards.append(risk_reward)
    
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
    profits_at_tps = []

    for i in range(tp_count):
        profit = (position_size * tp_splits[i]) * (tp_distances[i] / 100)
        profits_at_tps.append(profit)

    potential_profit_total = sum(profits_at_tps)
    avg_risk_reward = sum(risk_rewards) / tp_count
    
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

    # Dynamic Target display based on TP count
    cols = st.columns(tp_count)
    for i in range(tp_count):
        with cols[i]:
            split_pct = int(tp_splits[i] * 100)
            st.markdown(f"TARGET {i+1} [{split_pct}%]: `${tp_prices[i]:.2f} ({tp_distances[i]:.2f}%)`")
            st.markdown(f"RR: `1:{risk_rewards[i]:.2f}`")

    st.markdown(f"**AVERAGE RISK/REWARD: `1:{avg_risk_reward:.2f}`**")
    
    st.markdown("---")
    
    # Position Details
    st.markdown("**POSITION CONFIGURATION**")
    st.markdown(f"MARGIN: `${margin:.2f}` | LEVERAGE: `{leverage:.2f}x` | POSITION SIZE: `${position_size:.2f}`")
    
    st.markdown("---")
    
    # P&L
    st.markdown("**PROFIT & LOSS PROJECTION**")

    # Build dynamic profit display
    tp_profit_str = " | ".join([f"TP{i+1}: `${profits_at_tps[i]:.2f}`" for i in range(tp_count)])
    st.markdown(f"MAX LOSS: `${potential_loss:.2f}` | {tp_profit_str}")
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