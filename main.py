from classifiers import classifier
from mailer import mailer
from settings import get


def main():
    ticker = get("ticker")
    message = classifier(ticker).get_report_message()
    mailer(message, ticker).send_email(get("receiver_email"),
                                       get("sender_email"), get("sender_password"), get("smtp_server"))


if __name__ == "__main__":
    main()
