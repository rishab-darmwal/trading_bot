import logging
from bot.validators import validate_order
import random

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        validate_order(symbol, side, order_type, quantity, price)

        # Fake response (simulation)
        response = {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price if price else "market",
            "status": "FILLED"
        }

        logging.info(f"Fake Order placed: {response}")
        return response

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return {"error": str(e)}