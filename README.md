# Quantitative Finances applied to market risks and derivative products

## Derivative products 
* Swaps
* Forwards
* Options

We use different models to pricing derivative pruducts.

Quantitative analysis assumes a random behavior of assets so it is assumed that financial quantities such as stock prices, interest rates, the value of options have a random behavior.



## Brownian Motion 

In 1827 the Scottish botanist **Robert Brown** observed the random behavior of pollen particles suspended in water. This phenomenon cme to be known as *Brownian motion* .
Louis Bachelier in his doctoral work on option pricing in 1900 made numerous advances of this mathematical properties.


## The Wiener process

## Itô's lemma

**Stochastic calculus** is an important field of mathematics that works with stochastic processes. Much like ordinary calculus, stochastic calculus is based on several fundamental results. One of the most important stochastic calculus results used in options is **Itô's lemma**. Though this result was discovered about 1950, it did not get firmly establiseh in the finance literature until 1973 when Black, Scholes and Merton discovered that it could be used to model the price of a stock and ultimatwly to facilitate pricing an option.

In ordinary calculus, the variables are non-stochastic, wich simply means that when we talk about a particular value of $x$, that value is known for certain. When $x$ is stochastic, we leave the world of ordinary calculus and enter the world of stochastic calculus. There we cannot talk about a set of possible values of $x$ that are generated according to a probability distribution. In stochastic calculus, results are proven by demostrating what happends when squared values of a variable are multiplied by probabilities.

In simple words when a random variable follows a **Brownian-type process**, you cannot apply the traditional rules of differentiation. Itô’s Lemma corrects this by adding a second-order term that accounts for the variance of the stochastic process.

The generalized form of Itô process is expressed as:

<p align="center"> $dx = \mu (x,t)dt + \sigma(x,t)dW_t$</p>

where $F=F(x,t)$ , subject to certain technical constraints,

<p align="center"> $dF = \frac{\partial F}{\partial x}[\mu(x,t)dt + \sigma(x,t)dW] + \frac{\partial F}{\partial t} + \frac{1}{2} \frac{\partial^2 F}{\partial x^2} \sigma(x,t)^2 dt$</p>

This result is known as Ito's lemma, being named for the japanese mathematician Kiyoshi Itô, who discovered this result.

The equation describes the stochastic process of a function $F(x,t)$ that is driven by time $t$ and a stochastic process for $x$ of the form we previously referred to as a Winner process.

Itô's lemma is widely used in pricing derivatives. The price of a derivative is said to be 'derived' from the price of the underlying asset and time. Thus, $F(x,t)$ is a convenient specification of a derivative price, because its value is derived from $x$ and $t$ , with $x$ known to be stochastic and $t$ representing time. 


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
$C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)$


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


## Sources

* Robert E. Brooks & Don M. Chance. *Foundations of the Pricing of Financial Derivatives*
* John Hull. *Options, Futures and Other Derivatives*
