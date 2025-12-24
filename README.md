# Position Calculator - Neo/Matrix Style

Eine Streamlit-basierte Trading Position Size Calculator App im Neo/Matrix Design.

## Features

### Core Functionality
- **Position Size Berechnung** basierend auf Account Size und Risk Percentage
- **Flexible Multi-Target System** - wähle zwischen 1, 2, 3 oder 4 Take-Profit Levels
- **Long & Short Trading** - automatische Erkennung der Trade-Richtung
- **Risk/Reward Ratio** - individuelle RR-Berechnung für jeden Target Level
- **Leverage Calculation** - automatische Margin- und Leverage-Berechnung
- **Trade Validation** - umfassende Checks für sichere Trade-Setups

### UI/UX Features
- **Matrix-Style Terminal Design** - authentisches grünes Terminal-Theme
- **Button-Based TP Selection** - intuitive 1/2/3/4 Buttons statt Dropdown
- **Dynamic Input Fields** - Target-Inputs passen sich automatisch an
- **Matrix Green Styling** - alle Plus/Minus Buttons im Neo-Style
- **Custom Messages** - "You heard the monkey - make the trade" 🐒
- **Hover Effects** - weiße Text-Anzeige beim Execute Button Hover
- **Responsive Layout** - optimiert für Desktop und Mobile

## Installation (Lokal)

```bash
# Repository klonen
git clone https://github.com/foxhunter36/Position_Calculator_V2.git
cd Position_Calculator_V2

# Dependencies installieren
pip install -r requirements.txt

# App starten
streamlit run position_calculator_streamlit.py
```

## Deployment

Diese App ist optimiert für Streamlit Community Cloud Deployment.

**Live Version:** [https://position-calc-matrix.streamlit.app/](https://position-calc-matrix.streamlit.app/)

## Usage

### Basis-Workflow

1. **System Input**
   - Account Size eingeben (z.B. $10,000)
   - Risk Percentage festlegen (empfohlen: 1-2%)

2. **TP Level Selection**
   - Wähle zwischen 1, 2, 3 oder 4 Take-Profit Levels
   - Split wird automatisch berechnet:
     - 1 Level: 100%
     - 2 Levels: 50/50
     - 3 Levels: 33/33/34
     - 4 Levels: 25/25/25/25

3. **Trade Setup**
   - Entry Price eingeben
   - Stop Loss setzen
   - Target Levels definieren

4. **Execution**
   - "EXECUTE CALCULATION" klicken
   - Trade Analysis prüfen
   - Bei positiver RR: "You heard the monkey - make the trade" 🐒

## Trade Validation

Die App validiert automatisch:

- ✅ **Long/Short Detection** - basierend auf Target-Position
- ✅ **Stop Loss Position** - muss auf richtiger Seite sein
- ✅ **Target Order** - Long: aufsteigend | Short: absteigend
- ✅ **Risk/Reward Ratio** - individuell pro TP und durchschnittlich
- ✅ **Leverage Warnings** - bei >1x und >10x
- ✅ **Incomplete Data** - alle Felder müssen ausgefüllt sein

## Trade Recommendation

### ✅ APPROVED
- Risk/Reward ≥ 1:2
- Message: *"You heard the monkey - make the trade"*

### ❌ REJECTED
- Risk/Reward < 1:2
- Message: *"TRADE REJECTED - INSUFFICIENT RISK/REWARD [1:X.XX]"*

## Output Information

### Trade Analysis
- **Direction**: LONG oder SHORT
- **Entry & Stop Loss**: mit Prozent-Distanz
- **Target Levels**: Preise, Prozente, Risk/Reward pro Level
- **Average Risk/Reward**: Gesamtdurchschnitt

### Position Configuration
- **Margin**: benötigtes Kapital
- **Leverage**: verwendeter Hebel
- **Position Size**: totale Positionsgröße

### Profit & Loss Projection
- **Max Loss**: bei Stop Loss
- **TP Profits**: Gewinn pro Target
- **Total Profit**: wenn alle Targets erreicht

### Warnings
- Suboptimal RR Ratio (< 1:2)
- Excessive Leverage (> 10x)
- Leverage Active Info

## Tech Stack

- **Streamlit** - Web Framework
- **Python 3.x** - Backend
- **CSS** - Custom Matrix-Style Theming
- **JavaScript** - Enhanced UI Features

## Design Philosophy

Die App folgt dem Neo/Matrix Terminal Aesthetic:
- Schwarzer Hintergrund
- Matrix Green (#00ff41) als Primärfarbe
- Courier New Monospace Font
- Terminal-Style Outputs
- Minimalistisches, fokussiertes Layout

## Best Practices

### Empfohlene Settings
- **Risk**: 1-2% pro Trade (max 5%)
- **Risk/Reward**: Mindestens 1:2
- **Leverage**: Unter 10x (optimal: 1-3x)

### Trade Selection Criteria
1. Klare Support/Resistance für Targets
2. Definierter Stop Loss unter/über Key-Level
3. Minimum 1:2 Risk/Reward
4. Angemessene Position Size für Account

## Project Structure

```
Position_Calculator_V2/
├── position_calculator_streamlit.py    # Main App
├── requirements.txt                     # Dependencies
├── README.md                            # Documentation
├── .gitignore                          # Git ignore rules
└── archive/                            # Old versions & cheat sheets
    ├── TERMINAL_CHEAT_SHEET.txt
    └── GIT_CHEAT_SHEET.md
```

## Updates & Changelog

### Version 2.0 (Latest)
- ✨ Button-based TP Level Selection (1/2/3/4)
- ✨ Dynamic Input Fields basierend auf Selection
- ✨ Matrix Green Plus/Minus Buttons
- ✨ Custom Success/Fail Messages
- ✨ Enhanced Hover Effects
- 🐛 Fixed: TP Level validation
- 🎨 Improved: Matrix-Style consistency

### Version 1.0
- Initial Release
- 3 TP Levels (33/33/34 Split)
- Basic Matrix Styling
- Long/Short Support

## Contributing

Contributions are welcome! Dieses Projekt dient primär als Learning-Tool und Portfolio-Piece.

## License

Personal Project - Feel free to fork and modify for your own use.

---

**Built with 💚 by Andre**  
*Data-driven Marketing. Algorithm-driven Trading. Creativity-driven Photography.*

[GitHub](https://github.com/foxhunter36) | [Live App](https://position-calc-matrix.streamlit.app/)
