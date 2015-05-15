#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Rafael Figueroa
Send data from drone to ground station
"""

import socket

class Socket_ground(object):

    def __init__(self):
        # Symbolic name meaning all available interfaces
        HOST = ''
        # Arbitrary non-privileged port
        PORT = 50007  

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        socket.setdefaulttimeout(1.0)
        print 'Listen for incoming connections'
        self.sock.listen(1)  
        # Wait for connection
        self.conn, self.addr = self.sock.accept()
        print 'Connected by', self.addr

    def receive_data(self):
        print 'receiving data'
        self.data = self.conn.recv(1024)
        print 'Received:', self.data

        if not self.data: 
            print 'no more data'
            return None
        else:
            return self.data

    def close_socket(self):
            self.conn.close()

    def receive_message_counting(self):
        # TODO: Verify if receiving at middle of message
        MSGLEN = 10
        msg_list = []
        bytes_recd = 0

        while bytes_recd < MSGLEN:
            msg = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if msg == b'':
                raise RuntimeError("socket connection broken")
            msg_list.append(msg)
            bytes_recd = bytes_recd + len(msg)

        return b''.join(msg_list)

    def send_data_counting(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

