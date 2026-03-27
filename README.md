# 🚀 Binance Futures Testnet Trading Bot

A robust, Python-based Command Line Interface (CLI) trading bot designed for the Binance Futures Testnet (USDT-M).

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

```text
trading_bot/
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── cli.py
├── requirements.txt
├── README.md
└── .env               # (Not committed to version control)
```

---

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
```
**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory of your project and add your Testnet credentials:
```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
BASE_URL=[https://testnet.binancefuture.com](https://testnet.binancefuture.com)
```

---

## ▶️ How to Run

Use the CLI to execute different types of orders. Below are examples of how to format your commands:

**✅ MARKET Order**
```bash
python -m cli --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001
```

**✅ LIMIT Order**
```bash
python -m cli --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 60000
```

**🔥 STOP-LIMIT Order** *(Bonus Feature)*
```bash
python -m cli --symbol BTCUSDT --side BUY --order_type STOP_LIMIT --quantity 0.001 --price 60000 --stop_price 59000
```

---

## 📄 Logging

All bot activity is recorded for debugging and audit purposes.

- **Location:** Logs are stored locally in `logs/trading_bot.log`.
- **Included Data:** Order execution requests, Binance API responses, and detailed error/failure tracking.

---

## ⚠️ Assumptions & Notes

> **Note:** This bot connects exclusively to the **Binance Futures Testnet**. No real funds are involved or at risk. 

- **Prerequisites:** You must have an active Binance Futures Testnet account.
- **Configuration:** API keys must be valid, properly permissioned, and correctly set in the `.env` file before running the bot.
- **Market Constraints:** The trading pair must exist on the Testnet (e.g., `BTCUSDT`), and the requested quantity must adhere to Binance's lot size and minimum notional limits.

---

## 💡 Future Improvements

- Interactive CLI (menu-based interface)
- Retry logic for API failures
- Web-based UI dashboard
