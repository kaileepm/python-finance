import numpy as np
import pandas as pd
import pandas.io.data as web

goog = web.DataReader('GOOG', data_source='google', start='3/14/2009', end='4/14/2016')
goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)
