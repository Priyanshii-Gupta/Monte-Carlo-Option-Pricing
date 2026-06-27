# Monte Carlo Simulation for European Call Option Pricing

**Overview**
This project uses the Monte Carlo simulation technique to estimate the fair price of a European call option with the help of Geometric Brownian Motion (GBM).
Overall, this project shows how probability, statistics, and random simulation can be combined to solve real-world problems in financial markets, especially in option pricing.

**Workflow**
```mermaid
graph TD;
Download historical stock prices using Yahoo Finance-->Calculate daily logarithmic returns;
Calculate daily logarithmic returns-->Compute annualized volatility;
Compute annualized volatility-->Generate 10,000 random values from a standard normal distribution;
Generate 10,000 random values from a standard normal distribution-->Simulate future stock prices using Geometric Brownian Motion;
Simulate future stock prices using Geometric Brownian Motion --> Calculate the payoff of a European Call Option
Calculate the payoff of a European Call Option --> Average all simulated payoffs
Average all simulated payoffs --> Discount the average payoff to its present value
Discount the average payoff to its present value --> Display the estimated European Call Option Premium
```

