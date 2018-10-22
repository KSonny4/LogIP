import logging
import datetime
from time import sleep

from requests import get


# TODO: Better log name
date = datetime.date.today().strftime("%d-%m-%Y")
logname = str(date) + '.log'

logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S',
                            level=logging.INFO)

while True:
    ip_v4 = get('https://v4.ident.me').text
    ip_v6 = get('https://v6.ident.me').text

    str_ip_v4 = 'My public IPv4 address is = ' + ip_v4
    str_ip_v6 = 'My public IPv6 address is = ' + ip_v6

    print(str_ip_v4)
    print(str_ip_v6)

    logging.info(str_ip_v4)
    logging.info(str_ip_v6)

    sleep(3600)