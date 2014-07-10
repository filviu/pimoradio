#!/usr/bin/python
#import time import sleep
import time
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23 , GPIO.IN)
#GPIO.setup(24 , GPIO.IN)

statarr = []

with open("stations.txt") as stat_file:
    statarr = stat_file.readlines()

maxstat = len(statarr)
stat = 1

while True:
    print statarr[stat]
    os.system("sudo killall mplayer >/dev/null 2>/dev/null")
#    os.system("mplayer -really-quiet -playlist "+statarr[stat]+" >/dev/null 2>/dev/null &")
    command = 'mplayer -really-quiet -slave -playlist '+statarr[stat]
    mp = subprocess.Popen(command.split(),stdin=PIPE,stderr=subprocess.STDOUT, stdout=PIPE)
    time.sleep(5)
    mp.stdin.write('quit \n')
    stat+=1
    if stat > maxstat :
	stat=1
    time.sleep(0.1);
#GPIO.cleanup()
