# this program is coded to make ultrasonic sensor to detect object and execute a random function(task) from the list.

import RPi.GPIO as GPIO
import time
import time
import random
import datetime
import telepot
import subprocess
import smbus
import requests
import pyglet
import os
import urllib2
import json
import pygame
from pygame import mixer
import telepot, time
from nltk.chat.iesha import iesha_chatbot
wunderground_key = "80386ca03a8e512b"
from microsofttranslator import Translator
from gtts import gTTS


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
TRIG = 18
ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

n=0

_songs=['UPDOWN.mp3','OutlandishAicha.mp3','MYLOVE.mp3','LinkinParkTheEnd.mp3','LinkinParkNumb.mp3','JojoTooLittleTooLate.mp3','floridasugarft.wynter.mp3','Celine Dion - My Heart Will Go On.mp3','CassieMe&You.mp3']
_current_song= None



def Joke():
    joke1='you got joke, I will tell you a JOKE.'
    tts=gTTS(text=joke1,lang='en-uk')
    tts.save('joke1.mp3')
    mixer.init()
    pygame.mixer.music.load('joke1.mp3')
    pygame.mixer.music.play()
    time.sleep(3)
    joke2=random.choice(list(open('/home/pi/scripts/jokes.txt')))
    tts=gTTS(text=joke2,lang='en-uk')
    tts.save('joke2.mp3')
    mixer.init()
    pygame.mixer.music.load('joke2.mp3')
    pygame.mixer.music.play()

def Weather1():
    weather1='let me check, the weather in, Chemnitz'
    tts=gTTS(text=weather1,lang='en-uk')
    tts.save('weather1.mp3')
    mixer.init()
    pygame.mixer.music.load('weather1.mp3')
    pygame.mixer.music.play()
    url= 'http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/' + 'germany/chemnitz' + '.json'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    country_name = parsed_json['location']['country_name']
    weather = parsed_json['current_observation']['weather']
    temp_c = parsed_json['current_observation']['temp_c']
    feelslike_c = parsed_json['current_observation']['feelslike_c']
    final_city= 'Weather in ' + city + '-' + country_name + ': ' + weather.lower() + '.The temperature is ' + str(temp_c)+'degree Celsius' +',but it feels like ' + str(feelslike_c)+'degree Celsius' + ', ThankYou!.' 
    f.close()
    tts=gTTS(text=final_city,lang='en-uk')
    tts.save('weeather1.mp3')
    mixer.init()
    pygame.mixer.music.load('violent-thunder.mp3')
    pygame.mixer.music.play()
    #time.sleep(4)
    pygame.mixer.music.load('weeather1.mp3')
    pygame.mixer.music.play()

def Weather2():
    weather2='you got, weather, I will give you, todays weather in Hyderabad, India'
    tts=gTTS(text=weather2,lang='en-uk')
    tts.save('weather2.mp3')
    mixer.init()
    pygame.mixer.music.load('weather2.mp3')
    pygame.mixer.music.play()
    url= 'http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/' + 'india/hyderabad' + '.json'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    country_name = parsed_json['location']['country_name']
    weather = parsed_json['current_observation']['weather']
    temp_c = parsed_json['current_observation']['temp_c']
    feelslike_c = parsed_json['current_observation']['feelslike_c']
    final_city= 'Weather in ' + city + '-' + country_name + ': ' + weather.lower() + '.The temperature is ' + str(temp_c)+'degree Celsius' +',but it feels like ' + str(feelslike_c)+'degree Celsius' + ', ThankYou.'
    f.close()
    tts=gTTS(text=final_city,lang='en-uk')
    tts.save('weeather2.mp3')
    mixer.init()
    pygame.mixer.music.load('violent-thunder.mp3')
    pygame.mixer.music.play()
    #time.sleep(4)
    pygame.mixer.music.load('weeather2.mp3')
    pygame.mixer.music.play()


def Weather3():
    weather3='you got weather, here is the weather information of barcelona,spain'
    tts=gTTS(text=weather3,lang='en-uk')
    tts.save('weather3.mp3')
    mixer.init()
    pygame.mixer.music.load('weather3.mp3')
    pygame.mixer.music.play()
    url='http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/' + 'spain/barcelona' + '.json'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    country_name = parsed_json['location']['country_name']
    weather = parsed_json['current_observation']['weather']
    temp_c = parsed_json['current_observation']['temp_c']
    feelslike_c = parsed_json['current_observation']['feelslike_c']
    final_city= 'Weather in ' + city + '-' + country_name + ': ' + weather.lower() + '.The temperature is ' + str(temp_c)+'degree Celsius' +',but it feels like ' + str(feelslike_c)+'degree Celsius' + ',ThankYou.'
    f.close()
    tts=gTTS(text=final_city,lang='en-uk')
    tts.save('weeather3.mp3')
    mixer.init()
    pygame.mixer.music.load('violent-thunder.mp3')
    pygame.mixer.music.play()
    #time.sleep(4)
    pygame.mixer.music.load('weeather3.mp3')
    pygame.mixer.music.play()


def Picture():
    pic1='Congratulations!!...you got picture.I will take. your picture.Please,face, the camera'
    tts=gTTS(text=pic1,lang='en-uk')
    tts.save('pic1.mp3')
    mixer.init()
    pygame.mixer.music.load('pic1.mp3')
    pygame.mixer.music.play()
    subprocess.check_output(['python', '/home/pi/scripts/camerapi.py'])
    pic2='Well done!!,you look great.You can check my twitter for picture'
    tts=gTTS(text=pic2,lang='en-uk')
    tts.save('pic2.mp3')
    mixer.init()
    pygame.mixer.music.load('pic2.mp3')
    pygame.mixer.music.play()




def PlayMusic():
    playmusic='Have fun with music!!...I will play a song, from my playlist!!'
    tts=gTTS(text=playmusic,lang='en-uk')
    tts.save('playmusic.mp3')
    mixer.init()
    pygame.mixer.music.load('playmusic.mp3')
    pygame.mixer.music.play()
    time.sleep(5)
    global _current_song, _songs
    next_song = random.choice(_songs)
    while next_song == _current_song:
        next_song = random.choice(_songs)
        print next_song
    _current_song = next_song
    mixer.init()
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
    time.sleep(30)
    mixer.music.fadeout(1000)
    mixer.music.stop()


tasks=[Joke,Weather1,Weather2,Weather3,Picture,PlayMusic]


while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  #print "Waitng For Sensor To Settle"
  time.sleep(0.5)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  #print distance
  if distance > 5 and distance < 10:      #Check whether the distance is within range
    n=n+1
    print "Distance:",distance,"cm"  #Print distance with 0.5 cm calibration
    token= "ThankYou, for comming to the Science Fair, your token number is:"+ str(n)
    print token
    tts=gTTS(text=token,lang='en-uk')
    tts.save('token.mp3')
    mixer.init()
    pygame.mixer.music.load('token.mp3')
    pygame.mixer.music.play()
    time.sleep(4)
    random.choice(tasks)()
    

  elif distance < 4:
    print 'distance:',distance
    welcome= 'Hello!!, Welcome to the Science Fair.My name is Louisea,I am a Bot'
    tts=gTTS(text=welcome,lang='en-uk')
    tts.save('welcome.mp3')
    mixer.init()
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()

    

  else:
   a=1                  #display out of range
