# Quantitative Finances applied to market risks and derivative products

The most common definition of a derivative reads approximately as follows:

<p align="center"><em>A derivative is a finantial instrument that derives its performance from the performance of an underlying asset</em></p>


This definition despite being so widely quoted, can nonetheless be a bit troublesome. 


For example, it can also describe mutual funds and Exchange-Traded Funds, wich would never be viewed as derivatives even though they derive their values from the values of the underlying securities they hold. Perhaps the distinction that best characterizes derivatives is that they ussualy transform the performance of the underlying asset before paying it out in the derivatives transaction. In contrast, with the exception of expense deductions, mutual funds and ETF simply pass through the returns of their underlying securities.

<p align="right">&#8209; CFA Institute.</p>



## Summary

Quantitative analysis assumes a random behavior of assets so it is assumed that financial quantities such as stock prices, interest rates, the value of options have a random behavior. Thus, the financial landscape will be everchanging. Indeed, it is important to understand the probability process driving prices, because this helps to develop good valuation models. Estimates of expected returns and volatilities and their effects on assets and derivative prices are assential elements in the financial decision making process.



## Brownian Motion 

In 1827 the Scottish botanist **Robert Brown** observed the random behavior of pollen particles suspended in water. This phenomenon came to be known as *Brownian motion* .
Louis Bachelier in his doctoral work on option pricing in 1900 made numerous advances of this mathematical properties.


## The Wiener process

The increment to the standard Brownian Motion is called a *Winener process* , named for the American mathematician, Norbert Wiener

One interesting property of the Wiener process is that when you square it, it becomes perfectly predictable.

Some characteristics of the Wiener process are below:

<p align="center"> $E(dW_t) = E( \epsilon_t \sqrt{dt}) = \sqrt{dt} E(\epsilon_t) = 0 $</p>

And taking into account the variance:

<p align="center"> $var(dW_t) = E(\epsilon_t \sqrt{dt})^2 - [E(\epsilon_t \sqrt{dt} )]^2 = dtE(\epsilon_t^2 ) - 0 = dt$</p>

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


## Black - Scholes - Merton model.

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
  
<p align="center">$C = S \cdot N(d_1) - X \cdot e^{-rT} \cdot N(d_2)$</p>

where: 

<p align="center">$d_1 = \frac{ln(S/X) + (r_c + \sigma^2/2) \cdot T}{\sigma \sqrt{T}}$</p>

and

<p align="center">$d_2 = \frac{ln(S/X) + (r_c - \sigma^2/2) \cdot T}{\sigma \sqrt{T}} = d1 - \sigma \sqrt{T}$</p>


The option price is assumed to be a function of only two variables: the asset price and time. 

The model of stock price behavior used by Black, Scholes and Merton is the Winner proces and the Itô's lemma. It assumes that the percentage changes in the stock price in a very show period of time are normally distribuited. 


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
* Andrew Rennie & Martin Baxter. *Financial Calculus: An Introduction to Derivative Pricing*
* CFA 2023 program.
