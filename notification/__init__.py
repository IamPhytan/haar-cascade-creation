
# Name: Haar Cascade Creation
# Desc: Creation of custom Haar Cascades Classifiers
# Repo: https://github.com/IamPhytan/haar-cascade-creation
# Author: IamPhytan
# License: MIT
# Path: -/notification

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(config, subject, body):

    if config['EMAIL']['WITH_EMAIL_NOTIFICATIONS']:

        fromaddr = 'Haar Cascade Creation'
        recipients = config['EMAIL']['EMAIL_TO']
        cc_recipients = config['EMAIL']['EMAIL_CC']
        login = config['EMAIL']['EMAIL_LOGIN']
        password = config['EMAIL']['EMAIL_PASSWORD']

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ', '.join(recipients)
        msg['Cc'] = ', '.join(cc_recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        server = smtplib.SMTP(config['EMAIL']['EMAIL_SERVER'])
        server.starttls()
        server.login(login, password)
        server.sendmail(fromaddr, recipients, msg.as_string())
        server.quit()


def set_completed(config, new_set_name, old_set_name):
    email_subject = '[OpenCV] The following set: {} is now fully downloaded.'.format(old_set_name)
    email_message = "Now downloading pictures of {}".format(new_set_name)
    send_email(config, subject=email_subject, body=email_message)