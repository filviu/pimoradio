pimoradio
=========

Raspberry PI Internet Radio - everybody should make one. The name comes
from Pi Modem Radio - because it's housed inside an old external modem case.

I didn't want to use mpd as it's a lot of pain to configure all kind of
plugins for buttons, lcd (if any) and I wanted to try my hand at python.

Eventually I will add schematics for driving a few leds and buttons.

Usage
=====

Use getskylists.sh > stations.txt to generate a list of stations from
sky.fm (could stop working at any moment). This uses the free stations
list, no support for premium.

Alternatively create manually the list (one playlist url per line, no
comments, no empty lines because I'm not doing any input checks - as
this is a homebrew project)

Requirements
============
It requires mplayer and python. When I add button support it will probably be hardcoded to the Pi

*WARNING*
=========

For now it doesn't work - i.e. untill I build the buttons it will play 5s/stream and jump to the next one
