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
import thread
import json
import time


class RaspberryClient(object):
    def __init__(self):
        curr_path = os.path.dirname(__file__)
        with open(curr_path+"/config", 'r') as f:
            self.__config = json.load(f)
        websocket.enableTrace(True)
        self.__ws = websocket.WebSocketApp(self.__config["server_host"],
                                           on_message=self.on_message,
                                           on_error=self.on_error,
                                           on_close=self.on_close)
        self.__ws.on_open = self.on_open
        self.__ws.run_forever()

    def __del__(self):
        pass

    def on_message(self, ws, msg):
        """

        :param ws:
        :param msg:
        :return:
        """
        print msg

    def on_error(self, ws, error):
        """

        :param ws:
        :param error:
        :return:
        """
        print "oops...error occured....due to %s " % str(error)

    def on_close(self, ws):
        print "this connection is closing..."

    def on_open(self, ws):
        print "connetion trying to build..."

        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            # ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())


def main():
    """

    :return:
    """
    client = RaspberryClient()
    return 0

if __name__ == '__main__':
    sys.exit(main())

