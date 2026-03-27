import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger

logger = setup_logger()
load_dotenv()

class BinanceClient:
    def __init__(self):
        try:
            self.api_key = os.getenv("BINANCE_API_KEY")
            self.api_secret = os.getenv("BINANCE_API_SECRET")

            if not self.api_key or not self.api_secret:
                raise ValueError("API keys missing. Please set them in .env file")
            
            self.client = Client(
                self.api_key,
                self.api_secret,
                testnet=True
            )

            logger.info("Binance client initialized successfully (TESTNET)")

        except Exception as e:
            logger.error(f"Client initialization failed: {str(e)}")
            raise

    def get_client(self):
        return self.client