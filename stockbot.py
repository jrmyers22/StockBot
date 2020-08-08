import yfinance as yf

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-1-25')

#see your data
for key in tickerData.info.keys():
	print(key)