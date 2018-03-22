
import csv,os,sys,datetime
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import re

root = Tkinter.Tk()
root.withdraw()
fileString = tkFileDialog.askopenfile(parent=root,mode='r',filetypes=[("Excel file","*.csv")],title='Choose an CSV file')

# date and time for naming the output file
todayDt=datetime.datetime.now().strftime("D%Y-%m-%d_T%H-%M-%S")
file_name=todayDt+'MonthsReport'+'.txt'
print todayDt

if fileString != None:
    print "This CSV file has been selected", fileString

    pattern = '(?<=\')(.+csv)'
    m = re.findall( pattern, str(fileString))
    print m[0]
    csvPath= str(m[0])

# reading the csv data 
    csv_file= csv.reader(file(csvPath,'r'))
# for each row in csv data split is performed and re-arranging indexes in-order to acheive the desired output format.
    for row in csv_file:
    	for i in row:
    		line=i.split(';')
                print line

		# checking row for column names and eliminating that row 
    		if (line[2]=='KnotenID'or line[5]=='Uhrzeit'):
    			print 'column names will not be logged!!!'
			# re-arranging data with the indexes and formatting data.
    		else:
                
    			content= "NID:"+line[0]+';',"CURRENT:"+str((float(line[14])-0.01)*2040.8)  +';',"TEMP1:"+line[6]+';',"TEMP2:"+line[7]+';',"INCX:"+line[8]+';',"INCY:"+line[9
                ]+';',"TS:"+line[5]+'\n'
    			print content
			# appending the formatted data to the txt file
    			f = open(file_name,"a") 
    			f.writelines(" ".join(content))


# output will be generated with
# name:  date and time as .txt format 
# file location: same directroy of data_formater.py




	


	
	


