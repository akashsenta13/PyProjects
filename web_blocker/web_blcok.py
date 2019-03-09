# program to block website during your working hours
import time
from datetime import datetime as dt

hosts_temp = 'hosts'
hosts_file = '/etc/hosts'
redirect = '127.0.0.1'
website_list = [
    'www.facebook.com', 'facebook.com', 'youtube.com', 'www.youtube.com'
]

while True:
    # working hours from 10 to 17
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 10) < dt.now() < dt(dt.now().year,
                                            dt.now().month,
                                            dt.now().day, 17):
        print('working hours....')
        with open(hosts_file, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print('fun hours...')
        with open(hosts_file, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)