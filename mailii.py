import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

def maili():

    from_address = 'saipavan098765@gmail.com'

    to_address = 'saipavan098765@gmail.com'

    message = MIMEMultipart()


    #message['From'] = from_address

    #message['To'] = to_address

    content = MIMEText('Hi Satwika', 'plain')

    message.attach(content)

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    #mail.ehlo()

    mail.starttls()

    mail.login(from_address, '9848871539')

    mail.sendmail(from_address,to_address, message.as_string())

    mail.close()
    return("Mail Sent Successfully")
   