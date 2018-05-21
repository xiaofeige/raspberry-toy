#!/usr/bin/env python
# encoding: utf-8


"""
@author: fayren
@time: 2018/5/9
"""

import tornado.websocket
from protocol.packet import Packet


class RaspberryHandler(tornado.websocket.WebSocketHandler):
    """

    """
    clients = []
    agents = []
    count = 0

    def open(self):
        print "New client connected"
        pkt = Packet(Packet.PKT_LOGIN, "You are connected,so, who are you?")
        self.write_message(pkt.to_string())

    def broadcast(self, msg):
        """

        :param msg:
        :return:
        """
        for agent in RaspberryHandler.agents:
            agent.write_message(msg)

    def on_message(self, message):
        pkt = Packet.parse_packet(data=message)
        if pkt.get_message_type() == Packet.PKT_LOGIN:
            print pkt.get_payload() + " login..."
            if pkt.get_payload() == Packet.PKT_RASPBERRY:
                RaspberryHandler.agents.append(self)
            elif pkt.get_payload() == Packet.PKT_CLIENT:
                RaspberryHandler.clients.append(self)
        else:
            try:
                self.broadcast(message)
            except:
                print "raspberry not found..."

    def on_close(self):
        print "Client disconnected"
        try:
            RaspberryHandler.clients.remove(self)
            RaspberryHandler.agents.remove(self)
        except ValueError:
            pass


if __name__ == '__main__':
    pass