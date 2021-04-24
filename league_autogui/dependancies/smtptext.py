import os

from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


class TextNotifier:
    def __init__(self):
        '''
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_address, sender_pass)
    text = message.as_string()
    s.sendmail(sender_address, reciver_mail, text)
    s.quit()


        '''
        # Load Environment Variables
        env_path = r'C:\Users\ricky\Documents\python_scripts\git_ready\scratch\league_autogui\read.env'
        load_dotenv(env_path)

        # Load Variables
        self.host = os.getenv('EMAIL_HOST')
        self.port = os.getenv('EMAIL_PORT')

        self.receiver = os.getenv('EMAIL_RECEIVER')
        self.sender = os.getenv('EMAIL_HOST_USER')

        # server
        self.gmail_server = None

        self.date_fmt = '[%I:%M %p] %b %d, %Y'
        self.msg_date_fmt = '%b %d, %Y \n[%I:%M %p] '

    def send(self, text_message):
        # get connected to mail server
        self.gmail_server = smtplib.SMTP(self.host, self.port)
        print(f"{datetime.now().strftime(self.date_fmt)}: loading server")
        self.gmail_server.connect(self.host, self.port)

        # identify ourselves to smtp gmail client
        self.gmail_server.ehlo()

        # secure our email with tls encryption
        self.gmail_server.starttls()

        # re-identify ourselves as an encrypted connection
        self.gmail_server.ehlo()

        # Next, log in to your server
        print(f"{datetime.now().strftime(self.date_fmt)}: logging in")
        self.gmail_server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
        print(f"{datetime.now().strftime(self.date_fmt)}: login successful!")

        # Send the mail
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = 'League of Legends'
        message = f"{datetime.now().strftime(self.msg_date_fmt)} {text_message}  "

        msg.attach(MIMEText(message))

        print(f"{datetime.now().strftime(self.date_fmt)}: sending message")

        # This will depend on your cell provider.
        self.gmail_server.sendmail(self.sender, self.receiver, msg.as_string())
        print(f"{datetime.now().strftime(self.date_fmt)}: message sent!")
        self.gmail_server.quit()


if __name__ == "__main__":
    random_notifier = TextNotifier()
    random_notifier.send("Match Ready!")
