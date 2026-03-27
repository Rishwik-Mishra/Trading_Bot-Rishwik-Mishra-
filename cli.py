import click
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import *

@click.command()
@click.option("--symbol", required=True)
@click.option("--side", required=True, type=click.Choice(["BUY", "SELL"], case_sensitive=False))
@click.option("--order_type", required=True, type=click.Choice(["MARKET", "LIMIT", "STOP_LIMIT"], case_sensitive=False))
@click.option("--quantity", required=True, type=float)
@click.option("--price", type=float, default=None)
@click.option("--stop_price", type=float, default=None)

def main(symbol, side, order_type, quantity, price, stop_price):
    """Trading Bot CLI with STOP-LIMIT support"""

    try:
        validate_quantity(quantity)
        validate_price(price, order_type)
        validate_stop_price(stop_price, order_type)

        click.echo("\n📌 Order Request Summary")
        click.echo(f"Symbol: {symbol}")
        click.echo(f"Side: {side}")
        click.echo(f"Type: {order_type}")
        click.echo(f"Quantity: {quantity}")
        if price:
            click.echo(f"Price: {price}")
        if stop_price:
            click.echo(f"Stop Price: {stop_price}")

        client = BinanceClient().get_client()

        result = place_order(
            client, symbol, side, order_type, quantity, price, stop_price
        )

        click.echo("\n✅ Order Successful")
        click.echo(f"Order ID: {result['orderId']}")
        click.echo(f"Status: {result['status']}")
        click.echo(f"Executed Qty: {result['executedQty']}")
        click.echo(f"Avg Price: {result['avgPrice']}")

    except Exception as e:
        click.echo("\n❌ Order Failed")
        click.echo(f"Error: {str(e)}")


if __name__ == "__main__":
    main()