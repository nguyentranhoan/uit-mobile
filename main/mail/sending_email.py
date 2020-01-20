import mimetypes
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
from oauth2client import file
from json import dumps

from pydantic import EmailStr

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Gmail API Python Send Email'


def get_credentials():
    home_dir = os.path.expanduser('~')
    print(home_dir)
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)


def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def CreateMessage(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body


def create_message_with_attachment(
        sender, to, subject, message_text, file):
    """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    file: The path to the file to be attached.

  Returns:
    An object containing a base64url encoded email object.
  """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    content_type, encoding = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(file, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(file, 'rb ')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)
    return {'raw': base64.urlsafe_b64encode(message.as_bytes())}


def reset_pass_mail(to: EmailStr, normal_account: str):
    sender = "hoannguyen.meete@gmail.com"
    subject = "[welcome to UIT Mobile]"
    msg_html = f"""\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           MESSAGE FROM PERSONAL TESTS APP<br>
            <h1>Your username: {normal_account}</h1>
           <br>Click here <a href="http://localhost:8088/reset/password/successful">LINK</a> to reset password.</br>
        </p>
      </body>
    </html>
    """
    msg_plain = "uit"
    SendMessage(sender, to, subject, msg_html, msg_plain)


def validate_user_mail(to: EmailStr):
    sender = "hoannguyen.meete@gmail.com"
    subject = "[welcome to UIT Mobile]"
    msg_html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           MESSAGE FROM PERSONAL TESTS APP<br>
           Click here <a href="http://localhost:8088/register/successful">LINK</a> to register user.
        </p>
      </body>
    </html>
    """
    msg_plain = "uit"
    SendMessage(sender, to, subject, msg_html, msg_plain)


def recommend_friend_to(to: EmailStr, from_whom: EmailStr):
    sender = "hoannguyen.meete@gmail.com"
    subject = "[welcome to UIT Mobile]"
    msg_html = f"""\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           MESSAGE FROM PERSONAL TESTS APP<br>
           Hi {to}, {from_whom} wants to get in touch with you. send {from_whom} an email to connect.
        </p>
      </body>
    </html>
    """
    msg_plain = "uit"
    SendMessage(sender, to, subject, msg_html, msg_plain)


def recommend_friend_from(to: EmailStr, from_whom: EmailStr):
    sender = "hoannguyen.meete@gmail.com"
    subject = "[welcome to UIT Mobile]"
    msg_html = f"""\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           MESSAGE FROM PERSONAL TESTS APP<br>
           Hi {from_whom}, we've sent your request friend to {to}.
        </p>
      </body>
    </html>
    """
    msg_plain = "uit"
    SendMessage(sender, from_whom, subject, msg_html, msg_plain)


# def recommend_friend_to(to: EmailStr, from_whom: EmailStr):
#     rec = str(to)
#     sen = str(from_whom)
#     sender = "hoannguyen.meete@gmail.com"
#     subject = "[welcome to UIT Mobile]"
#     msg_html = f"""\
#     <html>
#       <head></head>
#       <body>
#         <p>Hi!<br>
#            MESSAGE FROM PERSONAL TESTS APP<br>
#            Hi {rec}, {sen} wants to get in touch with you. send {sen} an email to connect.
#         </p>
#       </body>
#     </html>
#     """
#     msg_plain = "uit"
#     SendMessage(sender, to, subject, msg_html, msg_plain)
#
#
# def recommend_friend_from(to: EmailStr, from_whom: EmailStr):
#     rec = str(to)
#     sen = str(from_whom)
#     sender = "hoannguyen.meete@gmail.com"
#     subject = "[welcome to UIT Mobile]"
#     msg_html = f"""\
#     <html>
#       <head></head>
#       <body>
#         <p>Hi!<br>
#            MESSAGE FROM PERSONAL TESTS APP<br>
#            Hi {sen}, we've sent your request friend to {rec}.
#         </p>
#       </body>
#     </html>
#     """
#     msg_plain = "uit"
#     SendMessage(sender, from_whom, subject, msg_html, msg_plain)
