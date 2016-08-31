# coding=utf-8

# 通过__slot__禁止类动态绑定属性，达到多实例的内存消耗
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

p1.x = u"可动态绑定属性"
print p1.x

p2.y = u"不可动态绑定属性"
print p2.y