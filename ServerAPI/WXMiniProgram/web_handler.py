#!/usr/bin/env python
# encoding: utf-8


"""
@author: fayren
@time: 2018/5/9
"""
import tornado.web


class WXMiniProgramHandler(tornado.web.RequestHandler):
    """

    """
    def get(self):
        self.write("hello! from fayren!")


if __name__ == '__main__':
    pass