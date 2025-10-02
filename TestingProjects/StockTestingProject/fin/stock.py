class Stock:
    def __init__(self, symbol, exchange):
        self._symbol = symbol
        self._exchange = exchange
        self._trades = []

    def buy(self, quantity):
        current_price = self._exchange.get_price(self._symbol)
        self._trades.append({'quantity':quantity, 'price': current_price, 'side':'BUY'})

    def sell(self, quantity):
        current_price = self._exchange.get_price(self._symbol)
        self._trades.append({'quantity':quantity, 'price': current_price, 'side':'SELL'})

    def total_number_of_trades(self):
        return len(self._trades)

    def get_total_quantity_bought(self):
        quantity = 0
        for trade in self._trades:
            if trade['side'] == 'BUY':
                quantity += trade['quantity']
        return quantity

    def get_total_quantity_sold(self):
        quantity = 0
        for trade in self._trades:
            if trade['side'] == 'SELL':
                quantity += trade['quantity']
        return quantity

    def get_total_value_bought(self):
        value = 0
        for trade in self._trades:
            if trade['side'] == 'BUY':
                value += trade['price'] * trade['quantity']
        return value

    def get_total_value_sold(self):
        return 0.0

    def get_biggest_quantity_buy(self):
        quantity = 0
        for trade in self._trades:
            if trade['side'] == 'BUY':
                if trade['quantity'] > quantity:
                    quantity = trade['quantity']
        return quantity

    def get_biggest_value(self):
        pass

    # Your tasks:
    #
    # Implement the get_total_quantity_bought() and get_total_quantity_sold()
    # methods using TDD with Python's unittest framework.
    #
    # Implement the get_total_value_bought() and get_total_value_sold()
    # methods using TDD with Python's unittest.mock framework. You will need
    # to mock the exchange so that it returns realistic prices, rather than 0.
    # Don't change any code in Exchange class, or create you own - use Mock!
    # You can also try the other methods if you have time.

