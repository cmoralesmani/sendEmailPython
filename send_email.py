import os
import smtplib
import sys

from configobj import ConfigObj

"""------------------------------------------
Send Email

Params:
subject     str
body_text   str
to_emails   list
cc_emails   list
bcc_emails  list

------------------------------------------"""


def send_email(
        subject, body_text, to_emails,
        cc_emails, bcc_emails):
    """
    Send an email
    """
    # path this file script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # path/config.ini
    config_path = os.path.join(base_path, "config.ini")

    if os.path.exists(config_path):
        cfg = ConfigObj(config_path)
        cfg_dict = cfg.dict()
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg_dict["server"]
    port = cfg_dict["port"]
    login_user = cfg_dict["user"]
    login_password = cfg_dict["password"]
    from_addr = cfg_dict["from_addr"]

    BODY = "\r\n".join((
        "From: {}".format(from_addr),
        "To: {}".format(", ".join(to_emails)),
        "CC: {}".format(", ".join(cc_emails)),
        "BCC: {}".format(", ".join(bcc_emails)),
        "Subject: {}".format(subject),
        "",
        body_text
    ))
    emails = to_emails + cc_emails + bcc_emails

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login_user, login_password)

    try:
        server.sendmail(from_addr, emails, BODY)
        print("email sent")
    except Exception:
        print("error sending mail")
    server.quit()


"""------------------------------------------
Program start
------------------------------------------"""
if __name__ == "__main__":
    to_emails = ["cmorales@thedataage.com", "camd.jun@yahoo.com"]
    cc_emails = [""]
    bcc_emails = []
    subject = "Test email from Python"
    body_text = "Python rules them all!"
    send_email(subject, body_text, to_emails, cc_emails, bcc_emails)
