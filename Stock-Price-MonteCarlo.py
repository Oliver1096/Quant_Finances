import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#numero de simulaciones del día
NUM_OF_SIMULATIONS = 10000


def stock_monte_carlo(S0, mu, sigma, N=252):
#252 debido a que son 252 días operativos al año
    result = []

    # number of simulations - possible S(t) realizations (of the process)
    for _ in range(NUM_OF_SIMULATIONS):
        prices = [S0]
        for _ in range(N):
            # we simulate the change day by day (t=1)
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma ** 2) +
                                              sigma * np.random.normal())
            prices.append(stock_price)

        result.append(prices)

    simulation_data = pd.DataFrame(result)
    # the given columns will contain the time series for a given simulation
    simulation_data = simulation_data.T
    print(simulation_data)
    plt.plot(simulation_data)
    plt.show()

    #Agregamos la media de cada una de la ssimulaciones
    simulation_data['mean'] = simulation_data.mean(axis=1)


    plt.plot(simulation_data['mean'])
    plt.show() #graficamos la media de las simulaciones

    print('Prediction for future stock price: $%.2f' % simulation_data['mean'].tail(1))


if __name__ == '__main__':
    stock_monte_carlo(50, 0.0002, 0.01)
