# coding=utf-8

from concurrent.futures import ThreadPoolExecutor
import time

# �̳߳��������3���߳̿ɹ�����
executor = ThreadPoolExecutor(3)

def f(a, b):
    time.sleep(10)
    print("f", a, b)
    return a ** b

# ��ǰӳ�䵽�̵߳ĺ������ڿ�ִ���߳�����3�������̴߳���pending�ȴ�״̬
executor.map(f, [2, 3, 4, 5, 6], [3, 4, 5, 6, 7])