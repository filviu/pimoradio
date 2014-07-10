#!/bin/bash
echo > $SKYLIST
while read LINE; do
    PLAYLIST=$(echo "$LINE" | awk -F\" '{print $4}')
    echo "$PLAYLIST"
done < <(curl -s http://listen.sky.fm/public1/ | grep -Po '"playlist":.*?[^\\]",')
