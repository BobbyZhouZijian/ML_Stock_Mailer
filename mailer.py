import smtplib
import ssl
from email_format import get_format


class mailer:

    def __init__(self, messages, ticker):
        self.messages = messages
        self.ticker = ticker

    def send_email(self, receiver_email, sender_email, sender_password, smtp_server):
        sender_email = sender_email

        port = 587  # For starttls
        smtp_server = smtp_server
        password = sender_password
        messages = self.messages
        msg_full = get_format(sender_email, receiver_email, self.ticker, messages[0],
                              messages[1], messages[2], messages[3], messages[4])

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg_full)

        return
