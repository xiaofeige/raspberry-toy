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
    """
    desc:

    """
    PKT_LOGIN = u"0"
    PKT_LOGOUT = u"1"
    PKT_SPEECH = u"2"
    PKT_CMD = u"3"
    PKT_HEART_BEAT = u'4'
    PKT_WORDS = u'5'

    PKT_RASPBERRY = u"raspberry"
    PKT_CLIENT = u'client'

    def __init__(self, msg_type=None, payload=None):
        self.__msg_type = msg_type
        self.__payload = payload

    @staticmethod
    def parse_packet(data):
        """

        :param data:
        :return:
        """
        msg_array = data.split(u"|")
        return Packet(msg_array[0], msg_array[1])

    def get_message_type(self):
        return self.__msg_type

    def get_payload(self):
        return self.__payload

    def to_string(self):
        return self.__msg_type + u"|" + self.__payload

if __name__ == '__main__':
    pass

