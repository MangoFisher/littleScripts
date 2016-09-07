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
    ʹ��mockװ��������mock�����滻multiply������Ȼ�����ǽ�����Ϊһ������mock_multiply
    ���뵽���ǵĲ��Դ����У���������Ե��������У��κζ�multiply�����ĵ��ö��ᱻ�ض�
    ��mock_multiply����
    """

    @mock.patch("function.multiply")
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5

        # ����mock����ķ���ֵ��Ҳ������Ԥ��ֵ����assrtEqual�Ƚϵ�ֵ
        mock_multiply.return_value = 20

        addition, multiple = add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(20, multiple)


if __name__ == "__main__":
    unittest.main()
