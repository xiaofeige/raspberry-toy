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

import tornado.ioloop
import tornado.web
import tornado.websocket

from ServerAPI.WXMiniProgram.web_handler import *
from ServerAPI.Rasberry.RasberryHandler import *


class RaspberryApplication(tornado.web.Application):
    def __init__(self):
        # self.__raspberry_server = RaspberryHandler()
        handlers = [
            (r"/", RaspberryHandler),
            (r"/mini-program", WXMiniProgramHandler),
        ]

        settings = {
            'template_path': 'html',
            'static_path':  'static',
        }
        tornado.web.Application.__init__(self, handlers, **settings)

    def send_voice(self, msg):
        pass


if __name__ == "__main__":
    curr_path = os.path.split(os.path.realpath(__file__))[0]
    with open(curr_path + "/config", 'r') as f:
        server_config = json.load(f)
    raspberry_server = RaspberryApplication()
    raspberry_server.listen(server_config["server"]["server_port"])
    tornado.ioloop.IOLoop.instance().start()