# Stock Statistical Analyzer

A financial data analysis project I developed while learning Python.

I started the project with basic price data. Over time, I added features such as moving averages, BUY/SELL signals, portfolio calculation, risk analysis, and strategy comparison.

The project is currently in the V1 stage.

## Features

* Mean, median, variance, and standard deviation calculation

* Daily percentage change calculation

* Volatility analysis

* Maximum Drawdown calculation

* MA3, MA5, and MA7 moving averages

* BUY / SELL / HOLD signals

* Signal success rate

* Calculation of strategy returns

* Portfolio simulation starting with 1000 TL

* Comparison with the Buy-and-Hold strategy

* Risk and return comparison

* Sharpe Ratio

* Z-Score analysis

* Outlier analysis

* Shapiro-Wilk test

* Visualizations / Charts

* Strategy scoring system

## Built With

* Python

* Pandas

* Matplotlib

* SciPy

## Project Structure

```
stock-statistical-analyzer/
│
├── data/
│   └── stock_data.csv
│
├── main.py
├── requirements.txt
└── README.md

```

## V1 Results

In the project, I compared four different approaches using a starting capital of 1000 TL.

| Strategy | Final Portfolio | Return | 
| ----- | ----- | ----- | 
| MA3 | 787.07 TL | \-21.29% | 
| MA5 | 1140.33 TL | +14.03% | 
| MA7 | 1333.33 TL | +33.33% | 
| Buy-Hold | 1600.00 TL | +60.00% | 

In this dataset, the Buy-and-Hold strategy yielded the highest return.

In the custom scoring system I created, **MA7** ranked first.

### Risk Results

| Strategy | Standard Deviation | Maximum Drawdown | Sharpe | 
| ----- | ----- | ----- | ----- | 
| MA3 | 3.62% | \-30.64% | \-0.210 | 
| MA5 | 3.30% | \-11.10% | 0.153 | 
| MA7 | 2.88% | \-3.08% | 0.360 | 
| Buy-Hold | 3.44% | \-3.08% | 0.492 | 

## How to Run

First, install the required libraries:

```
pip install -r requirements.txt

```

Then run:

```
python main.py

```

If `python` does not work on Windows:

```
py main.py

```

## Project Status

**V1 is complete.**

The dataset used in this version is small and consists of sample data. My primary goal was to build a working analysis system using Python, Pandas, and basic statistical concepts.

I plan to further develop the project in the future to work with real market data.

## Disclaimer

This project was developed for educational purposes and does not constitute financial advice.
