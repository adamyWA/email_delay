from connection import Connection
import smtplib

class Outgoing(Connection):

    def __init__(self):
        super().__init__()
        self.smtp = smtplib

    def connect(self):
        smtp = self.smtp.SMTP_SSL(self.host, self.port)
        try:
            return smtp
        except smtp.Exception:
            return smtp.Exception
