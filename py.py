#!/usr/bin/env python3

import socket
import time
import datetime

srv = {'drive.google.com':'', 'mail.google.com':'', 'google.com':''}

while 1==1 :
  for host in srv:
    ip = socket.gethostbyname(host)
    print(host + '-' + ip)

    if not srv[host]:
      srv[host] = ip

    if ip != srv[host]:
      print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + host +' IP mistmatch: '+srv[host]+' '+ip)
      srv[host]=ip

  time.sleep(1)
