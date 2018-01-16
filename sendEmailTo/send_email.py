
# import necessary packages
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_contacts import get_contacts
from read_template import read_template
from setup_smtp import get_smtp


def main():
    # Path directory
    path_dir = os.path.dirname(__file__)
    print('Directorio raíz: {}'.format(path_dir))

    # read contacts
    path_contacts = os.path.join(path_dir, 'contacts.txt')
    names, emails = get_contacts(path_contacts)

    path_message = os.path.join(path_dir, 'message.txt')
    message_template = read_template(path_message)

    path_config = os.path.join(path_dir, 'config.ini')
    s, from_addr = get_smtp(path_config)

    # For each contact, send the email
    for name, email in zip(names, emails):
        print('Enviando a: {} {}'.format(name, email))
        msg = MIMEMultipart()  # Create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = from_addr
        msg['To'] = email
        msg['Subject'] = 'This is test'

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        try:
            # send the message via the server set up earlier.
            s.send_message(msg, from_addr=from_addr, to_addrs=email)
            print('Ok the email has sent')
        except Exception:
            print('Can\'t send the email')

        del msg
    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
