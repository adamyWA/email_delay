from sendemail import SendEmail
from getmessages import GetMessages
from calculatedelay import CalculateDelay
from grandmasterflash import GrandmasterFlash
import time

furious_five = GrandmasterFlash()


send_email = SendEmail()
send_email.config_connection(host='smtp.xxx.com', port=465, user='xxx@smtp.com', password='xxx')
send_email.send(send_to='xxx@recipient.com', message=furious_five.the_message(), subject='One word subjects are no good.')

if send_email.error:
    print(send_email.error)
    exit()
else:
    print('='*25)
    print('Message sent....')
    print('='*25)
    count = 3
    while count:
        time.sleep(20)
        print("Working...")
        count -= 1

messages = GetMessages()
messages.config_connection(user='xxx@imap.com', port=993, password='xxx', host='imap.xxx.com')


calculate = CalculateDelay()
messages.connect()

if messages.error:
    print(messages.error)
    exit()

values = calculate.calculate_delay(messages)

if values.error:
    print(values.error)
    exit()

print(len(values.results))

for value in values.results:
    server, time = value
    print('Received: ' + server)
    print(time)
    exit()


