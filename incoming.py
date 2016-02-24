from connection import Connection
import imaplib
import socket


class Incoming(Connection):

    def __init__(self):
        super().__init__()
        self.imap = imaplib

    def connect(self):
        socket.setdefaulttimeout(15)
        imap = None
        try:
            imap = self.imap.IMAP4_SSL(self.host, self.port)
        except socket.gaierror:
            self.error = "Unable to connect to IMAP server - 01"
            return self.error
        except OSError:
            self.error = "Unable to connect to IMAP server - 02"
        except TimeoutError:
            self.error = "Connection to IMAP server timed out"
        if imap:
            return imap
        else:
            self.error = 'Unknown IMAP Connection Error'
            return self.error