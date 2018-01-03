import os
import smtplib
import sys

from configobj import ConfigObj

# ------------------------------------------------------------
def send_email(subject, to_addr, body_text):
    """
    Send an email
    """
    # path this file script
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "config.ini")

    if os.path.exists(config_path):
        cfg = ConfigObj(config_path)
        cfg_dict = cfg.dict()
    else:
        print("Config not fount! Exiting!")
        sys.exit(1)

    host = cfg_dict["server"]
    port = cfg_dict["port"]
    login_user = cfg_dict["user"]
    login_password = cfg_dict["password"]
    from_addr = cfg_dict["from_addr"]

    BODY = "\r\n".join((
                    "From: {}".format(from_addr),
                    "To: {}".format(to_addr),
                    "Subject: {}".format(subject),
                    "",
                    body_text
                    ))

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login_user, login_password)

    try:
        server.sendmail(from_addr, [to_addr], BODY)
        print("email sent")
    except:
        print("error sending mail")
    server.quit()

if __name__ == "__main__":
    subject = "Test email from Python"
    to_addr = "cmorales@thedataage.com"
    body_text = "Python rules them all!"
    send_email(subject, to_addr, body_text)
