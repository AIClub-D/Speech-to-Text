#!/usr/bin/env python3

import os, sys
import urllib.request
import urllib.parse
import requests

s = "효원"
voice_recognize_flag = 0
URL = 'http://192.168.0.103:8000/'  # django server url
name = s.encode('utf-8')

while 1:
    # stt.sh 파일을 실행
    os.system('./stt.sh')
    f = open('speech_to_text.txt', 'r')
    content = f.read().encode('utf-8')
    str_len = len(content)
    content = content[:str_len - 1]

    # 이름을 부르면 voice_recognize_flag를 1로 세팅
    if name == content:
        voice_recognize_flag = 1
        continue

    if voice_recognize_flag == 1:
        value = {'sentence': content}

        # csrf cookie parts
        client = requests.session()
        client.get(URL)
        csrftoken = client.cookies['csrftoken']
        headers = {"X-CSRFToken": csrftoken, "Referer": URL}

        # 입력된 내용이 없을 때 get 요청
        if content == b'':
            res = client.get(URL, headers=headers)
        else:
            res = client.post(URL, data=value, headers=headers)

        result = res.content.decode('utf-8')
        print(result)
        voice_recognize_flag = 0

