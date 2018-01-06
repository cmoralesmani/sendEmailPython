import os
import smtplib
import string
import sys

from configobj import ConfigObj
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

"""------------------------------------------
Send Email

Params:
subject str
body_text str
emails list

------------------------------------------"""
def send_email_with_attachment(subject,
                               body_text,
                               to_emails,
                               cc_emails,
                               bcc_emails,
                               file_to_attach):
    """
    Send an email with an attachment
    """
    # path this file script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # path/config.ini
    config_path = os.path.join(base_path, "config.ini")
    header = (
              "Content-Disposition",
              "attachment; filename= {}".format(file_to_attach)
             )

    # get the config
    if os.path.exists(config_path):
        cfg = ConfigObj(config_path)
        cfg_dict = cfg.dict()
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    # extract server, login and from_addr from config
    host = cfg_dict["server"]
    port = cfg_dict["port"]
    login_user = cfg_dict["user"]
    login_password = cfg_dict["password"]
    from_addr = cfg_dict["from_addr"]

    # create the message
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    if body_text:
        msg.attach(MIMEText(body_text))
    msg["To"] = ", ".join(to_emails)
    msg["cc"] = ", ".join(cc_emails)
    msg["bcc"] = ", ".join(bcc_emails)

    attachment = MIMEBase("application", "octet-stream")

    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header(*header)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file {}".format(file_to_attach)
        print(msg)
        sys.exit(1)

    emails = to_emails + cc_emails + bcc_emails

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login_user, login_password)

    try:
        server.sendmail(from_addr, emails, msg.as_string())
        print("email sent")
    except:
        print("error sending mail")

    server.quit()

"""------------------------------------------
Program start
------------------------------------------"""
if __name__ == "__main__":
    to_emails = ["cmorales@thedataage.com"]
    cc_emails = ["camd.jun@yahoo.com"]
    bcc_emails = ["camd.jun@hotmail.com"]
    subject = "Test email with attachment from Python"
    body_text = "This email contains an attachment!"
    path = os.path.join(
                        os.path.dirname(os.path.abspath(__file__)),
                        "logo.png"
                       )
    print(path)
    send_email_with_attachment(subject, body_text, to_emails, cc_emails, bcc_emails, path)
