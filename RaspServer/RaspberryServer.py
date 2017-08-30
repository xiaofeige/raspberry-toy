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
import json
import os
import sys
import tornado.web
import tornado.websocket
import tornado.ioloop
from protocol.packet import Packet

sys.path.append("..")


class RaspberryHandler(tornado.websocket.WebSocketHandler):
    """

    """
    clients = {}
    count = 0

    def open(self):
        print "New client connected"
        pkt = Packet(Packet.PKT_LOGIN, "You are connected,so, who are you?")
        self.write_message(pkt.to_string())

        RaspberryHandler.count += 1
        RaspberryHandler.clients[self] = RaspberryHandler.count

    def on_message(self, message):
        print message
        pkt = Packet.parse_packet(data=message)
        if pkt.get_message_type() == Packet.PKT_LOGIN:
            print pkt.get_payload() + " login..."
            if pkt.get_payload() == Packet.PKT_RASPBERRY:
                RaspberryHandler.clients['raspberry'] = self
        else:
            RaspberryHandler.clients['raspberry'].write_message(message)

    def on_close(self):
        print "Client disconnected"
        del RaspberryHandler.clients[self]


class RaspberryApplication(tornado.web.Application):
    def __init__(self):
        # self.__raspberry_server = RaspberryHandler()
        handlers = [
            (r"/", RaspberryHandler),
        ]

        settings = {
            'template_path': 'html',
            'static_path':  'static',
        }
        tornado.web.Application.__init__(self, handlers, **settings)

    def send_voice(self, msg):
        pass


if __name__ == "__main__":
    curr_path = os.path.dirname(__file__)
    if curr_path == '':
        curr_path = '.'
    with open(curr_path + "/config", 'r') as f:
        server_config = json.load(f)
    raspberry_server = RaspberryApplication()
    raspberry_server.listen(server_config["server_port"])
    tornado.ioloop.IOLoop.instance().start()