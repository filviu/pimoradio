pimoradio
=========

Raspberry PI Internet Radio - everybody should make one. The name comes
from Pi Modem Radio - because it's housed inside an old external modem case.

I didn't want to use mpd as it's a lot of pain to configure all kind of
plugins for buttons, lcd (if any) and I wanted to try my hand at python.

Eventually I will add schematics for driving a few leds and buttons.

Heavily based on http://www.linuxuser.co.uk/tutorials/raspberry-pi-portable-internet-radio

Usage
=====
Have radio.py start as root via some means (sudo from cron, rc.local, etc.) and preferably using a script to respawn it ~~when~~ if it crashes

Use getskylists.sh > stations.txt to generate a list of stations from
sky.fm (could stop working at any moment). This uses the free stations
list, no support for premium.

Alternatively create manually the list (one playlist url per line, no
comments, no empty lines because I'm not doing any input checks - as
this is a homebrew project)

Requirements
============
It requires mplayer and python. Button support is hardcoded to GPIO 23 and 24 (prev,next station in list)

*WARNING*
=========

* ~~For now it doesn't work - i.e. untill I build the buttons it will play 5s/stream and jump to the next one~~
* very rough and this from an amateur coder and python begginer
* as stated above the stations list is not checked in any way, and doesn't support comments, empty lines, etc. but it does *require* one empty line as the last line (if not your last station will never be reached)