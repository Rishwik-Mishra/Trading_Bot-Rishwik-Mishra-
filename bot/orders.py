from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        logger.info(f"Placing order: {symbol} | {side} | {order_type} | {quantity} | {price} | {stop_price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Raw API response: {response}")

        if not response or "orderId" not in response:
            raise Exception(f"Invalid API response: {response}")

        return {
            "orderId": response["orderId"],
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }

    except Exception as e:
        logger.error(f"Order placement failed: {str(e)}")
        raise