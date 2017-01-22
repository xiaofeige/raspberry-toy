#!/usr/bin/env python
# encoding: utf-8

from __future__ import with_statement
import json
"""
@version: ??
@author: luffyren
@site: http://www.luffyren.club
@software: PyCharm Community Edition
@file: ConfigManage.py
@time: 2016/12/13 0:00
"""


def get_settings():
    """解析配置文件"""
    with open("config.json") as config:
        return json.load(config)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

