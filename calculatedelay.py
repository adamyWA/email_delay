import datetime
from parsereceived import ParseReceived
import itertools


class CalculateDelay(ParseReceived):

    def calculate_delay(self, get_messages_object):
        time_list = []
        server_list = []

        got_headers = get_messages_object.get_headers()

        if not isinstance(got_headers, str):
            fmt = "%Y-%m-%d %H:%M:%S"
            header_tuple = self.get_parsed(got_headers)
            if header_tuple:
                for tups in header_tuple:
                    server_and_time = []
                    if self.error:
                        return self

                    for tup in tups:
                        server_name, timestamp = tup
                        server_list.append(server_name)
                        try:
                            time_list.append(datetime.datetime.strptime(timestamp, fmt))
                        except TypeError:
                            pass

                counter = 0
                server_count = 1
                server_and_time = []
                for time, server in list((itertools.zip_longest(time_list, server_list))):
                    if counter == 0:
                        server_and_time.append((server_list[counter], '*'))
                    try:
                        delay = time_list[1::][counter] - time_list[counter]
                        if delay.days >= 0:
                            server_and_time.append((server_list[server_count], delay)) # add server name and delay as tuple to new list
                            counter += 1 # increment counter
                            server_count += 1
                        else:
                            server_and_time.append((server_list[server_count], '*')) # if timedelta is negative, add filler string in place of timedelta
                            counter +=1 # counter should still be incremented
                            server_count += 1
                    except IndexError:
                        pass
                self.results =  server_and_time
                return self


        else:
            self.error = got_headers
            return self
