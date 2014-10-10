#!/bin/bash
# Originally by Dan Fountain
# modifcations by silviu vulcan

# this might need customizing if you are not using SkyFm
INPUT=$(curl -s $1 | grep -m 1 Title | awk -F= '{print $2}' | sed 's/RadioTunes\ \-\ //')

#INPUT=$*
STRINGNUM=0

ary=($INPUT)

for key in "${!ary[@]}"; do
    SHORTTMP[$STRINGNUM]="${SHORTTMP[$STRINGNUM]} ${ary[$key]}"
    LENGTH=$(echo ${#SHORTTMP[$STRINGNUM]})
    if [[ "$LENGTH" -lt "100" ]]; then
	SHORT[$STRINGNUM]=${SHORTTMP[$STRINGNUM]}
    else
	STRINGNUM=$(($STRINGNUM+1))
	SHORTTMP[$STRINGNUM]="${ary[$key]}"
	SHORT[$STRINGNUM]="${ary[$key]}"
    fi
done

for key in "${!SHORT[@]}"
do
    echo "Playing line: $(($key+1)) of $(($STRINGNUM+1))"
    /usr/bin/mplayer -really-quiet "http://translate.google.com/translate_tts?tl=en&q=${SHORT[$key]}" >/dev/null 2>&1
done
