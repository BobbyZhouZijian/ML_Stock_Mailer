import smtplib
import ssl


class mailer:

    def __init__(self, message, ticker):
        self.message = message
        self.ticker = ticker

    def send_email(self, receiver_email, sender_email, sender_password, smtp_server):
        port = 587  # For starttls
        smtp_server = smtp_server
        sender_email = sender_email
        receiver_email = receiver_email
        print(receiver_email)
        password = sender_password
        subject = "ML Weekly Report"
        message = """
Dear Subscriber:

    The following is the price prediction provided using our ML analysis service.

stock price predicted is for Stock No: {}

{}

Hope you have a good day and make lots of fortune!


Regards,
Zijian's ML generator on behalf of zijian

(Note: The report is automatically generated and only serves as a reference. You SHOULD NOT rely on it for 
making any trading decisions!)
""".format(self.ticker, self.message)

        content = 'Subject: {}\n\n{}'.format(subject, message)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, content)
