#!/usr/bin/python
from time import sleep
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23 , GPIO.IN) # prev
GPIO.setup(24 , GPIO.IN) # next

statarr = []

with open("stations.txt") as stat_file:
    statarr = stat_file.readlines()

maxstat = len(statarr)-1 # reads whin one extra
stat = 0

# play something on start
print statarr[stat]
command = 'mplayer -really-quiet -slave -playlist '+statarr[stat]
mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
a = mp.poll()

while True:
    if GPIO.input(23)==1 and GPIO.input(24)==0:
	stat-=1
	if stat == -1 :
		stat=maxstat-1 			# empty line on last line
	print statarr[stat]
	if mp.poll() is None: 			# check if the process didn't crash in the mean time
	     mp.stdin.write('quit \n')
	command = 'mplayer -really-quiet -slave -playlist '+statarr[stat]
	mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
	sleep(0.5) # ignore long press

    if GPIO.input(24)==1 and GPIO.input(23)==0:
	stat+=1
	if stat == maxstat :
		stat=0
	print statarr[stat]
	if mp.poll() is None:
	     mp.stdin.write('quit \n')
	command = 'mplayer -really-quiet -slave -playlist '+statarr[stat]
	mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
	sleep(0.5) # ugly way to ignore longer presses
    if GPIO.input(24)==1 and GPIO.input(23)==1:
	sleep(1)
	if GPIO.input(24)==1 and GPIO.input(23)==1:
	    os.system("poweroff")
	    raise SystemExit(0)
    sleep(0.1);
GPIO.cleanup()
