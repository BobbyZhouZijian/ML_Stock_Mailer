import numpy as np
import ta
from scipy.stats import linregress
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
# import libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
# set up training tools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from dataframe import stockData


class classifier:

    def __init__(self, ticker):
        self.df = stockData(ticker).get_stock_price()

    def get_report_message(self):
        # get data frame
        df = self.df

        # feature engineering
        df = df.astype(float)

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

        # train test split
        X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, shuffle=False)

        # logistic regression
        clf0 = LogisticRegression()
        clf0.fit(X_train, y_train)
        scores = cross_val_score(clf0, X_train, y_train, cv=10)
        logistic_mean = scores.mean()
        logistic_std = scores.std()
        logistic_prediction = clf0.fit(X_train, y_train).predict(X_test[-1].reshape(-1, 34))[0]

        # support vector machine
        clf1 = svm.SVC(kernel='linear', C=1)
        scores = cross_val_score(clf1, X_train, y_train, cv=10)
        svm_mean = scores.mean()
        svm_std = scores.std()
        svm_prediction = clf1.fit(X_train, y_train).predict(X_test[-1].reshape(-1, 34))[0]

        # XG boosting
        clf2 = XGBClassifier(random_state=0)
        scores = cross_val_score(clf2, X_train, y_train, cv=10)
        xg_mean = scores.mean()
        xg_std = scores.std()
        xg_prediction = clf2.fit(X_train, y_train).predict(X_test[-1].reshape(-1, 34))[0]

        # random forest
        clf3 = RandomForestClassifier(max_depth=4, random_state=0)
        scores = cross_val_score(clf3, X_train, y_train, cv=10)
        rf_mean = scores.mean()
        rf_std = scores.std()
        rf_prediction = clf3.fit(X_train, y_train).predict(X_test[-1].reshape(-1, 34))[0]

        message = ""

        # logistic regression
        message += "The logistic regression model has a mean score {} and variance {} \n".format(logistic_mean,
                                                                                                 logistic_std)
        message += "The prediction given by logistic regression model for the price trend in \n" \
                   "the next trading week is: {}".format("rising" if logistic_prediction == 0 else "falling")

        message += "\n\n"

        # support vector machine
        message += "The support vector machine model has a mean score {} and variance {} \n".format(svm_mean, svm_std)
        message += "The prediction given by the support vector machine model for " \
                   "the price trend in the next trading week is: {}" \
            .format("rising" if svm_prediction == 1 else "falling")

        message += "\n\n"

        # XG Boosting
        message += "The XG Boost model has a mean score {} and variance {} \n".format(xg_mean, xg_std)
        message += "The prediction given by the XG Boost model for " \
                   "the price trend in the next trading week is: {}".format(
            "rising" if xg_prediction == 1 else "falling")

        message += "\n\n"

        # random forest
        message += "The random forest model has a mean score {} and variance {} \n".format(rf_mean, rf_std)
        message += "The prediction given by the random forest model for " \
                   "the price trend in the next trading week is: {}".format(
            "rising" if rf_prediction == 1 else "falling")
        return message
