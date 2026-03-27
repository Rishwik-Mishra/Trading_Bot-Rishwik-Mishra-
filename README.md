# 🚀 Binance Futures Testnet Trading Bot

A Python CLI-based trading bot for Binance Futures Testnet (USDT-M).

## ✨ Features

- ✅ Place MARKET orders
- ✅ Place LIMIT orders
- 🔥 Place STOP-LIMIT orders (Bonus Feature)
- ✅ Supports BUY and SELL
- ✅ CLI-based input using Click
- ✅ Structured modular code
- ✅ Logging of API requests & responses
- ✅ Error handling and input validation

---

## 📁 Project Structure


trading_bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .env (not committed)


---

## 🛠 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
2. Create Virtual Environment
python -m venv venv
Activate:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
▶️ How to Run
✅ MARKET Order
python -m cli --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
✅ LIMIT Order
python -m cli --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 60000
🔥 STOP-LIMIT Order (Bonus Feature)
python -m cli --symbol BTCUSDT --side BUY --order_type STOP_LIMIT --quantity 0.001 --price 60000 --stop_price 59000
📄 Logging

Logs are stored in:

logs/trading_bot.log

Includes:

Order requests
API responses
Errors and failures
⚠️ Assumptions
User has a Binance Futures Testnet account
API keys are valid and configured correctly
Trading pair exists (e.g., BTCUSDT)
Quantity adheres to Binance limits
📌 Notes
Uses Binance Futures Testnet (no real funds involved)
Ensure .env file is correctly configured before running
STOP-LIMIT order support is implemented as a bonus feature
💡 Future Improvements
Interactive CLI (menu-based interface)
Retry logic for API failures
Web-based UI dashboard