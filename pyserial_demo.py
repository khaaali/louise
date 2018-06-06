import serial,os,sys,time
ser=serial.Serial("/dev/ttyUSB0", 57600, bytesize=8,timeout = 0.5)
buf=[] #buffer
n=0 #counter
while(True):
	if ser.inWaiting() != 0: 
		if(n==0 or n<3): # to check for 3 packets of data
			data=ser.read(34).encode("hex") # read 34 bytes serial data
			data= [''.join(x) for x in zip(*[iter(data)]*2)] # serial data is coverted to list  easy access 
			print data
			if(data):
				buf.append(data[8:22]) # slicing specific region for data
				print buf
				print buf[n][n]
				n=n+1
				if(n==3):	# when true checks the 3 appended packets in buffer for validity 
					if( buf[0][0]=='31' and buf[1][0]=='32' and buf[2][0]=='33'):
						print "valid data....sending response.."
						ser.write("\x55\x00\x01\x00\x05\x70\x03\x09")# tested with version number
						print ser.read(42).encode("hex")
						n=0 #reset
						buf=[]
	else:
		print 'waiting for data'
		time.sleep(1)
	

		






#000707017af60001a6b46e2002ffffffff2d0012

#55000707017af60001a6b46e2002ffffffff2e002d
#55000707017af60001a6b46e2002ffffffff2d0012

