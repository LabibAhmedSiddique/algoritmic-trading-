class StockTrader:
    def __init__(self, symbol, from_date, to_date,initial_budget=5000):
        self.symbol = symbol
        self.from_date = from_date
        self.to_date = to_date
        self.initial_budget = initial_budget
        self.has_position = False  # Flag to track open position

    def get_data(self):
        import yfinance as yf
        self.data = yf.download(self.symbol, start=self.from_date, end=self.to_date)

    def clean_data(self):
        self.data.drop_duplicates(inplace=True)  
        self.data.ffill(inplace=True)  

    def calculate_moving_avg(self):
        self.data['MA50'] = self.data['Close'].rolling(window=50).mean()
        self.data['MA200'] = self.data['Close'].rolling(window=200).mean()

    def identify_golden_cross(self):
        self.golden_cross = self.data[ (self.data['MA50'] > self.data['MA200']) & (self.data['MA50'].shift(1) <= self.data['MA200'].shift(1)) ]
        if self.golden_cross.empty:
          print("No golden cross found for the given period.")

    def get_buy_quantity(self):        
        self.buy_quantity = int(self.initial_budget / self.golden_cross.iloc[0]['Close'])

    def buy(self):
        if not self.has_position:
            self.get_buy_quantity()
            self.buy_date = self.golden_cross.index[0]
            self.has_position = True
            print(f"Bought {self.buy_quantity} shares on {self.buy_date}")

    def identify_golden_cross_reversal(self):
       
        self.golden_death_cross = self.data.loc[(self.data['MA50'] < self.data['MA200']) & (self.data['MA50'].shift(1) >= self.data['MA200'].shift(1))]
        

    def sell(self):
        if self.has_position:
            if self.golden_death_cross is not None:
                # Sell on reversal signal
                self.sell_date = self.golden_death_cross.index[0]
            else:
                # No reversal signal, sell on last day
                self.sell_date = self.data.index[-1]
            self.has_position = False
            print(f"Sold {self.buy_quantity} shares on {self.sell_date}")

    def evaluate(self):
        if self.has_position:
            print("WARNING: Position still open, cannot calculate final profit/loss accurately.")
            return
        buy_price = self.data.loc[self.buy_date]['Close']
        sell_price = self.data.loc[self.sell_date]['Close']
        profit = (sell_price - buy_price) * self.buy_quantity
        if profit<0:
          print(f"Loss: ${profit:.2f}")
        else :
          print(f"profit: ${profit:.2f}")  


if __name__ == "__main__":
  trader = StockTrader("AAPL", "2018-01-01", "2023-12-31")
  trader.get_data()
  print()
  trader.clean_data()
  trader.calculate_moving_avg()
  trader.identify_golden_cross()
  trader.buy()  # Assuming a golden cross is identified
  trader.identify_golden_cross_reversal()  # Check for reversal after buy
  trader.sell()  # Sell based on reversal or last day
  trader.evaluate()
