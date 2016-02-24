import hashlib


class Connection:

    def __init__(self):
        self.error = None
        self.port = 465
        self.password = 'password'
        self.user = 'sender@example.com'
        self.host = 'mail.mailserver.com'

    def config_connection(self, **kwargs):
        if 'port' in kwargs:
            try:
                self.port = int(kwargs['port'])
            except ValueError:
                self.error = 'Invalid Port Specified, revert port to ' + str(self.port)
                #  create logger and log this event
        if 'host' in kwargs:
            self.host = kwargs['host']
        if 'user' in kwargs:
            self.user = kwargs['user']
        if 'password' in kwargs:
            self.password = kwargs['password']

    def show_current(self):
        hashed = hashlib.md5()
        hashed.update(self.password.encode('utf-8'))
        return {'port': self.port, 'host': self.host, 'user': self.user, 'password': hashed.hexdigest()}
