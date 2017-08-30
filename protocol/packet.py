#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: packet.py
@time: 2017/2/17 14:37
"""


class Packet(object):
    def __init__(self, msg_type=None, payload=None):
        self.__msg_type = msg_type
        self.__payload = payload

    def parse_packet(self, data):
        """

        :param data:
        :return:
        """
        msg_array = data.split("|")
        self.__msg_type = msg_array[0]

    def get_message_type(self):
        return self.__msg_type

if __name__ == '__main__':
    pass

