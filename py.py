#!/usr/bin/env python3

import socket
import time
import datetime
import json
import yaml

srv = {'drive.google.com':'', 'mail.google.com':'', 'google.com':''}

while 1==1 :
  with open('json_data.json') as json_file:
    data = json.load(json_file)

  for host in srv:
    ip = socket.gethostbyname(host)
    data[host] = ip

    # json write
    json_object = json.dumps(data)
    print(host + '-' + ip)
    with open('json_data.json', 'w') as outfile:
      outfile.write(json_object)

    # yaml write
    dataYaml = []
    for el in data:
      str = el + ':' + data[el]
      dataYaml.append(str)
    with open('data.yml', 'w') as outfile:
      yaml.dump(dataYaml, outfile, default_flow_style=False)

    if not srv[host]:
      srv[host] = ip

    if ip != srv[host]:
      print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + host +' IP mistmatch: '+srv[host]+' '+ip)
      srv[host]=ip

  time.sleep(1)
