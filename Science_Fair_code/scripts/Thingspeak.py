import smbus
import time
import requests
import httplib, urllib
import math

i2c = smbus.SMBus(1)
address = 0x48


while True:

    # process of temperature sensoring
	block = i2c.read_i2c_block_data(address, 0x00, 12)
	temp = (block[0] << 8 | block[1]) >> 3
    	if(temp >= 4096):
        	temp -= 8192
    	value = temp / 16.0
    	msg = "Current temperature:%6.2f Deg. C. " % value
    	print(msg)
    	params = urllib.urlencode({'field1': value, 'key':'8U2TEG4CL6ZDD5PI'})
    	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    	conn = httplib.HTTPConnection("api.thingspeak.com:80") 
    	conn.request("POST", "/update", params, headers)
    	response = conn.getresponse()
    #print value
    #print response.status, response.reason
    	data = response.read()
        conn.close()
	
