# -*- coding: utf-8 -*-

# startswith()��endswith()���ƥ��ʱ����ʹ��Ԫ��
import os
l = [name for name in os.listdir(".") if name.endswith((".py", ".pyc"))]
print l