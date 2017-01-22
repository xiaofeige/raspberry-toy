#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: RaspberryServer.py
@time: 2016/12/13 21:53
"""

import socket

def func():
    pass


class Server(object):
    def __init__(self):
        self.__clients = {}

    def send_msg(self, msg):
        for client in self.__clients:
            pass

    def start(self):
        pass

    def run(self):
        address = ('', 9527)
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind(address=address)
        tcp_socket.listen(5)
        while True:
            client, client_address = tcp_socket.accept()
            self.__clients[client] = client_address

if __name__ == '__main__':
    pass

