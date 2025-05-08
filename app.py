from src.trade_simulator import simulate_trade
from src.portfolio import get_portfolio_value
from src.optimizer import optimize_portfolio

if __name__ == "__main__":
    # Simulate trade
    price = simulate_trade("AAPL", "BUY", 10, "2023-06-01")
    print(f"Bought AAPL at ${price:.2f}")

    # Show portfolio value
    value = get_portfolio_value()
    print(f"Current Portfolio Value: ${value:.2f}")

    # Optimize allocation
    weights = optimize_portfolio(["AAPL", "GOOGL", "MSFT"], "2023-01-01", "2023-12-31")
    print("Optimized Portfolio Allocation:")
    for ticker, weight in weights.items():
        print(f"{ticker}: {weight:.2%}")
