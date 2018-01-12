
# import necessary packages
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_contacts import get_contacts
from read_template import read_template

# Path directory
path_dir = os.path.dirname(__file__)
print('Directorio raíz: {}'.format(path_dir))

# read contacts
names, emails = get_contacts(os.path.join(path_dir, 'contacts.txt'))
# message_template = read_template('message.txt')


# print(message_template)
# # For each contact, send the email
for name, email in zip(names, emails):
    print('{} {}'.format(name, email))
    #     msg = MIMEMultipart() # Create a message
    #
    #     # add in the actual person name to the message template
    #     message = message_template.substitute(PERSON_NAME=name.title())
    #
    #     # setup the parameters of the message
    #     msg['From'] = ''
    #     msg['To'] = ''
    #     msg['Subject'] = 'This is test'
    #
    #     # add in the message body
    #     msg.attach(MIMEText(message, 'plain'))
    #
    #     # send the message via the server set up earlier.
    #     s.send_message(msg)
    #
    #     del msg
