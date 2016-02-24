from incoming import Incoming
import email


class GetMessages(Incoming):

    def get_headers(self):
        header_list = []
        if self.error:
            return self.error
        try:
            connect = self.connect()
        except connect.error:
            self.error = "Unable to connect to IMAP server"
            return self.error
        try:
            connect.login(self.user, self.password)
        except connect.error:
            self.error = 'Connected to IMAP server, but unable to login.'
            return self.error

        connect.select('Inbox')
        try:
            typ, messages = connect.search(None, '(UNSEEN)')
        except connect.error:
            if self.connect().error:
                self.error = 'Invalid Mailbox supplied'
                return self.error
        if typ != 'OK':
            self.error = 'Found no messages'
            return self.error
        for num in messages[0].split():
            stat, data = connect.fetch(num, '(BODY.PEEK[HEADER])')
            bytes_trash, header_bytes = data[0]
            msg = email.message_from_bytes(header_bytes)
            connect.store(num, '+FLAGS', '\SEEN')
            header_list.append(msg)

        connect.close()
        connect.logout()
        return header_list






