#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: RaspberryClient.py
@time: 2016/12/12 23:52
"""
import os
import sys
import websocket
import json
from protocol.packet import Packet
from websocket import create_connection


class RaspberryClient(object):
    def __init__(self):
        curr_path = os.path.split(os.path.realpath(__file__))[0]
        with open(curr_path+"/config", 'r') as f:
            self.__config = json.load(f)

        self.ws = create_connection(url=self.__config["client"]["host_port"])

    def reconnect(self):
        """

        :return:
        """
        pass

    def login(self):
        try:
            pkt = Packet(Packet.PKT_LOGIN, Packet.PKT_CLIENT)
            self.ws.send(pkt.to_string())
            msg = self.ws.recv()
            print msg
            return 0
        except websocket._exceptions.WebSocketConnectionClosedException:
            print "network initialize failed..."
            return 1

    def start(self):
        """

        :return:
        """
        if self.login() > 0:
            print "failed to login..."
            return
        while True:
            try:
                data = raw_input("cmd>:")
                pkt = Packet(Packet.PKT_WORDS, data)
                self.ws.send(pkt.to_string())
                msg = self.ws.recv()
                print msg
            except KeyboardInterrupt:
                self.ws.close()
                break


def main():
    """

    :return:
    """
    client = RaspberryClient()
    print "starting client..."
    client.start()
    return 0

if __name__ == '__main__':
    sys.exit(main())

