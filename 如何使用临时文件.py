# coding=utf-8

# ����һ:TemporaryFile�������ļ��������ļ�ϵͳ���ҵ�
# from tempfile import TemporaryFile,NamedTemporaryFile
#
# f = TemporaryFile()
# # д�뵽��ʱ�ļ�
# f.write("abc" * 10000)
# # �ļ�ָ�����õ��ļ���ʼ���Է����ȡ
# f.seek(0)
# # ����ʱ�ļ��ж�ȡ����
# print f.read(100)

# ������:NamedTemporaryFile��������ʱ�ļ��������ļ�ϵͳ���ҵ�
from tempfile import TemporaryFile,NamedTemporaryFile
# ��ʱ�ļ��رպ�Ĭ�ϻᱻɾ��delete=False�ɲ�ɾ��
ntf = NamedTemporaryFile(delete=False)
# ���ɵ���ʱ�ļ�
print ntf.name