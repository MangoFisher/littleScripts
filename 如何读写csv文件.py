# coding=utf-8

from urllib import urlretrieve
import csv

# 通过Yahoo接口下载数据文件
#urlretrieve("http://table.finance.yahoo.com/table.csv?s=000001.sz", "pingan.csv")

with open("pingan.csv", "rb") as rf:
    reader = csv.reader(rf)
    with open("pingan_copy.csv", "wb") as wf:
        writer = csv.writer(wf)
        header = reader.next()
        for row in reader:
            if row[0] < "2016-01-01":
                break
            if int(row[5]) >= 5000000:
                writer.writerow(row)
print("end")
