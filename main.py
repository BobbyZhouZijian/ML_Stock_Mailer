from classifiers import classifier
from mailer import mailer
from settings import get
from api_fetcher import response
from dataframe import stockData


def main():
    res = response

    for ticker_obj in res:
        ticker = ticker_obj['name']
        email = ticker_obj['uid']
        df = stockData().get_stock_price(ticker)
        message = classifier(df).get_report_message()
        mailer(message, ticker).send_email(email,
                                           get("sender_email"), get("sender_password"), get("smtp_server"))
    return


if __name__ == "__main__":
    main()
