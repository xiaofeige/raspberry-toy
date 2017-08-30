#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: RaspTalker.py
@time: 2017/1/22 17:10
"""

import os


class RaspSound():
    def __init__(self):
        pass

    def play_music(self):
        pass

    def say(self, msg, is_chinese=True):
        """

        :param msg:
        :param is_chinese:
        :return:
        """
        cmd = None
        if is_chinese:
            cmd = "espeak -vzh '%s'" % msg
        else:
            cmd = "espeak -ven+f3 -k5 -s150 '%s'" % msg
        os.system(cmd)

if __name__ == '__main__':
    test = RaspSound()
    test.say("你好")

