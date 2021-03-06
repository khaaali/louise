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

translator = Translator('LouiseTranslator', '+AH3hqxjCwEewPTCVe5TshRLgJ3XpR2avkov4ijXxH8=')

"""

but accepts commands:
- `roll` - reply with a random integer between 1 and 6, like rolling a dice.
   current time- gives time and date at that moment
   system time - gives uptime of system
   name- will relpy with her name
   created- gives name of creator
   joke-tells a joke
   picture- takes picture and tweets
   temperature- gives the value of sensor data
   music -plays shuffled music
   weather country,city- gives you current weather information
   translate - translates from english to german    
"""

_songs=['UPDOWN.mp3','OutlandishAicha.mp3','MYLOVE.mp3','LinkinParkTheEnd.mp3','LinkinParkNumb.mp3','JojoTooLittleTooLate.mp3','IridiumCleanvsDirty.mp3','floridasugarft.wynter.mp3','Celine Dion - My Heart Will Go On.mp3','CassieMe&You.mp3','CashisEverythngShady.mp3','BritneySpears3.mp3','BONJOVIMYLIFE.mp3','BARBYGIRL.mp3','Bailamos.mp3','WEAREGOINGTOIBIZA.mp3','SPANISH.mp3','RhythmDivine.mp3']
_current_song= None

