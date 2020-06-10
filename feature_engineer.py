from dataframe import stockData
from sklearn.impute import SimpleImputer
import ta
from scipy.stats import linregress
import numpy as np
from sklearn.preprocessing import StandardScaler


class featureGenerator:
    def __init__(self, ticker):
        # get data frame
        self.df = stockData(ticker).get_stock_price()

    def get_features(self):
        # feature engineering
        df = self.df.astype(float)

        for i in range(len(df) - 1):
            if df.at[i + 1, 'close'] > df.at[i, 'close']:
                df.at[i, 'delta'] = 1
            else:
                df.at[i, 'delta'] = 0

        # technical analysis features
        def add_slope(r):
            for j in range(r - 1, len(df)):
                a = df['high'][j - (r - 1):j + 1]
                b = []
                for k in range(r):
                    b.append(k)
                name = 'slope_%s' % r
                df.at[j, name] = linregress(a, b).slope

        def add_SO(r):
            ind_SO = ta.momentum.StochasticOscillator(high=df['high'], low=df['low'], close=df['close'], n=r)
            name = 'so_%s' % r
            df[name] = ind_SO.stoch()
            return

        def add_WR(r):
            ind_WR = ta.momentum.WilliamsRIndicator(high=df['high'], low=df['low'], close=df['close'], lbp=r)
            name = 'wr_%s' % r
            df[name] = ind_WR.wr()
            return

        def add_ROC(r):
            ind_ROC = ta.momentum.ROCIndicator(close=df['close'], n=r)
            name = 'roc_%s' % r
            df[name] = ind_ROC.roc()
            return

        def add_MACD(r, j):
            ind_MACD = ta.trend.MACD(close=df['close'], n_fast=r, n_slow=j)
            name = 'macd_%s_%s' % (r, j)
            df[name] = ind_MACD.macd()
            return

        def add_CCI(r):
            ind_CCI = ta.trend.cci(high=df['high'], low=df['low'], close=df['close'], n=r)
            name = 'cci_%s' % (r)
            df[name] = ind_CCI
            return

        # process data
        for i in [3, 4, 5, 10, 20, 30]:
            add_slope(i)

        df['wclose'] = (df['close'] * 2 + df['high'] + df['low']) / 4

        for i in [3, 4, 5, 8, 9, 10]:
            add_SO(i)

        for i in [6, 7, 8, 9, 10]:
            add_WR(i)

        for i in [12, 13, 14, 15]:
            add_ROC(i)

        add_MACD(15, 30)
        add_CCI(15)

        # signal processing features
        for i in range(1, len(df)):
            df.at[i, 'hi_avg_2'] = (df.at[i - 1, 'high'] + df.at[i, 'high']) / 2
            df.at[i, 'lo_avg_2'] = (df.at[i - 1, 'low'] + df.at[i, 'low']) / 2
            df.at[i, 'hilo_avg_2'] = (df.at[i, 'hi_avg_2'] + df.at[i, 'lo_avg_2']) / 2
            df.at[i, 'hilo_avg'] = (df.at[i, 'high'] + df.at[i, 'low']) / 2

        df.dropna(inplace=True)

        df['trend'] = df['open'] - df['open'].shift(1)
        df['trend'] = df['trend'].shift(-1)
        df.fillna(0, inplace=True)

        # generate y
        df['trend'][df['trend'] >= 0] = 1
        df['trend'][df['trend'] < 0] = 0
        y = df['trend'].values
        df.drop(df.columns[[-1]], axis=1, inplace=True)

        def impute(dataframe):
            imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
            imp_mean.fit(dataframe)
            return imp_mean.transform(dataframe)

        df = impute(df)

        # scale features
        scaler = StandardScaler()
        scaler.fit(df)
        df = scaler.transform(df)

        return [df, y]
