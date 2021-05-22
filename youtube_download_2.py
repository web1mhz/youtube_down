# 유투브 동영상 다운로드

# 파이썬과 아나콘다 SSL 오류 날때 해결법

# 아나콘다가 설치된 G:\Anaconda3\Lib\site-packages\pip\_vendor\requests에 가서

# sessions.py를 메모장으로 열고

# 다음 python은 설치된 폴더 

# G:\Python38\Lib\site-packages\pip\_vendor\requests로 가서

# sessions.py를 메모장으로 열고 self.verify = False로 지정하면된다.

# 끝
# -*- conding: utf-8 -*-
# -*- conding: utf-8 -*-
import os
import subprocess
# pip install pytube3
import pytube
from pytube.cli import on_progress

import time

youtube_address = input("동영상주소는? (예시: https://www.youtube.com/watch?v=whBV&index=13)")
yt = pytube.YouTube(youtube_address, on_progress_callback=on_progress) #다운받을 동영상 URL 지정


vids= yt.streams
vids = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
download_folder = input("어디에다 저장? (예시: c:\\test) ")


#저장 폴더 생성(Windows or mac)
try:
    if not(os.path.isdir(download_folder)):
        os.makedirs(os.path.join(download_folder))
except OSError as e:
    if e.errno != errno.EXIST:
        print("Failed to create directory!!!!!")
        raise


start = time.time()
vids.download(download_folder) 
elasped_time = time.time() - start

print('동영상 다운로드', elasped_time, '초 걸림')





