# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_contacts import get_contacts
from read_template import read_template

names, emails = get_contacts('contacts.txt') # read contacts
message_template = read_template('message.txt')

message_template
# # For each contact, send the email
# for name, email in zip(names, emails):
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
