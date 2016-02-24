import time
from email.mime.text import MIMEText


class Message:
    def __init__(self):
        self.current_time = time.strftime("%m/%d/%Y >>  %H:%M:%S")
        self.message = 'Message Received'
        self.send_to = 'recipient@example.com'

    def create_message(self, **kwargs):
        subject = self.current_time
        if 'send_to' in kwargs:
            self.send_to = kwargs['send_to']
        if 'message' in kwargs:
            self.message = kwargs['message']
        if 'subject' in kwargs:
            subject = kwargs['subject']

        msg = MIMEText(self.message)
        msg['Subject'] = subject
        msg['To'] = self.send_to

        return msg.as_string()