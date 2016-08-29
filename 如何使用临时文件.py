# coding=utf-8

# 方法一:TemporaryFile创建的文件不能在文件系统中找到
# from tempfile import TemporaryFile,NamedTemporaryFile
#
# f = TemporaryFile()
# # 写入到临时文件
# f.write("abc" * 10000)
# # 文件指针重置到文件开始，以方便读取
# f.seek(0)
# # 从临时文件中读取内容
# print f.read(100)

# 方法二:NamedTemporaryFile创建的临时文件，可在文件系统中找到
from tempfile import TemporaryFile,NamedTemporaryFile
# 临时文件关闭后，默认会被删除delete=False可不删除
ntf = NamedTemporaryFile(delete=False)
# 生成的临时文件
print ntf.name