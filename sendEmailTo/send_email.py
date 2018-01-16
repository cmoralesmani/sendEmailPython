
# import necessary packages
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_contacts import get_contacts
from read_template import read_template


def main():
    # Path directory
    path_dir = os.path.dirname(__file__)
    print('Directorio raíz: {}'.format(path_dir))

    # read contacts
    names, emails = get_contacts(os.path.join(path_dir, 'contacts.txt'))
    message_template = read_template(os.path.join(path_dir, 'message.txt'))

    # set up the SMTP server
    s = smtplib.SMTP(host='', port='')
    s.starttls()
    s.login('', '')

    # For each contact, send the email
    for name, email in zip(names, emails):
        print('{} {}'.format(name, email))
        msg = MIMEMultipart()  # Create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake

        # setup the parameters of the message
        msg['From'] = ''
        msg['To'] = ''
        msg['Subject'] = 'This is test'

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg
    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
