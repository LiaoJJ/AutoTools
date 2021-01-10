import smtplib


def send_email(subject, text, receiver):
    TO = receiver

    # Gmail Sign In
    gmail_sender = 'jjliao14@gmail.com'
    gmail_passwd = 'lfxiggycekbnlpry'
    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % subject,
                            '', text])

        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()
