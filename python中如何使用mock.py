# coding=utf-8
"""
def multiply(x, y):
    return x * y + 3


def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)

    return addition, multiple
"""

import unittest
from function import add_and_multiply
import mock


class MyTestCase(unittest.TestCase):
    """
    使用mock装饰器来用mock对象替换multiply函数，然后我们将它作为一个参数mock_multiply
    插入到我们的测试代码中；在这个测试的上下文中，任何对multiply函数的调用都会被重定
    向到mock_multiply对象。
    """

    @mock.patch("function.multiply")
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5

        # 定义mock对象的返回值，也是最后给预期值进行assrtEqual比较的值
        mock_multiply.return_value = 20

        addition, multiple = add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(20, multiple)


if __name__ == "__main__":
    unittest.main()
