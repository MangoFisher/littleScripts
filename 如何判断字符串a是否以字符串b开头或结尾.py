# -*- coding: utf-8 -*-

# startswith()、endswith()多个匹配时参数使用元组
import os
l = [name for name in os.listdir(".") if name.endswith((".py", ".pyc"))]
print l