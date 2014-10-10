#!/usr/bin/python
from time import sleep
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23 , GPIO.IN) # prev
GPIO.setup(24 , GPIO.IN) # next

statArr = []

with open("stations.txt") as stat_file:
    statArr = stat_file.readlines()
maxstat = len(statArr)-1 # reads with one extra why?

if os.path.isfile("stations.pos"):
    posFile = open("stations.pos") 
    statStr = posFile.read()
    statPos = int(statStr)
else:
    statPos = 0

# play something on start
print statArr[statPos]
os.system('./say-station.sh '+statArr[statPos])
command = 'mplayer -really-quiet -slave -playlist '+statArr[statPos]
mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
a = mp.poll()

while True:
    if GPIO.input(23)==1 and GPIO.input(24)==0:
	statPos-=1
	if statPos == -1 :
		statPos=maxstat-1 			# empty line on last line
	print statArr[statPos]
	if mp.poll() is None: 			# check if the process didn't crash in the mean time
	     mp.stdin.write('quit \n')
	os.system('./say-station.sh '+statArr[statPos])
	command = 'mplayer -really-quiet -slave -playlist '+statArr[statPos]
	mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
	posFile = open('stations.pos', 'w')
	posFile.write(str(statPos))
	posFile.close()
	sleep(0.5) # ignore long press

    if GPIO.input(24)==1 and GPIO.input(23)==0:
	statPos+=1
	if statPos == maxstat :
		statPos=0
	print statArr[statPos]
	if mp.poll() is None:
	     mp.stdin.write('quit \n')
	os.system('./say-station.sh '+statArr[statPos])
	command = 'mplayer -really-quiet -slave -playlist '+statArr[statPos]
	mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
	posFile = open('stations.pos', 'w')
	posFile.write(str(statPos))
	posFile.close()
	sleep(0.5) # ugly way to ignore longer presses
    if GPIO.input(24)==1 and GPIO.input(23)==1:
	sleep(1)
	if GPIO.input(24)==1 and GPIO.input(23)==1:
	    if mp.poll() is None:
		 mp.stdin.write('quit \n')
    sleep(0.1);
GPIO.cleanup()
