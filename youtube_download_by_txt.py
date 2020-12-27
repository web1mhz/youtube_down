# 유투브 동영상 다운로드

# 파이썬과 아나콘다 SSL 오류 날때 해결법

# 아나콘다가 설치된 G:\Anaconda3\Lib\site-packages\pip\_vendor\requests에 가서

# sessions.py를 메모장으로 열고

# 다음 python은 설치된 폴더 

# G:\Python38\Lib\site-packages\pip\_vendor\requests로 가서

# sessions.py를 메모장으로 열고 self.verify = False로 지정하면된다.

# 끝
# -*- conding: utf-8 -*-
import os
import subprocess
# pip install pytube3
import pytube
import time


in_file = input("url 리스트 파일? (예시: c:\\test.txt) ")
download_folder = input("어디에다 저장? (예시: c:\\test) ")
#저장 폴더 생성(Windows or mac)

start = time.time()
try:
    if not(os.path.isdir(download_folder)):
        os.makedirs(os.path.join(download_folder))
except OSError as e:
    if e.errno != errno.EXIST:
        print("Failed to create directory!!!!!")
        raise


# in_file = "test.txt"
url = open(in_file, 'r', newline='')
urls=[]

line = "init"
while line:
    line= url.readline().strip()
    urls.append(line)   


for url in urls:
    youtube_address = url
    if url =='':
        break
    print(youtube_address)
    yt = pytube.YouTube(youtube_address) #다운받을 동영상 URL 지정
    # vids=yt.streams.all() -- 오류 발생 : this is list object. all() is useless
    vids= yt.streams
    vids = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    parent_dir = download_folder
    # 동영상 2번 형식(video/mp4" res="720p" fps="30fps) 다운로드 수행
    time.sleep(10)
    vids.download(parent_dir)
    time.sleep(10)

    elasped_time = time.time() - start

print('동영상 다운로드', elasped_time, '초 걸림')





