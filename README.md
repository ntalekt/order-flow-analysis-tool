# Order Flow Analysis Tool for E-mini S&P 500 Futures

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Stargazers](https://img.shields.io/github/stars/ntalekt/order-flow-analysis-tool?style=flat)](https://github.com/ntalekt/order-flow-analysis-tool/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ntalekt/order-flow-analysis-tool?style=flat)](https://github.com/ntalekt/order-flow-analysis-tool/commits/master)

## Project Overview

A real-time tool for identifying **support/resistance levels** in E-mini S&P 500 Futures using:

- Market depth analysis
- Volume profile clustering
- Cumulative delta calculations
- Iceberg order detection

## Key Components
1. **Data Sources**: Denali/Sierra Chart integration
2. **Core Analysis**:
   - Volume-at-price clustering
   - Bid/ask absorption detection
   - Hidden order identification
3. **Visualization**:
   - Heatmaps
   - Footprint charts
   - Delta divergence alerts

## Features ✨

- **Dynamic Support/Resistance Detection**  
  Identifies liquidity zones using:
  - High-volume nodes
  - Bid/ask absorption patterns
  - Hidden iceberg orders
- **Cumulative Delta Analysis**  
  Tracks net buying/selling pressure with configurable thresholds
- **Breakout Alert System**  
  Triggers notifications for confirmed breakouts/rejections

### 3. **Visualization**
- Interactive heatmaps of order book liquidity
- Footprint charts with delta-by-price
- Real-time volume profile overlays

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ntalekt/order-flow-analysis-tool.git
cd order-flow-analysis-tool
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create environment file
```bash
cp .env.example .env
```

### 4. Create data directory
```bash
mkdir -p ~/sierra_data
```

### 5. Run tool
```bash
python src/main.py --product ES --timeframe 5m
```

## Configuration ⚙️

**Environment Variables** (`.env`):
```bash
# Denali/Sierra Chart API Credentials
DENALI_API_KEY=your_api_key_here
DENALI_API_SECRET=your_api_secret_here

# CME Globex Market Data Settings
CME_PRODUCT=ES
CME_TIMEFRAME=5m
```

**Chart Data**
Here's how to populate the ~/sierra_data directory with market data for the E-mini S&P 500 Futures (ES):
1. Sierra Chart Configuration (Recommended)
  - Download Sierra Chart
  - Configure data export:
  - Global Settings > Intraday Data Storage
    - 📁 Set "Save directory" to: ~/sierra_data
    - ✅ Enable "Save Chart Data to Disk"
    - 📈 Add ES futures chart (Symbol: ESZ2023 for Dec 2023 contract)

2. Generate Sample Data (If Sierra Not Available)
  - Create a dummy data file:
  ```bash
  echo "timestamp,price,volume
  $(date +%Y%m%d%H%M%S),4501.25,1500" > ~/sierra_data/ES_sample.scid
  ```

## Security Notes 🛡

- Never commit `.env` to version control
- Rotate API keys quarterly
- Use environment-specific files (`.env.prod`, `.env.dev`)

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Support 📞

For issues or questions, please [open an issue](https://github.com/ntalekt/order-flow-analysis-tool/issues)

---

**Disclaimer**: This tool is not officially affiliated with Southwest Airlines. Use responsibly and in accordance with airline policies.
