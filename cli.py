from bot.orders import place_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    print("=== Binance Futures Trading Bot ===")

    symbol = input("Enter Symbol (e.g., BTCUSDT): ")
    side = input("Enter Side (BUY/SELL): ")
    order_type = input("Enter Type (MARKET/LIMIT): ")
    quantity = float(input("Enter Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter Price: "))

    result = place_order(symbol, side, order_type, quantity, price)

    print("\n===== RESULT =====")
    print(result)

if __name__ == "__main__":
    main()