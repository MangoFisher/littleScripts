# coding=utf-8

# ����һ:ʹ�ñ�׼��os�е�����ϵͳ����stat��fstat��lstat
import os
import stat
import time
s = os.stat("test.txt")

# �ж��Ƿ�ΪĿ¼
print stat.S_ISDIR(s.st_mode)
# �ж��Ƿ�Ϊ��ͨ�ļ�
print stat.S_ISREG(s.st_mode)

# �ж��ļ���Ȩ��
print s.st_mode & stat.S_IRUSR

# ��ѯ�ļ�ʱ��
print time.localtime(s.st_atime)

# ��ѯ��ͨ�ļ��Ĵ�С
print s.st_size


# ������:ʹ�ñ�׼����os.path��һЩ���������Ӽ��
import os

# ����ļ�����
print os.path.isdir("test.txt")

# �ж��Ƿ�����ͨ�ļ�
print os.path.isfile("test.txt")

# ��ȡ�ļ�ʱ��
print os.path.getatime("test.txt")

# ��ȡ��ͨ�ļ���С
print os.path.getsize("test.txt")