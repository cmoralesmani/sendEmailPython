import smtplib

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login('camd.jun@gmail.com','uxrFvl-23444')
