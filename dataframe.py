import baostock as bs
import pandas as pd
import datetime


class stockData:
    def __init__(self):
        lg = bs.login(user_id="anonymous", password="123456")
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)

        self.today = datetime.datetime.today().strftime("%Y-%m-%d")

    def get_all_tickers(self):
        rs = bs.query_all_stock(day=self.today)
        # print results
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # append results
            data_list.append(rs.get_row_data())

        df = pd.DataFrame(data_list, columns=rs.fields)

        return df['code'].values

    def get_stock_price(self, ticker):

        if ticker[0] == '6':
            ticker = 'sh.' + ticker
        else:
            ticker = 'sz.' + ticker

        # get intraday data online
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
