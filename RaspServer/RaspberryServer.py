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


class RaspberryServer(tornado.websocket.WebSocketHandler):
    """

    """
    def open(self):
        print "New client connected"
        self.write_message("You are connected")

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print "Client disconnected"


application = tornado.web.Application([
    (r"/", RaspberryServer),
])

if __name__ == "__main__":
    curr_path = os.path.dirname(__file__)
    with open(curr_path + "/config", 'r') as f:
        server_config = json.load(f)
    application.listen(server_config["server_port"])
    tornado.ioloop.IOLoop.instance().start()