is_chatting = False

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()
    command_weather = msg['text'].lower() 

    global is_chatting
    
    print 'Got command: %s' % command
    	
    if 'roll' in command:
        bot.sendMessage(chat_id, random.randint(1,6))

    elif 'oosey' in command:
	buthu=random.choice(list(open('/home/pi/scripts/buthulu.txt')))
	bot.sendMessage(chat_id,str(buthu))

    elif 'system time' in command:
	uptime = subprocess.check_output(['python', '/home/pi/scripts/uptime.py'])
	bot.sendMessage(chat_id,str(uptime))

    elif 'name' in command:
        bot.sendMessage(chat_id,'My name is Louise')

    elif 'created' in command:
      	bot.sendMessage(chat_id,' I am the vision of Sairam')

    elif 'joke' in command:
        joke=random.choice(list(open('/home/pi/scripts/jokes.txt')))
        tts=gTTS(text=joke,lang='en-uk')
        tts.save('joker.mp3')
        mixer.init()
        pygame.mixer.music.load('joker.mp3')
        pygame.mixer.music.play()
        bot.sendMessage(chat_id,str(joke))


    elif 'picture' in command:
	subprocess.check_output(['python', '/home/pi/scripts/camerapi.py'])
        pic='I have posted your picture, in the Twitter, follow the link'
        tts=gTTS(text=pic,lang='en-uk')
        tts.save('pic.mp3')
        mixer.init()
        pygame.mixer.music.load('pic.mp3')
        pygame.mixer.music.play()
	bot.sendMessage(chat_id,str("Your tweet --> https://twitter.com/MyLouiseBot"))

    elif 'temperature sensor' in command:
	i2c = smbus.SMBus(1)
	address = 0x48	
	block = i2c.read_i2c_block_data(address, 0x00, 12)
	temp = (block[0] << 8 | block[1]) >> 3
    	if(temp >= 4096):
        	temp -= 8192
        value = temp / 16.0
    	temper = "your temperature sensor value is %6.2f Degree Celcius. " % value
        tts=gTTS(text=temper,lang='en-uk')
        tts.save('temper.mp3')
        mixer.init()
        pygame.mixer.music.load('temper.mp3')
        pygame.mixer.music.play()
        bot.sendMessage(chat_id,str(temper))

    elif 'hallo' in command:
	reply=open('/home/pi/scripts/hireply.txt','r')
	bot.sendMessage(chat_id,str(reply.readlines()))

    elif 'play music' in command:
        
	def play_shuffle_song():
            global _current_song, _songs
    	    next_song = random.choice(_songs)
            while next_song == _current_song:
        	next_song = random.choice(_songs)
	    print next_song
    	    _current_song = next_song
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
	    
        mixer.init()
        play_shuffle_song()
        bot.sendMessage(chat_id,"Enjoy the Music")
    
    elif 'stop music' in command:
	mixer.music.stop()
	bot.sendMessage(chat_id,"Music is Stopped")
    
    elif 'weather' in command_weather:
        words=command_weather.split()
        #print words
        length_words=len(words)
        #print length_words
        #print words[length_words-1]
        actual=str(words[length_words-1])
        word_=actual.split(',')
        actual_city = word_[0]+'/'+word_[1]
        url = 'http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/' + actual_city + '.json'
        f = urllib2.urlopen(url)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        city = parsed_json['location']['city']
        country_name = parsed_json['location']['country_name']
        weather = parsed_json['current_observation']['weather']
        temp_c = parsed_json['current_observation']['temp_c']
        feelslike_c = parsed_json['current_observation']['feelslike_c']
        final_city= 'Weather in ' + city + '-' + country_name + ': ' + weather.lower() + '.The temperature is ' + str(temp_c)+'degree Celsius' + ',but it feels like ' + str(feelslike_c)+'degree Celsius' + '.'
        f.close()
        tts=gTTS(text=final_city,lang='en-uk')
        tts.save('weeather.mp3')
        mixer.init()
        pygame.mixer.music.load('weeather.mp3')
        pygame.mixer.music.play()
        bot.sendMessage(chat_id,final_city)


    elif 'translate' in command:
	words=command.split(",")
	output= translator.translate(words[1], "de")
	encoded=output.encode('utf-8')
	tts=gTTS(text=encoded,lang='de')
        tts.save('translatee.mp3')
        mixer.init()
	bot.sendMessage(chat_id,encoded)
        pygame.mixer.music.load('translatee.mp3')
        pygame.mixer.music.play()


    elif 'repeat' in command:
        words=command.split(",")
        rep_out= words[1]
        tts=gTTS(text=rep_out,lang='en-uk')
        tts.save('repeat.mp3')
        mixer.init()
        bot.sendMessage(chat_id,rep_out)
        pygame.mixer.music.load('repeat.mp3')
        pygame.mixer.music.play() 


    elif 'winner' in command:
        words=command.split(",")
        win= words[1]
        win_int=int(win)
        winner_is= random.randrange(win_int)
        speech='So the Lucky winner for Todays SCIENCE FAIR is:'+str(winner_is)
        tts=gTTS(text=speech,lang='en-uk')
        tts.save('speech.mp3')
        mixer.init()
        bot.sendMessage(chat_id,speech)
        pygame.mixer.music.load('speech.mp3')
        pygame.mixer.music.play()



    elif 'darling' in command:
	dar=random.choice(list(open('/home/pi/scripts/darling.txt')))
        tts=gTTS(text=dar,lang='en-uk')
        tts.save('darlinge.mp3')
        mixer.init()
        bot.sendMessage(chat_id,str(dar))
        pygame.mixer.music.load('darlinge.mp3')
        pygame.mixer.music.play()

   
    elif 'hi' in command:
	is_chatting = True
        his='Hai, my name is Louisea, Welcome!!to the Science Fair'
        tts=gTTS(text=his,lang='en-uk')
        tts.save('hiis.mp3')
        mixer.init()
        bot.sendMessage(chat_id,his)
        pygame.mixer.music.load('hiis.mp3')
        pygame.mixer.music.play()



    elif 'bye' in command:
        is_chatting = False
        bot.sendMessage(chat_id, 'Bye Bye. take care!')
    elif is_chatting:
        bot.sendMessage(chat_id, iesha_chatbot.respond(command))

    else:
        sorry='I am sorry.I am un-authorised, to-do that!!'
        tts=gTTS(text=sorry,lang='en-uk')
        tts.save('sorry.mp3')
        mixer.init()
        bot.sendMessage(chat_id,sorry)
        pygame.mixer.music.load('sorry.mp3')
        pygame.mixer.music.play()

    #elif 'thingspeak' in command:	
	#subprocess.check_output(['python', '/home/pi/scripts/Thingspeak.py'])
	#bot.sendMessage(chat_id,str("Follow Link to visualize data -->https://thingspeak.com/channels/160149"))

bot = telepot.Bot('277021293:AAFVI_q3imw3F-3nW5kc03wgKBBFwnmW4RY')
bot.message_loop(handle)
print 'I am listening ...'


while 1:
	time.sleep(10)
mixer.init()
