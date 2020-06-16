import baostock as bs
import pandas as pd
import datetime


class stockData:
    def __init__(self, ticker):
        lg = bs.login(user_id="anonymous", password="123456")
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

        if ticker[0] == '6':
            ticker = 'sh.' + ticker
        else:
            ticker = 'sz.' + ticker

        self.ticker = ticker
        self.today = datetime.datetime.today().strftime("%Y-%m-%d")

    def get_ticker(self):
        return self.ticker

    def get_stock_price(self):
        # get intraday data online
        ticker = self.ticker
        date_today = self.today
        rs = bs.query_history_k_data_plus(ticker,
                                          "open,high,close,low,volume",
                                          start_date='2013-07-01', end_date=date_today,
                                          frequency="d", adjustflag="3")
        print('query_history_k_data_plus respond error_code:' + rs.error_code)
        print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)

        # print results
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # append results
            data_list.append(rs.get_row_data())

        intraday = pd.DataFrame(data_list, columns=rs.fields)
        bs.logout()

        return intraday
