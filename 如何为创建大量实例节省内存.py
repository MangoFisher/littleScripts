# coding=utf-8

# ͨ��__slot__��ֹ�ද̬�����ԣ��ﵽ��ʵ�����ڴ�����
import sys
class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    __slots__ = ["uid", "name", "status", "level"]
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

p1 = Player("0001", "Jim")
p2 = Player2("0001", "Jim")

p1.x = u"�ɶ�̬������"
print p1.x

p2.y = u"���ɶ�̬������"
print p2.y