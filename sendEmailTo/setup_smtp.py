import os
import smtplib
from configobj import ConfigObj


def get_smtp(
        filename):
    """
    Return the SMTP Object and the from email
    """

    if os.path.exists(filename):
        cfg = ConfigObj(filename)
        cfg_dict = cfg.dict()
    else:
        print("Not found: {}".format(filename))

    host = cfg_dict["server"]
    port = cfg_dict["port"]
    user = cfg_dict["user"]
    password = cfg_dict["password"]
    from_addr = cfg_dict["from_addr"]

    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(user, password)

    return s, from_addr
