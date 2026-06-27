import yfinance as yf
import numpy as np
stock = yf.download("RELIANCE.NS" , start = "2014-07-22", end = "2015-07-21")
# print(stock.columns)
close = stock['Close'].iloc[:,0]


daily_returns = np.log(close / close.shift(1))
daily_returns = daily_returns.dropna()
sigma = daily_returns.std() 
sigma =sigma * np.sqrt(252)

simulations = 10000
Z = np.random.normal(0, 1, simulations)

S0 = close.iloc[-1]
K = S0 * 1.05
r = 0.06 
T = 30/365 

ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

payoffs = np.maximum(ST - K, 0)
call_price = np.exp(-r*T) * np.mean(payoffs)
print("For OTM:")
print("current price:",S0)
print("strike price: ",K)
print("expected call_price: ",call_price)


K = S0
r = 0.06 
T = 30/365 

ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

payoffs = np.maximum(ST - K, 0)
call_price = np.exp(-r*T) * np.mean(payoffs)
print("For ATM:")
print("current price:",S0)
print("strike price: ",K)
print("expected call_price: ",call_price)


K = S0 * 0.95
r = 0.06 
T = 30/365 

ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

payoffs = np.maximum(ST - K, 0)
call_price = np.exp(-r*T) * np.mean(payoffs)
print("For ITM:")
print("current price:",S0)
print("strike price: ",K)
print("expected call_price: ",call_price)