#!venv/bin/python
# -*- coding:utf-8 -*-

import HD44780 as LCD
import time
import requests

lcd = LCD.HD44780('lcdsample.conf')
lcd.init()

class Marquee:
    offset = 0

    def __init__(self, text, length=16):
        self.text = text
        self.display = text[:length]
        self.length = length

    def tick(self, text=''):
        if text != '' and text != self.text:
            self.text = text
            self.offset = 0
            self.display = text[:self.length]
            return
        self.offset += 1
        self.offset = self.offset % (len(text) + 5)
        self.display = str((self.text + ' *** ' + self.text)[self.offset:self.offset + self.length])

def timeString(seconds):
    if seconds is None:
        return "00:00"
    minutes = int(seconds / 60)
    seconds = int(seconds - minutes * 60)
    minutesStr = ('0' if minutes < 10 else '') + str(minutes)
    secondsStr = ('0' if seconds < 10 else '') + str(seconds)
    return minutesStr + ':' + secondsStr

title = Marquee('')

while True:
    try:
        status = requests.get('http://192.168.1.11:3000/api/v1/getState').json()
    except:
        lcd.message("loading", 1)
        time.sleep(5)
        continue
    isPlaying = status['status'] == 'play' and len(status['bitdepth']) > 0
    lcd.setbacklight(isPlaying)
    if not isPlaying:
        time.sleep(2)
        continue
    lcd.message(title.display, 1)
    # print(title.display)
    seek = status['seek'] if status['seek'] is not None else 0
    print(seek)
    times = (timeString(int(seek) / 1000) + ' ' + timeString(status['duration']) + ' ' + status['trackType'])[:16]
    # print(times)
    lcd.message(times, 2)
    title.tick(status['title'] + ' : ' + status['artist'])
    time.sleep(1)
