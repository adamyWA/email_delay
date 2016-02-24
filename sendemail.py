from outgoing import Outgoing
from message import Message
import socket


class SendEmail(Outgoing):

    def send(self, **kwargs):
        try:
            smtp = self.connect()
        except socket.gaierror:
            self.error = 'No message sent: \nPlease check port and hostname before retrying'
            return self.error
        except OSError:
            self.error = 'No message sent: \nCould not connect on provided port/hostname'
            return self.error
        # instantiate message and pass kwargs
        message = Message()
        try:
            smtp.login(self.user, self.password)
        except self.smtp.SMTPException:
            self.error = 'No message sent: Unable to verify your credentials'
            return self.error
        try:
            smtp.sendmail(msg=message.create_message(**kwargs), to_addrs=message.send_to, from_addr=self.user)
        except self.smtp.SMTPException as smtp_error:
            self.error = 'No message sent: ' + str(smtp_error)
            return self.error

