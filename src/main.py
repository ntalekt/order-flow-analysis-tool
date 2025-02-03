import argparse
from data_sources import DenaliDataFeed
from order_flow import OrderFlowAnalyzer
from visualization import Dashboard


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--product", type=str, default="ES")
    parser.add_argument("--timeframe", type=str, default="5m")
    args = parser.parse_args()

    feed = DenaliDataFeed()
    analyzer = OrderFlowAnalyzer()
    Dashboard(feed, analyzer).run()


if __name__ == "__main__":
    main()
