from classifiers import classifier
from mailer import mailer
from settings import get


def main():
    ticker = get("test_ticker")
    email = get("test_receiver_email")
    message = classifier(ticker).get_report_message()
    mailer(message, ticker).send_email(email,
                                       get("sender_email"), get("sender_password"), get("smtp_server"))
    return


main()
