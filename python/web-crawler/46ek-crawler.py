#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 知乎上的爬虫实例-国内站点，爬取video文件
import urllib2
import urllib
import datetime
import re
import os.path
import requests

def save_file(this_download_url,path):
    print('--------------------------------------------')
    time1 = datetime.datetime.now()
    print(str(time1)[:-7])
    if os.path.isfile(path):
        file_size = os.path.getsize(path)/1024/1024
        print("File" + path + " (" + str(file_size) + "Mb) already exists.")
        return
    else:
        print("Downloading " + path + "....")
        r = requests.get(this_download_url,stream = True)
        with open(path.encode('utf-8'),"wb") as code:
            code.write(r.content)
        
        time2 = datetime.datetime.now()
        print(str(time2)[:-7])
        print(path + "Done")
        use_time = time2 - time1
        print("Time used:" + str(use_time)[:-7])
        file_size = os.path.getsize(path)/1024/1024
        print("File size:" + str(file_size) + " MB,Speed:" + str(file_size/(use_time.total_seconds()))[:4] + "MB/s")

def download_the_av(url):
    mheader = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url,headers = mheader)
    content = urllib2.urlopen(req).read()
    while len(content) < 100:
        print("try again...")
        content = urllib2.urlopen(req).read()
    print("All length:" + str(len(content)))

    pattern = re.compile(r"http://m4.26ts.com/[.0-9a-zA-Z]*.mp4")
    match = pattern.search(content)
    if match:
        the_url = match.group()
        save_file(the_url,the_url[19:])
    else
        print("No video found.")

urls = ["http://www.46ek.c*m/view/22133.html",]
print(len(urls))
print("videos to download...")
count = 0

for url in urls:
    print count
    count += 1
    download_the_av(url)
print("All done")