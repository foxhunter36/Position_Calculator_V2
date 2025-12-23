# Position Calculator - Neo/Matrix Style

Eine Streamlit-basierte Trading Position Size Calculator App im Neo/Matrix Design.

## Features

- **Position Size Berechnung** basierend auf Account Size und Risk Percentage
- **Multi-Target System** mit 3 Take-Profit Levels (33/33/34 Split)
- **Long & Short Trading** automatische Erkennung
- **Risk/Reward Ratio** für jeden Target Level
- **Leverage Calculation** automatische Margin- und Leverage-Berechnung
- **Matrix-Style UI** grünes Terminal-Design

## Installation (Lokal)

```bash
pip install -r requirements.txt
streamlit run position_calculator_streamlit.py
```

## Deployment

Diese App ist optimiert für Streamlit Community Cloud Deployment.

## Usage

1. Account Size eingeben
2. Risk Percentage festlegen (z.B. 1%)
3. Entry Price, Stop Loss und 3 Targets eingeben
4. "EXECUTE CALCULATION" klicken
5. Trade Analysis anzeigen lassen

## Trade Validation

Die App validiert automatisch:
- ✓ Long/Short Detection
- ✓ Stop Loss Position
- ✓ Target Order (TP1 < TP2 < TP3)
- ✓ Risk/Reward Ratio (empfohlen: mindestens 1:2)
- ✓ Leverage Warnings (>10x)

## Trade Recommendation

- **APPROVED**: Risk/Reward ≥ 1:2
- **REJECTED**: Risk/Reward < 1:2

---

Made with ☕ by Andre
