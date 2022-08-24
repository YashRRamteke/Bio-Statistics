import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt


stocks = ['GOOG','AMZN']
data = pdr.get_data_yahoo(stocks,start = '2019-01-01')['Close']
data.head()

## from matplotlib import rcParams
rcParams['figure.figsize'] = 14,8
plt.plot(data.AMZN)
plt.plot(data.GOOG)
plt.grid(True, color='k', linestyle=':')
plt.title('Amazon and Google prices')
plt.xlabel("Date")
plt.ylabel("Prices")
plt.ylim(25,200)
plt.yticks([50,100,150,200])
plt.style.use('fivethirtyeight')
plt.show()
