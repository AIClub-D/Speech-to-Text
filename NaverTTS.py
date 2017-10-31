import os

import sys

import urllib.request

client_id = "input your id"

client_secret = "input your secret"

speakers = [

    'mijin',  # 한국어 여성

    'jinho',  # 한국어 남성

    'clara',  # 영어 여성

    'matt',  # 영어 남성

    'yuri',  # 일본어 여성

    'shinji',  # 일본어 남성

    'meimei',  # 중국어 여성

    'liangliang',  # 중국어 남성

    'jose',  # 스페인어 남성

    'carmen'  # 스페인어 여성

]


class NaverTTS():
    def __init__(self, speaker, speed):

        self.speaker = speakers[speaker]

        self.speed = str(speed)

    def play(self, sentence):

        encText = urllib.parse.quote(sentence)

        data = "speaker=" + self.speaker + "&speed=" + self.speed + "&text=" + encText;

        url = "https://openapi.naver.com/v1/voice/tts.bin"

        request = urllib.request.Request(url)

        request.add_header("X-Naver-Client-Id", client_id)

        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode('utf-8'))

        rescode = response.getcode()

        if (rescode == 200):

            print("TTS mp3 저장")

            response_body = response.read()

            with open('tts.mp3', 'wb') as f:

                f.write(response_body)

            os.system('omxplayer tts.mp3')

        else:

            print("Error Code:" + rescode)


if __name__ == "__main__":
    navertts = NaverTTS(1, 0)

    navertts.play("어쩌라고, 스페인어 여성")



