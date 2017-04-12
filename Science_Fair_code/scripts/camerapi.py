#This script will post pic to twitter acccount https://twitter.com/marias9124mari1
import picamera
import time
from time import sleep
import sys
from twython import Twython

camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.sharpness = 60
camera.contrast = 50
camera.brightness = 60
camera.saturation = 50
camera.ISO = 1150
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
sleep(2)

photo = open('image.jpg','rb')
time_now = time.strftime("%H:%M:%S") 
date_now =  time.strftime("%d/%m/%Y")
tweet_txt = "Photo captured by @LouiseBot at " + time_now + " on " + date_now


CONSUMER_KEY = 'nqWjIsVAA9CIuiwXNrFIryytZ'
CONSUMER_SECRET ='wH6b2ODTGGTaVBn7zQgxHNDWMJkueRnbaJZ3w4SemzVqo0L8j2'
ACCESS_KEY = '776493817721651204-rumxvAXkHYKcQLJxtwND9QI0rsk0nmL'
ACCESS_SECRET = 'Xv9aRrOgRaHBZ3uZRRdKhIbb78PnDvfOcd9Y2L8mDNplQ'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


api.update_status_with_media(media=photo, status=tweet_txt)

