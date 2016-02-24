import re
from email.utils import parsedate_to_datetime
from pytz import timezone

class ParseReceived:
    def __init__(self):
        self.error = None
        self.results = None

    def get_parsed(self, message_set):
        parsed_list = []
        header_list = []
        header_time = []

        headers = False
        local_time = timezone('UTC')

        if not isinstance(message_set, str):
            for message in message_set:
                headers = message.get_all('RECEIVED') # only handles single email, will revisit

            while headers:
                try:
                    match = re.search('([a-zA-Z]{3},.+.[0-9].+[0-9]{4})', headers[len(headers) - 1], re.DOTALL)
                    if match:
                        match = match.group().replace('\r\n', '')
                        header_time.append(parsedate_to_datetime(match).astimezone(local_time).strftime("%Y-%m-%d %H:%M:%S"))
                except IndexError:
                    continue
                header_list.append(headers[len(headers) - 1])
                headers.pop(len(headers)-1)
            parsed_list.append(list(zip(header_list, header_time)))
            return parsed_list
        else:
            self.error = message_set
            return self
