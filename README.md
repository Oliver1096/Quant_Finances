# Quantitative Finances applied to market risks and derivative products

## Derivative products 
* Swaps
* Forwards
* Options

We use different models to pricing and trading.

Quantitative analysis assumes a random behavior of assets so it is assumed that financial quantities such as stock prices, interest rates, the value of options have a random behavior.


## Itô's lemma

**Stochastic calculus** is an important field of mathematics that works with stochastic processes. Much like ordinary calculus, stochastic calculus is based on several fundamental results. One of the most important stochastic calculus results used in options is **Itô's lemma**. Though this result was discovered about 1950, it did not get firmly establiseh in the finance literature until 1973 when Black, Scholes and Merton discovered that it could be used to model the price of a stock and ultimatwly to facilitate pricing an option.

In simple words when a random variable follows a **Brownian-type process**, you cannot apply the traditional rules of differentiation. Itô’s Lemma corrects this by adding a second-order term that accounts for the variance of the stochastic process.


## Black - Scholes model.

Propuesto en 1973 por Fischer Black y Myron Scholes para la valoración de opciones europeas sobre una acción que no paga dividendos y cuyo precio es descrito por un movimiento Browniano geométrico.

Analíticamente, el modelo B-S es una **ecuación diferencial parcial**.

**Supuestos**

* Volatilidades constantes asociadas al comportamiento del precio del activo subyacente.
* Ausencia de costos de transacción.
* Mercados perfectamente liquidos.
* Tasas de interés iguales para inversión o prestamo.
* Ausencia de riesgo contraparte.
* El activo subyacente no paga dividendos.
* El precio S del activo subyacente es descrito mediante un movimiento geométrico Browniano.
* No existen oportunidades de arbitraje.
* 



## Value at Risk (VaR)

**VaR is a number measure in price unit.**

It tells you that in a large percentage of cases your portfolio is likely to not lose more than that amount of money.

**VaR** measures the amount of potential loss that could happen in an investment ( or a portfolio of investments) over a given period of time (with a given degree of confidence).


**VaR** is easy to understand and easy to interpret.

Standard deviation or beta is not that straightforward.


You can compare different types of assets or portfolios with **VaR**.

You can compare profitability and risk of different units and make a decision accordingly. 


Basically, there are two ways to handle value at Risk, with the **variance method** and with the **Monte Carlo Simulation**

#### Variance Method

This method assumes returns are normally distributed


