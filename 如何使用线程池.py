# coding=utf-8

from concurrent.futures import ThreadPoolExecutor
import time

# 线程池中最多有3个线程可供分配
executor = ThreadPoolExecutor(3)

def f(a, b):
    time.sleep(10)
    print("f", a, b)
    return a ** b

# 当前映射到线程的函数大于可执行线程总数3，会有线程处于pending等待状态
executor.map(f, [2, 3, 4, 5, 6], [3, 4, 5, 6, 7])