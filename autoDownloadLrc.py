# -*- coding: utf-8 -*- 
__author__ = "MangoFisher"
'''
自动为mp3文件下载歌词
'''
import os.path
import re
import eyed3
import urllib2
# from urllib import urlencode
import sys


reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
music_path = r"E:\music"
lrc_path = r"e:\lrc"
os.remove('nolrc.txt')
os.remove('lrcxml.txt')
the_file = open('lrcxml.txt','a')
nolrc_file = open('nolrc.txt','a')

for root,dirs,files in os.walk(music_path):
    for filepath in files:
        the_path = os.path.join(root,filepath)
        if (the_path.find("mp3") != -1):
            print the_path
            the_music = eyed3.load(the_path)
            the_teg = the_music.tag._getAlbum()
            the_artist = the_music.tag._getArtist()
            the_title = the_music.tag._getTitle()
            b = the_title.replace(' ','+')                
            a = the_artist.replace(' ','+')            
            if isinstance(a,unicode):
                a = a.encode('UTF-8')
            song_url = "http://box.zhangmen.baidu.com/x?op=12&count=1&title="+b+"$$"+a+"$$$$ "            
            the_file.write(song_url+'\n')
            page = urllib2.urlopen(song_url).read()
            print page
            theid = 0
            lrcid =  re.compile('<lrcid>(.*?)</lrcid>',re.S).findall(page)
            have_lrc = True
            if lrcid != []:
                theid = lrcid[0]
            else:
                nolrc_file.write(the_title+'\n')
                have_lrc = False
            print theid
            if have_lrc:
                firstid = int(theid)/100
                lrcurl = "http://box.zhangmen.baidu.com/bdlrc/"+str(firstid)+"/"+theid+".lrc"
                print lrcurl
                lrc = urllib2.urlopen(lrcurl).read()
                if(lrc.find('html')== -1):
                    lrcfile = open(lrc_path+"\\"+the_title+".lrc",'w')
                    lrcfile.writelines(lrc)
                    lrcfile.close()
                else:
                    nolrc_file.write(the_title+'\n')
the_file.close()
nolrc_file.close()
print "end!"