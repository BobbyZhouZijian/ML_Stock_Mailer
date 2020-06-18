from classifiers import classifier
from mailer import mailer
from settings import get
from dataframe import stockData


def main():
    ticker = get("test_ticker")
    email = get("test_receiver_email")
    df = stockData().get_stock_price(ticker)
    message = classifier(df).get_report_message()
    mailer(message, ticker).send_email(email,
                                       get("sender_email"), get("sender_password"), get("smtp_server"))
    return


main()
