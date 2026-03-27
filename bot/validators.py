def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    if order_type.upper() in ["LIMIT", "STOP_LIMIT"]:
        if price is None or price <= 0:
            raise ValueError("Price must be provided and greater than 0")


def validate_stop_price(stop_price, order_type):
    if order_type.upper() == "STOP_LIMIT":
        if stop_price is None or stop_price <= 0:
            raise ValueError("Stop price required for STOP_LIMIT orders")