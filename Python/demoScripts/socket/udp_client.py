# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah', b'exit']:
    # 发送数据:
    s.sendto(data, ('172.105.199.214', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()