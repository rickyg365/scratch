import os

from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv(r'C:\Users\ricky\Documents\python_scripts\git_ready\scratch\league_autogui\read.env')

# print(os.environ)
# get connected to mail server
host = os.getenv('EMAIL_HOST')
port = os.getenv('EMAIL_PORT')

date_fmt = '%b %d, %Y [%I:%M %p]'
msg_date_fmt = '%b %d, %Y [%I:%M %p] '

# port 587,
print(f"{datetime.now().strftime(date_fmt)}: loading server")
server = smtplib.SMTP(host, port)
server.connect(host, port)
# identify ourselves to smtp gmail client
server.ehlo()
# secure our email with tls encryption
server.starttls()
# re-identify ourselves as an encrypted connection
server.ehlo()

# Next, log in to your server
print(f"{datetime.now().strftime(date_fmt)}: logging in")
server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
print(f"{datetime.now().strftime(date_fmt)}: login successful!")
# To and From
receiver = os.getenv('EMAIL_RECEIVER')
sender = os.getenv('EMAIL_HOST_USER')

# Send the mail
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = 'League of Legends'
message = f"\n{datetime.now().strftime(msg_date_fmt)}: Match is ready!  "

msg.attach(MIMEText(message))

print(f"{datetime.now().strftime(date_fmt)}: sending message")

# This will depend on your cell provider.
server.sendmail(sender, receiver, msg.as_string())
print(f"{datetime.now().strftime(date_fmt)}: message sent!")
server.quit()
