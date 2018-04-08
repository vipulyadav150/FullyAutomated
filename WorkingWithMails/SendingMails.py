import smtplib



def sendMail(server,senderMail,revMail,passSecure,mailBody):
    smtpObj = smtplib.SMTP(server,587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(senderMail,passSecure)
    smtpObj.sendmail(senderMail,revMail,mailBody)
    smtpObj.quit()

server = input('Enter your Email Client\'s SMTP : ')
senderMail = input('Enter sender\'s Email address : ')
revMail = input('Enter receiver\'s Email address : ')
passSecure = input('Enter the Sender Email PAssword : ')
mailBody = input('Enter Email content : ')

sendMail(server,senderMail,revMail,passSecure,mailBody)

