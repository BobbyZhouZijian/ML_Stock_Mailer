from classifiers import classifier
from mailer import mailer
from settings import get
from api_fetcher import response


def main():
    res = response

    for ticker_obj in res:
        ticker = ticker_obj['name']
        message = classifier(ticker).get_report_message()
        mailer(message, ticker).send_email(get("receiver_email"),
                                           get("sender_email"), get("sender_password"), get("smtp_server"))
    return


if __name__ == "__main__":
    main()
