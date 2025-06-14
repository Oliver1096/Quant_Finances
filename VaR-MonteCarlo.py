import numpy as np
import yfinance as yf
import datetime
import pandas as pd


def download_data(stock, start, end):
    ticker = yf.download(stock, start=start, end=end, auto_adjust=True)
    df = ticker[['Close']].rename(columns={'Close': 'Adj Close'})  # Renombramos para mantener compatibilidad
    return df


class ValueAtRiskMonteCarlo:

    def __init__(self, S, mu, sigma, c, n, iterations):
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n
        self.iterations = iterations

    def simulation(self):
        rand = np.random.normal(0, 1, self.iterations)
        stock_price = self.S * np.exp(self.n * (self.mu - 0.5 * self.sigma ** 2) + self.sigma * np.sqrt(self.n) * rand)
        percentile = np.percentile(stock_price, (1 - self.c) * 100)
        return self.S - percentile


if __name__ == "__main__":
    S = 1e6  # Inversión
    c = 0.99  # Nivel de confianza
    n = 1  # Horizonte (1 día)
    iterations = 100000

    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime(2017, 10, 15)

    citi = download_data('C', start_date, end_date)

    citi['returns'] = citi['Adj Close'].pct_change()
    citi.dropna(inplace=True)

    mu = citi['returns'].mean()
    sigma = citi['returns'].std()

    model = ValueAtRiskMonteCarlo(S, mu, sigma, c, n, iterations)
    print('Value at Risk with Monte Carlo simulation: $%0.2f' % model.simulation())
