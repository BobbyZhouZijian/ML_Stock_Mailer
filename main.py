from classifiers import classifier
from mailer import mailer
from settings import get
import sys


def main():
    ticker = "000066" # sys.argv[1]
    message = classifier(ticker).get_report_message()
    mailer(message, ticker).send_email(get("receiver_email"),
                                       get("sender_email"), get("sender_password"), get("smtp_server"))
    return


if __name__ == "__main__":
    main()
