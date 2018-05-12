#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# SOURCE: https://habrahabr.ru/post/149077/


import socket
from common import send_msg, recv_msg


PORT = 9090


with socket.socket() as sock:
    sock.bind(('', 9090))
    sock.listen(1)

    print('Server: {}'.format(sock.getsockname()))

    while True:
        conn, addr = sock.accept()
        print('Connected:', addr)

        data = recv_msg(conn)
        print('Receiving: {}: {}'.format(len(data), data))

        print('Sending')
        send_msg(conn, data.upper())

        print('Close\n')
