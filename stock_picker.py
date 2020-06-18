from classifiers import classifier
from dataframe import stockData


def main():
    f = open("selected_tickers.txt", "a")
    stock_data = stockData()
    all_tickers = stock_data.get_all_tickers()
    for ticker in all_tickers:
        df = stock_data.get_stock_price(ticker[3:])
        if len(df) == 0:
            continue
        else:
            cur_classifier = classifier(df)
            max_auc = cur_classifier.get_max_auc()
            if max_auc >= 0.7:
                f.write('ticker: ' + ticker + ', max_auc: ' + str(max_auc))

    f.close()
    return


main()
