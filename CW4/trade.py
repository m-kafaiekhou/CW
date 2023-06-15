# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import talib
import sys

# Create Trading Strategy Class
class ForexStrategy:
    def __init__(self):
        # Parameters
        self.interval_length = 15 #minutes
        self.risk_tolerance = 100 #percent risk for each trade
        self.pair = 'USD/EUR'

    # Function to generate signals
    def signal_generator(self):
        # Load data
        global df
        df = pd.read_csv('EURUSD.csv')
        df.columns = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        # Calculate MACD
        df['macd_hist'] = talib.MACD(df['Close'])[2]
        df['macd_signal'] = talib.MACD(df['Close'])[1]
        # Create a flag column for buy and sell signals
        df['sell'] = np.where(df['macd_hist'] > 0, 1, 0)
        df['buy'] = np.where(df['macd_hist'] <= 0, -1, 0)
        # Combine the flag columns
        df['signal'] = (df['sell'] + df['buy'])
        return df

    # Function to generate trades
    def trade_generator(self):
        # Calculate lot size based on risk tolerance
        lot_size = (self.risk_tolerance / 100.0) * df['Close']
        # Generate buy and sell trades
        df['buy_trades'] = np.where(df['signal'] == -1, lot_size, 0)
        df['sell_trades'] = np.where(df['signal'] == 1, lot_size, 0)
        return df
        # Function to backtest strategy

    def backtest_strategy(self):
    # Calculate profit and loss
        df['profit_loss'] = df['buy_trades'] - df['sell_trades']
        df['pnl'] = df['profit_loss'].cumsum()
        # Calculate risk reward ratio
        drawdown = df['pnl'].cummax() - df['pnl']
        ddpercent = drawdown / df['pnl'].cummax() * 100.0
        df['ddpercent'] = ddpercent
        return df
# Initialize Trading Strategy
strategy = ForexStrategy()
# Generate signals
signals = strategy.signal_generator()
# Generate trades
trades = strategy.trade_generator()
# Backtest strategy
results = strategy.backtest_strategy()
# Print results
print(results)