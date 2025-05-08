import pandas as pd
import numpy as np
import yfinance as yf
import cvxpy as cp

def optimize_portfolio(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    returns = data.pct_change().dropna()

    n = len(tickers)
    weights = cp.Variable(n)
    ret = returns.mean().values @ weights
    risk = cp.quad_form(weights, returns.cov().values)
    prob = cp.Problem(cp.Maximize(ret / cp.sqrt(risk)), [cp.sum(weights) == 1, weights >= 0])
    prob.solve()

    return dict(zip(tickers, weights.value))
