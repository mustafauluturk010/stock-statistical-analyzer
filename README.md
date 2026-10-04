# Stock Statistical Analyzer

A financial data analysis project I built while learning Python.

I started the project with a simple price dataset and gradually added moving averages, buy/sell signals, portfolio calculations, risk analysis, and strategy comparisons.

The project is currently at **V1**.

## What Can It Do?

* Calculate mean, median, variance, and standard deviation
* Calculate daily percentage changes
* Analyze volatility
* Calculate Maximum Drawdown
* Calculate MA3, MA5, and MA7 moving averages
* Generate BUY / SELL / HOLD signals
* Calculate signal success rate
* Calculate strategy returns
* Simulate a portfolio starting with 1000 TL
* Compare strategies with Buy & Hold
* Compare risk and return
* Calculate Sharpe Ratio
* Perform Z-Score analysis
* Detect outliers using IQR
* Perform the Shapiro-Wilk test
* Generate charts
* Rank strategies using a custom scoring system

## Technologies

* Python
* Pandas
* Matplotlib
* SciPy

## Project Structure

```text
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

I used a starting capital of 1000 TL to compare four different approaches.

| Strategy   | Final Portfolio |  Return |
| ---------- | --------------: | ------: |
| MA3        |       787.07 TL | -21.29% |
| MA5        |      1140.33 TL | +14.03% |
| MA7        |      1333.33 TL | +33.33% |
| Buy & Hold |      1600.00 TL | +60.00% |

With this dataset, **Buy & Hold** had the highest return.

However, my custom scoring system ranked **MA7** as the best overall strategy.

### Risk Results

| Strategy   | Standard Deviation | Maximum Drawdown | Sharpe Ratio |
| ---------- | -----------------: | ---------------: | -----------: |
| MA3        |              3.62% |          -30.64% |       -0.210 |
| MA5        |              3.30% |          -11.10% |        0.153 |
| MA7        |              2.88% |           -3.08% |        0.360 |
| Buy & Hold |              3.44% |           -3.08% |        0.492 |

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## Project Status

**V1 is complete.**

The dataset used in this version is small and consists of sample data. The main goal of this version was to practice Python, Pandas, statistics, and basic strategy analysis by building a working project from scratch.

I plan to develop the project further and eventually make it work with real market data.

## Note

This project was created for educational purposes and is not financial advice.
