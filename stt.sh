#!/bin/bash

echo "Recording... 5[sec] Press Ctrl+C to Stop."
arecord -D "plughw:1,0" -f S16_LE -t wav -r 16000 -d 5 > file.wav
curl -o stt.txt -X POST --data-binary @file.wav --header "Content-Type: audio/l16; rate=16000;" "your api key"
cat stt.txt | cut -d$'\n' -f2 | cut -d : -f4 | cut -d , -f1 | cut -d \" -f2 > speech_to_text.txt
cat stt.txt | cut -d$'\n' -f2 | cut -d : -f4 | cut -d , -f1 | cut -d \" -f2
