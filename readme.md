# Monte Carlo Simulation for European Call Option Pricing

**Overview**
This project uses the Monte Carlo simulation technique to estimate the fair price of a European call option with the help of Geometric Brownian Motion (GBM).
Overall, this project shows how probability, statistics, and random simulation can be combined to solve real-world problems in financial markets, especially in option pricing.

##Workflow
```mermaid
graph TD;
    A[Download historical stock prices using Yahoo Finance] --> B[Calculate daily logarithmic returns]
    B --> C[Compute annualized volatility]
    C --> D[Generate 10,000 random values from a standard normal distribution]
    D --> E[Simulate future stock prices using Geometric Brownian Motion]
    E --> F[Calculate the payoff of a European Call Option]
    F --> G[Average all simulated payoffs]
    G --> H[Discount the average payoff to its present value]
    H --> I[Display the estimated European Call Option Premium]
```

## What are Options?
An option is a financial contract that gives the buyer the right, but not the obligation, to buy or sell an asset at a predetermined price before or on a specified date.
It is a type of derivative.

## Decoding symbols
| Symbol | Meaning |
|---------|----------|
| **S0** | Current stock price |
| **ST** | Simulated future stock price |
| **r** | Risk-free interest rate |
| **sigma** | Annualized volatility |
| **T** | Time to expiry |
| **Z** | Random variable |

##References
- Zerodha Varsity modules
- investopedia
- Yahoo Finance API (yFinance)
