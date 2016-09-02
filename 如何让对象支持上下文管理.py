# coding=utf-8

""""
 ʵ�������Ĺ���Э�飬�趨��ʵ����__enter__��__exit__������
 ���Ƿֱ���with��ʼ�ͽ���ʱ������
"""

from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None

    def start(self):


        t = self.tn.read_until("login: ")
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        t = self.tn.read_until("password: ")
        if t.startswith(user[:-1]):
            t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until("$")
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.read_until("$")
            stdout.write(t[len(uinput) + 1:])

    def cleanup(self):
        pass

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tn.close()
        self.tn = None
        with open(self.addr + "_history.txt", "w") as f:
            f.writelines(self.history)


client = TelnetClient("127.0.0.1")
client.start()
client.cleanup()